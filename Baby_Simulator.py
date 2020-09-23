#PY.01.08 Project 6: Baby conversation Simulator
#Description: This code gives us the question from the list mentioned using random and choice keywords
#             and it asks us the answer untill we give the answer as just because to keep on asking why.           
import random
# or use "from random import choice" --(1)
question = ["why is earth round in shape?: ","where does the god live?: ","Who is devil?: "]
question = random.choice(question) #Gives out the random question from the above list
#or if you have used the 1 now use question = choice(question)
answer=input(question).strip().lower()
while answer!="just because":
    answer=input("why?: ").strip().lower()
print("oh..! okay")
