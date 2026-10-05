from lfs_handoff import audit,VERSION
import tempfile,pathlib,hashlib,json
with tempfile.TemporaryDirectory()as t:
 r=pathlib.Path(t);p=r/'pointers';o=r/'objects';p.mkdir();o.mkdir();data=b'demo payload';oid=hashlib.sha256(data).hexdigest();f=o/oid[:2]/oid[2:4]/oid;f.parent.mkdir(parents=True);f.write_bytes(data);(p/'asset').write_text(f'{VERSION}\noid sha256:{oid}\nsize {len(data)}\n');a=audit(p,o);assert a['findings']==0;print(json.dumps(a))
