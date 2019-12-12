from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self):
        pass

class ConcreateStateB(State):
    def Handle(self):
        print("concreateStateB")

class ConcreateStateA(State):
    def Handle(self):
        print("concreateStatesA")

class Context(State):
    def __init__(self):
        self.state=None
    
    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state

    def Handle(self):
        self.state.Handle()

context = Context()
stateA = ConcreateStateA()
stateB = ConcreateStateB()
context.setState(stateB)
context.Handle()
context.getState()
