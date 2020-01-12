from cmd import Cmd
import docker
import container

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

    pass

cli = ahab()
cli.cmdloop()