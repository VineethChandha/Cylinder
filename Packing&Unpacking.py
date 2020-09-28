#PY.01.14 Introduction to packing and unpacking
L=[1,2,3,4]
P="abc"
print(P)
print(*P)
print(L)
print(1,2,3,4)
print(*L)   #* is used in unpacking the data




def add(*numbers):      #by using the * in parameter it acts as tuple and can take any number of arguments
    total=0
    for number in numbers:
        total=total+number
    print(total)
add(1,2,3,3,4,)


def about(name,age,like):
    s="{} is {} years old and likes {}".format(name,age,like)
    print(s)
dictionary={"name":"vineeth","age":24,"like":"playing"}
about(**dictionary)


def foo(**kwargs):    #for unpacking use ** as parameter
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
foo(ram="male",sita="female")
