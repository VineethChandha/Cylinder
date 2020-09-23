#PY.01.09 This code helps us to find number of vowels and consonents in the given word

vowels = 0
consonents = 0
word = input("Tell the word: ").lower().strip()
for letter in word:
    if letter in "aeiou":
   # if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
        vowels=vowels+1
    elif letter==" ":
        pass
    else:
        consonents=consonents+1
print("Number of vowels in the word are {}.".format(vowels))
print("Number of consonents in the word are {}.".format(consonents))

        
