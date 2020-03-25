import os
import json
from compyler.token import Token


tokens = {
    "+": "PLUS",
    "-": "MINUS",
    "/": "DIVIDE",
    "*": "MULTIPLY",
    "(": "OPEN",
    ")": "CLOSE"
}


class Tokenizer:
    def __init__(self, origin, position=0, actual=None):
        self.origin = origin
        self.position = position
        self.actual = actual

    def selectNext(self):
        lenOrigin = len(self.origin)
        for i in self.origin[self.position:]:
            if i.strip() == "":
                self.position += 1
            else:
                break

        if self.position >= lenOrigin:
            self.actual = Token("", "EOF")
        elif self.origin[self.position].isdigit():
            digit = ""
            i = self.position
            while i < lenOrigin and self.origin[i].isdigit():
                digit += self.origin[i]
                i += 1
            self.actual = Token(digit, "INT")
        elif self.origin[self.position] in tokens:
            actual = self.origin[self.position]
            self.actual = Token(actual, tokens[actual])
        else:
            raise Exception(
                f"[-] could not decode character at position {self.position}")

        self.position += len(self.actual.value)