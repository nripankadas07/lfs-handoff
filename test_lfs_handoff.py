import unittest,tempfile,pathlib,hashlib
from lfs_handoff import audit,pointer,VERSION
class Tests(unittest.TestCase):
 def fixture(self,t,data=b'payload'):
  p=pathlib.Path(t);ptr=p/'pointers';obj=p/'objects';ptr.mkdir();obj.mkdir();oid=hashlib.sha256(data).hexdigest();f=obj/oid[:2]/oid[2:4]/oid;f.parent.mkdir(parents=True);f.write_bytes(data);(ptr/'asset').write_text(f'{VERSION}\noid sha256:{oid}\nsize {len(data)}\n');return ptr,obj,f
 def test_valid_preserved(self):
  with tempfile.TemporaryDirectory()as t:
   p,o,f=self.fixture(t);before=(p/'asset').read_bytes();self.assertEqual(audit(p,o)['findings'],0);self.assertEqual((p/'asset').read_bytes(),before);self.assertEqual(f.read_bytes(),b'payload')
 def test_missing(self):
  with tempfile.TemporaryDirectory()as t:
   p,o,f=self.fixture(t);f.unlink();self.assertEqual(audit(p,o)['pointers'][0]['issue'],'missing_object')
 def test_same_length_corruption(self):
  with tempfile.TemporaryDirectory()as t:
   p,o,f=self.fixture(t);f.write_bytes(b'corrupt');self.assertEqual(audit(p,o)['pointers'][0]['issue'],'hash_mismatch')
 def test_size(self):
  with tempfile.TemporaryDirectory()as t:
   p,o,f=self.fixture(t);f.write_bytes(b'x');self.assertEqual(audit(p,o)['pointers'][0]['issue'],'size_mismatch')
 def test_object_symlink(self):
  with tempfile.TemporaryDirectory()as t:
   p,o,f=self.fixture(t);outside=pathlib.Path(t)/'outside';outside.write_bytes(b'payload');f.unlink();f.symlink_to(outside);self.assertEqual(audit(p,o)['pointers'][0]['issue'],'symlink_object')
 def test_ordinary_file(self):self.assertIsNone(pointer(b'ordinary data'))
 def test_malformed(self):
  with self.assertRaises(ValueError):pointer((VERSION+'\noid sha256:wrong\nsize 1\n').encode())
 def test_noncanonical(self):
  oid='0'*64
  for raw in [f'{VERSION}\r\noid sha256:{oid}\r\nsize 0\r\n',f'{VERSION}\noid sha256:{oid}\nsize 0']:
   with self.assertRaises(ValueError):pointer(raw.encode())
