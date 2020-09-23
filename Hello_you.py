# PY.01.02 Project - 2 Hello You! and some basics
# Introduces Input function 
#The input function always tends to be a string (str) irrespective of data type given.

#format function :
A="part"
B=1
print("{}-{}".format(A,B))
print("{1}-{0}".format(A,B))  # gives part-1 , 1-part


#Concatinating the strings using + , Repeating the strings using *
C="ram"
D="esh"
print(C+D)
print(C*5)


#Methods:

x="Happy Birthday"
print(type(x))
print(x.count("a")) #strings are immutable (will return to same form once entered independently after methods being executed) unless it is assigned.
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.index("Birth")) # gives the index or position and gives error when the string not found
print(x.find("Birth"))  # gives the index or position and gives -1 if the string does not present

Y="0000Happy0000"
print(Y.strip("0"))  #clears total
print(Y.lstrip("0")) # clears only left 
print(Y.rstrip("0")) #Clears only right
print(len(Y))  #Gives lenght of Y

# User name
name= input('What is your name?: ')
# User Age
age = input("Please enter your age: ")
# User city
city = input("Enter your city: ")
#Ask User what they enjoy
enjoy = input ("What does you enjoy?:")
#User details
print(name,",a superman of age",age,"lives in",city,"and enjoys",enjoy)
# user details using format fuction
string= "your name is {}. Your age is {}, lives in {} and enjoys {}"
output=string.format(name,age,city,enjoy)
print(output)


#Gives True or False:
#x.islower()
#x.isupper()
#x.isalpha() [it will validate the data to alphabets and <space> is not alpha)
#x.isdigit()
#x.isalnum()[alphanumeric]



