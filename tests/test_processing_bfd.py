import tempfile

from cuckoo.misc import set_cwd
from cuckoo.processing.bytes import ByteFrequencyDistribution

class TestProcessing(object):
    def setup(self):
        self.tmpdirs = []

    def teardown(self):
        for path in self.tmpdirs:
            try:
                shutil.rmtree(path)
            except:
                pass

    def mkdtemp(self):
        path = tempfile.mkdtemp()
        self.tmpdirs.append(path)
        return path

    def test_bytefreqdist(self):
        set_cwd(self.mkdtemp())

        bfd = ByteFrequencyDistribution()
        bfd.set_task({
            "category": "file",
            "package": "pdf",
            "target": "pdf0.pdf",
        })
        bfd.file_path = "tests/files/pdf0.pdf"
        results = bfd.run()
        sample_frequency_table = {
            '0D' : 8.529, '20': 13.529, '25': 2.059, '27': 0.294,
            '28': 0.441, '29': 0.441, '2B': 0.294, '2D': 0.147,
            '2E': 0.147,'2F': 3.529,'30': 15.294,'31': 1.765,
            '32': 1.471,'33': 0.735,'34': 1.176,'35': 1.618,
            '36': 1.618,'37': 1.029,'38': 0.294,'39': 0.147,
            '3B': 0.588,'3C': 2.206,'3D': 0.294,'3E': 2.059,
            '41': 0.294,'42': 0.147,'43': 0.441,'44': 0.147,
            '45': 0.147,'46': 0.294,'4A': 0.294,'4B': 0.147,
            '4C': 0.147,'4D': 0.147,'4F': 0.588,'50': 0.735,
            '52': 1.176,'53': 0.588,'54': 0.735,'5B': 0.294,
            '5D': 0.294,'61': 2.5,'62': 1.765,'63': 1.029,
            '64': 1.324,'65': 4.412,'66': 0.882,'67': 0.882,
            '68': 0.147,'69': 1.765,'6A': 1.765,'6C': 0.735,
            '6D': 0.294,'6E': 3.235,'6F': 3.088,'70': 1.176,
            '72': 1.765,'73': 1.471,'74': 2.353,'75': 0.735,
            '76': 0.441,'78': 0.735,'79': 0.735,'7A': 0.147,
            '7B': 0.147,'7D': 0.147,'shannon_entropy': 4.915}
        assert results == sample_frequency_table
        
