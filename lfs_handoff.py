"""Verify exported Git LFS pointers against an offline object directory."""
import argparse,hashlib,json,pathlib,os,re
VERSION='version https://git-lfs.github.com/spec/v1'

def pointer(raw):
    if not raw.startswith(VERSION.encode()):return None
    if len(raw)>=1024:raise ValueError('pointer must be less than 1024 bytes')
    try:s=raw.decode('ascii')
    except UnicodeError:raise ValueError('pointer must be ASCII')
    if not s.endswith('\n') or '\r' in s:raise ValueError('pointer requires canonical LF line endings')
    lines=s.splitlines()
    if len(lines)!=3 or lines[0]!=VERSION or not re.fullmatch(r'oid sha256:[0-9a-f]{64}',lines[1])or not re.fullmatch(r'size (0|[1-9][0-9]{0,18})',lines[2]):
        raise ValueError('unsupported or malformed v1 pointer; extensions not supported')
    return lines[1][11:],int(lines[2][5:])

def audit(pointer_root,object_root):
    root=pathlib.Path(pointer_root).resolve(strict=True);store=pathlib.Path(object_root).resolve(strict=True)
    if not root.is_dir()or not store.is_dir():raise ValueError('roots must be directories')
    rows=[];inspected=0
    for parent,dirs,files in os.walk(root,followlinks=False):
        dirs[:]=sorted(d for d in dirs if d!='.git'and not (pathlib.Path(parent)/d).is_symlink())
        for name in sorted(files):
            inspected+=1
            if inspected>100000:raise ValueError('100000 file limit exceeded')
            p=pathlib.Path(parent)/name
            if p.is_symlink():continue
            with p.open('rb')as f:raw=f.read(1025)
            try:parsed=pointer(raw)
            except ValueError as e:rows.append({'path':str(p.relative_to(root)),'issue':str(e)});continue
            if parsed is None:continue
            oid,size=parsed;obj=store/oid[:2]/oid[2:4]/oid
            row={'path':str(p.relative_to(root)),'oid':oid,'expected_size':size,'issue':None}
            if obj.is_symlink()or any(x.is_symlink()for x in [obj.parent,obj.parent.parent]):row['issue']='symlink_object'
            elif not obj.is_file():row['issue']='missing_object'
            else:
                actual=obj.stat().st_size;row['actual_size']=actual
                if actual!=size:row['issue']='size_mismatch'
                else:
                    h=hashlib.sha256()
                    with obj.open('rb')as f:
                        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
                    if h.hexdigest()!=oid:row['issue']='hash_mismatch'
            rows.append(row)
    return {'pointers':rows,'findings':sum(x['issue']is not None for x in rows),'pointer_count':len(rows)}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('pointers');p.add_argument('objects');a=p.parse_args()
    try:
        r=audit(a.pointers,a.objects);print(json.dumps(r));return 2 if not r['pointer_count']else int(bool(r['findings']))
    except (ValueError,OSError)as e:print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
