
__author__ = "David Fogelman"
__license__ = "MIT"
__version__ = "3.0.1"
__maintainer__ = "David Fogelman"
__status__ = "Production"

__all__ = ['node',
           'parser',
           'preprocessor',
           'token',
           'tokenizer']

import os
from compyler.parser import Parser
from compyler.preprocessor import Preprocessor
from compyler.symboltable import SymbolTable


def _run(code, path=os.path.join("compyler", "model.asm")):
    preprocessed = Preprocessor.run(code)
    parsed = Parser.run(preprocessed)
    symboltable = SymbolTable()

    with open(path, "r") as file:
        code = file.read()
        code += parsed.Evaluate(symboltable)[0]
        code += """
; interrupcao de saida
POP EBP
MOV EAX, 1
INT 0x80"""
    return code
