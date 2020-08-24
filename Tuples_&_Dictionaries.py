# Introduction to Tuples and Dictionaries

L = [1,2,3]
L.insert(3,4)#A.insert(position,value) 
print(L)
L.insert(3,5)
print(L)
L=L+[6]     #+ is used to add the elements to the list
print(L)
L=L+list("ab") # it adds the a,b to thr list
print(L)
L=L+[7,8,9] # we cant add number like this L=L+list(7,8,9)
print(L)

#Tuples

tuple = 1,2,3,"A"
print(tuple)
# tuple[2] = 8 this cannot be done since tuples are immutable there values cannot be changed
A,B,C = 1,2,3
print(A)
print(B)
print(C)
s="12345"
# s[1]=4        This cannont be done because strings are immutable
# print(s)


#Dictionaries

Students ={
            "A":["ID0001",21,"P"],          # A is the key next to that is the value
            "B":["ID0002",22,"F"],
            "C":["ID0003",23,"P"]
            }
print(Students.keys())      #Gives all the keys
print(Students.values())    #Gives all values
print(Students.items())     # Gives all the tuples couples
print(Students["A"])
print(Students["C"][0])
print(Students["C"][0:2])
del Students["C"]       #Delets entire C 
print(Students.keys()) 

Students ={
            "A":{"id":"ID0001","age":21,"result":"P"},
            "B":{"id":"ID0002","age":22,"result":"f"},
            "C":{"id":"ID0003","age":23,"result":"P"}
            }
print(Students["A"]["age"])

