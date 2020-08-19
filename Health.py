# Project 1 - crafting a health portion
#Description : Gives a random health score by using predefined random function 
import random
health = 50
level=3
portion_health = int(random.randint(10,20)/level) #Here int is used to make sure it gives only integer but not float
health= health * portion_health
print(health)
