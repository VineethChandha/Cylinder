#PY.01.07 Project 5: Cinema Simulator
#Description: This is the code for booking tickets by checking the availabilty od tickets and validating age using dictionaries and loops

film ={
    "After Age":{"age":10,"tickets":5},
    "Brand":{"age":12,"tickets":3},
    "Clock":{"age":18,"tickets":1},
    }
while True:
    user_film=input("Enter the film name: ").strip().title()
    if user_film in film.keys():
        age=int(input("Please enter ther age: ").strip())
        if age>=film[user_film]["age"]:
            if film[user_film]["tickets"]>0:
                print("enjoy the film")
                film[user_film]["tickets"]=film[user_film]["tickets"]-1
            else:
                print("No tickets available")
        else:
            print("You are too young to watch this film")
    else:
        print("Sorry, We dont have that film")
