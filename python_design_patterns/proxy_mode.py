# 代理模式

class Actor(object):
    def __init__(self):
        self.isBuy = True
    
    def occupied(self):
        self.isBuy = True
        print(type(self).__name__, "is occupied with cvurrent movie")

    def available(self):
        self.isBuy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBuy

class Agent(object):

    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == "__main__":
    r = Agent()
    r.work()