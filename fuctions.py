#PY.01.12 This is a program to introduce the Finctions concept and using it created a string reverse program

text=input("enter the name to get the reverse name: ").strip().lower()
def rev(x):
    return x[::-1]
reverse = rev(text)
print(reverse)

def about(name,age,like="football"):
    #foot ball will be defalut value if the fuctioncal does not contain like
    #defalut parameters should be at last
    s="{} is {} years old and likes {}".format(name,age,like)
    print(s)
about("ram",23,"tennis")
about("ram",23)  # ram,23,tennies are called arguments
