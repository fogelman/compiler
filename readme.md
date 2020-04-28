# compyler

A revolutionary language to make your life harder

[![Build Status](https://travis-ci.com/Fogelman/compyler.svg?token=m4KMpTsinBJNfZSW8czm&branch=APS)](https://travis-ci.com/Fogelman/compyler)

### Requirements

```
python >= 3.x
make >= 4.x
pip
```

### Setup

```
pip install -r requirements.txt
```

### Test

The tests can be found in `./tests/tests.json`

```
make test
```

### Project Structure

```
compyler/
├── __init__.py
├── lexer.py
├── node.py
├── parser.py
└── symboltable.py
```

### References

[Using RPython and RPly to build a language interpreter](https://joshsharp.com.au/blog/rpython-rply-interpreter-1.html)

[Writing your own programming language and compiler with Python](https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)

[Python's full Grammar specification](https://docs.python.org/3/reference/grammar.html)

[joshsharp/python-braid lexer.py](https://github.com/joshsharp/python-braid/blob/master/lexer.py)

[radk0s/ply SymbolTable.py](https://github.com/radk0s/ply/blob/master/Symboltable.py)

[zjl233/moe parser.py](https://github.com/zjl233/moe/blob/master/src/parser.py)
