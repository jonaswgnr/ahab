import unittest
import docker
import container
from io import StringIO
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout

class TestAhab(unittest.TestCase):
    client = docker.from_env()
    testcontainerName = "testcontainer"

    def setUp(self):
        self.client.containers.run("ubuntu", detach=True, command="sleep infinity", name=self.testcontainerName)

    def tearDown(self):
        container = self.client.containers.get(self.testcontainerName)
        container.remove(force=True)

    def testList(self):
        with Capturing() as listOut:
            container.list_container(self, "")
        self.assertIn(self.testcontainerName, str(listOut))
        self.assertIn("running", str(listOut))

    def testStop(self):
        with Capturing() as stopOut:
            container.stop_container(self, "thisshouldnotbefound")
        self.assertIn("Container not found", str(stopOut))

    def testListAll(self):
        with Capturing() as listAllOut:
            container.list_container(self, "-a")
        self.assertIn(self.testcontainerName, str(listAllOut))
        self.assertIn("exited", str(listAllOut))



if __name__ == '__main__':
    unittest.main()