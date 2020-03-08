from texttable import Texttable

def pull_image(self, inp):
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
    self.client.images.remove(name)

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

