#PY.01.11 Project 7:Pig Latin Translator
#Description: pig latin is a text coding here word starting with vowel will be just added with
#             yay in the end where as word starting with consonents will be changed as this boy --> oybay


# taking input sentance from user
sentance = input("enter the sentence: ").strip().lower()
# spliting the sentance into words using split function and storing it as list of words
words= sentance.split()
new_words=[]
# validate the words
for word in words:
    # if 1st letter is vowel
    if word[0] in "aeiou":
        new_word=word+"yay"
        # append the changed word to the new words list
        new_words.append(new_word)
    else:
        count=0
        # validate letter by letter
        for letter in word:
             if letter not in "aeiou":
                    count=count+1
             else:
                break
        #split the word till the consonents
        con = word[:count]
        # rest of the word
        rest = word[count:]
        #join to form new word
        new_word=rest+con+"ay"
        new_words.append(new_word)
# join function is used to make the list of words to a sentence with space mentioned
output=" ".join(new_words)
print(output)
