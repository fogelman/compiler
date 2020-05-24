# https://joshsharp.com.au/blog/rpython-rply-interpreter-1.html
from compyler import _run
code = """

a fifty-fifty 5111
print(a)

isit(a ==1){
    print(0)
}other{
    b fifty-fifty 5
    print(b)
}
"""
result = _run(code)


with open("output.o", "wb") as file:
    file.write(result)

# def fibbonacci(n):
#     if(n == 0):
#         return 0
#     else:
#         if(n == 1):
#             return 1
#         else:
#             return (fibbonacci(n-1) + fibbonacci(n-2))


# print(fibbonacci(10))
