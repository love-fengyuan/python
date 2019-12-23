# -*- encoding: utf-8 -*-

class Singleton(object):
    def __new__(cls):
        if not  hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("object created", s)

s1 = Singleton()
print("objects created", s1)

# 单列模式中的懒汉模式

class Singleton:
    __instance = None
    def __init__(slef):
        if not Singleton.__instance:
            print("__init__ method called ..")
        else:
            print("Instance already created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("object created", Singleton.getInstance())

s1 = Singleton()