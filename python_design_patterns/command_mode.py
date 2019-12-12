class Wizard():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def perferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("copying binaries --", self.src, "to", self.rootdir)
            else:
                print("no operation")

if __name__ == "__main__":
    wizard = Wizard("python3.5.gzip", "/usr/bin/")
    wizard.perferences({"python": True})
    wizard.perferences({"java":False})
    wizard.execute(