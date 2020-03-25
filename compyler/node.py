
from abc import ABC, abstractmethod


class Node(ABC):

    @abstractmethod
    def Evaluate(self):
        pass


class BinOp(Node):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        if children is None:
            self.children = list()

    def Evaluate(self):
        if self.value == "PLUS":
            return self.children[0].Evaluate() + self.children[1].Evaluate()
        elif self.value == "MINUS":
            return self.children[0].Evaluate() - self.children[1].Evaluate()
        elif self.value == "DIVIDE":
            return self.children[0].Evaluate() // self.children[1].Evaluate()
        elif self.value == "MULTIPLY":
            return self.children[0].Evaluate() * self.children[1].Evaluate()


class UnOp(Node):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        if children is None:
            self.children = list()

    def Evaluate(self):
        if self.value == "PLUS":
            return self.children[0].Evaluate()
        elif self.value == "MINUS":
            return -self.children[0].Evaluate()


class IntVal(Node):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        if children is None:
            self.children = list()

    def Evaluate(self):
        return self.value


class NoOp(Node):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        if children is None:
            self.children = list()

    def Evaluate(self):
        return
