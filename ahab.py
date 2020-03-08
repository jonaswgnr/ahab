#!/usr/bin/env python3

from cmd import Cmd
import docker
import container
import image


class ahab(Cmd):
    prompt = "Ahab> "
    client = docker.from_env()

    def emptyline(self):
        pass

    def do_exit(self, inp):
        print("Leaving Ahab")
        return True

    def do_ls(self, inp):
        container.list_container(self, inp)

    def do_list(self, inp):
        container.list_container(self, inp)

    def do_ps(self, inp):
        container.list_container(self, inp)

    def do_stop(self, inp):
        container.stop_container(self, inp)

    def do_start(self, inp):
        container.start_container(self, inp)

    def do_rm(self, inp):
        container.remove_container(self, inp)

    def do_remove(self, inp):
        container.remove_container(self, inp)

    def do_pull(self, inp):
        image.pull_image(self, inp)

    def do_image(self, inp):
        command = inp.split()[0]
        params = inp.split()[1:]
        if command in ["ls","list"]:
            image.list_images(self, params)
        if command in ["rm","remove"]:
            image.remove_image(self, params[0])
    pass

cli = ahab()
cli.cmdloop()