```
input: [NEWLINE] (stmt)*

exprlist: expr (',' expr)* [',']
testlist: test (',' test)* [',']
testlist_expr: (test|expr) (',' (test|expr))* [',']
arglist: argument (',' argument)*
argument: NAME

NEWLINE: '\n' | '\n' NEWLINE

suite: '{' NEWLINE stmt+ '}'
stmt: (simple_stmt | compound_stmt )
simple_stmt: ( expr_stmt | return_stmt ) NEWLINE
expr_stmt: (test | NAME 'fifty-fifty' test)
return_stmt: 'return' [testlist]

compound_stmt: (if_stmt | while_stmt | funcdef | print_stmt ) [NEWLINE]
if_stmt: 'isit' test suite ['other' suite]

while_stmt: 'during' test suite
funcdef: 'hmmm' NAME '(' [arglist] ')' suite
funccall: NAME '(' [testlist] ')'

print_stmt: 'print' '(' (test|expr) ')'

test: and_test ('or' and_test)*
and_test: not_test ('and' not_test)*
not_test: 'not' not_test | comparison
comparison: expr (('<'|'>'|'=='|'>='|'<='|'!=') expr)*
expr: arith | (arith ('|', '^', '&') expr)
arith: term | (term ('+'|'-') arith)
term: factor | (factor ('*'|'/'|'%'|'//') term)
factor: ('+'|'-'|'~') factor | atom
atom: '(' test ')' | NAME | NUMBER | 'None' | 'True' | 'False' | funcall
```
