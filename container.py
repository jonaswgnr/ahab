import docker.errors
from texttable import Texttable

def list_container(self, params):
    if "a" in params:
        containers = self.client.containers.list(all=True)
    else:
        containers = self.client.containers.list(all=False)
    containerList = Texttable()
    containerList.add_row(['ID',
                           'Name',
                           'Image',
                           'Status'
                           ])
    for container in containers:
        containerList.add_row([getattr(container, "id")[0:15],
                               getattr(container, "name"),
                               getattr(container, "image").attrs["RepoTags"][0],
                               getattr(container, "status")
                               ])
    print(containerList.draw())

def stop_container(self, container_id):
    try:
        container = self.client.containers.get(container_id)
        container.stop()
    except docker.errors.NotFound:
        print("Container not found")
    except Exception as e:
        print(e)

def start_container(self, container_id):
    try:
        container = self.client.containers.get(container_id)
        container.start()
    except docker.errors.NotFound:
        print("Container not found")
    except Exception as e:
        print(e)

def remove_container(self, container_id):
    try:
        container = self.client.containers.get(container_id)
        container.remove()
    except docker.errors.NotFound:
        print("Container not found")
    except Exception as e:
        print(e)
