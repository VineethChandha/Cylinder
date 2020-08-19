# Project 4 - Travis the Ridiculous Security System
# Description - This code helps us to add or delete the name given by user into the List.
#Python list can have multiple data types. List = [1,2,"a",True]

my_list = ["Vineeth","Varun","Varshini"]
while True:
    name=input("Enter your name: ").strip().capitalize()
    if name in my_list:         # in keyword is used to see the existence of the specified word in the given list. ex L=[1,2] | 2 in L | True
        print("Name recognized")
        output= "Hello {}!"
        print(output.format(name))
        remove=input("Would you like to remove your name from the list (y/n)?").upper()
        if remove=="Y":
            my_list.remove(name)    #remove function to remove the items in list or can use del function    L=[1,3]

                                                                                                            #del L[0] --> del fuction removes 1st instance

                                                                                                            #del L[0:2] --> Removes the slice
            print(my_list)
        else:
            print(my_list)
        
    else:
        print("Name Not recognized")
        output= "Hello {}!"
        print(output.format(name))
        add=input("Would you like to add your name(Y/N)?: ").upper()
        if add=="Y":
            my_list.append(name)            #append function is to add item to the list.
            print(my_list)
        else:
            print(my_list)
    
