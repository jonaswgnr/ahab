import docker
from texttable import Texttable

def pull_image(self, inp):
    self.apiclient = docker.APIClient(base_url='unix://var/run/docker.sock')
    image = inp.split(':')[0]
    try:
        tag = inp.split(':')[1]
    except IndexError:
        print("No tag given, using latest")
        tag = 'latest'
    print("Pulling: " + image + ':' + tag)
    for line in self.apiclient.pull(image, stream=True, tag=tag, decode=True):
        if 'progress' in line:
            print(line['progress'])

def remove_image(self, name):
    print("Removing: " + name)
    try:
        self.client.images.remove(name)
    except docker.errors.ImageNotFound:
        print("Image not found")

def list_images(self, params):
    if "a" in params:
        images = self.client.images.list(all=True)
    else:
        images = self.client.images.list(all=False)
    imageList = Texttable()
    imageList.add_row(['ID','Tag'])
    for image in images:
        imageList.add_row([getattr(image, "id").split(':')[1][0:15], getattr(image, "tags")])
    print(imageList.draw())

