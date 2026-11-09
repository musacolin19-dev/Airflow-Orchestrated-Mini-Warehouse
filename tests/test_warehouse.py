import tempfile,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from warehouse import run
class TestWarehouse(unittest.TestCase):
    def test_run_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            db=Path(d)/'test.db'
            self.assertEqual(run(db),run(db))
            self.assertEqual(run(db)[0][2],200.0)
