# PY.01.10 introduction to the loops

for a in range(1,11):   # a will be valuated from 1 to 10   
    print("Hi")
    print(a)

even_numbers = [x for x in range(1,100) if x%2 == 0]
print(even_numbers)
odd_numbers = [x for x in range(1,100) if x%2 != 0]
print(odd_numbers)
words = ["ram","krishna","sai"]
answer = [[w.upper(),w.lower(),len(w)] for w in words]
print(answer)

word = ["Happy","Birthday","To","You"]
word="-".join(word)     #Join key word is used to join the list of the words with some specific sign or space as required
print(word)

Word2 = "Happy Birthday To You"
split_word = Word2.split()      #.split() funtion is used to make the sentance to the list of words
print(split_word)


# This brings out the names of friends in which letter a is present
names={"male":["sandeep","rakesh","sudheer",],"female":["sravani","dolly"]}
for gender in names.keys():
    for friend in names[gender]:
        if "a" in friend:
            print(friend)
