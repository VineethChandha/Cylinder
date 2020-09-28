# PY.01.13 This is the program to explain the scope of variables

a=100
def f1():
    global a #will change the value of a globally
    a=10
    return a
def f2():
    a=50
    return a
print(f1())
print(f2())
print(a)


b=[1,2,3,]
def f1():
    b[0]=5   # In this case we no neeth to specify the global keyword
    print(b)
def f2():
    b=10
    print(b)
f1()
f2()
print(b)
