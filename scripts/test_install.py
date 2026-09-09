import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

INSTALL = Path(__file__).with_name('install.py')

class InstallTests(unittest.TestCase):
    def test_install_and_refuse_existing_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            argv=[sys.executable,str(INSTALL),'project-artifact-cleanup','--dest',directory]
            result=subprocess.run(argv,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            installed=Path(directory)/'project-artifact-cleanup'
            self.assertTrue((installed/'SKILL.md').is_file())
            self.assertTrue((installed/'scripts/artifacts.py').is_file())
            self.assertFalse(list(installed.rglob('*.pyc')))
            marker=installed/'keep.txt';marker.write_text('local customization')
            second=subprocess.run(argv,capture_output=True,text=True)
            self.assertNotEqual(second.returncode,0)
            self.assertEqual(marker.read_text(),'local customization')

if __name__=='__main__': unittest.main()
