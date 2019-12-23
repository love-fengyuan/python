from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAnsRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class IOSCompiler(Compiler):

    def collectSource(self):
        print("collecting seift source code")

    def compileToObject(self):
        print("compiling swift code to LLVM bitcode")

    def run(self):
        print(" program runing on runtime environment")

IOS = IOSCompiler()
IOS.compileAnsRun()