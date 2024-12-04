from itertools import count
from operator import countOf, index
from random import random
from sys import stdlib_module_names

"""#  1   Create a dictionary with some key-value pairs.
dict1 = {'name':'lalith','age':'23','country':'India'}
print(dict1)

# 2
sample_data ={'name':'anil','age':21,'College':'abc'}
s=sample_data.keys()
print(s)
t=sample_data.values()
print(t)
sample_data.update({'class':12})
print(sample_data)
sample={'College':'sri indu'}
sample_data.update(sample)
print(sample_data)
u=sample_data.get('age')
print(u)

# 3
x1 = ['fruit','vegetable','gender','name']
x2 =['apple','potato','female','john']
x3 =dict(zip(x1,x2))
print(x3)

# 4
l=[1,2,3,4,5,6,7]
l.insert(4,8)
l.pop()
l.append("anil")
l[1]=str(l[1])
l.pop()
l.remove('2')
print(l)

# 5
l1 = ['king','queen',23,'bhAAi','atom']
a = l1[0:2]
b=l1[3:]
print(a+b)

# 6
l3=[1,2,3,4,5,6,7,8]
l4=['a','b','c','d','e']
c=l3+l4
print(c)

# 7
d= len(l3)
print(d)

# 8
l5=[1,2,3,45,123,1,2,2,2,2,2,2,3]
w=l5.count(2)
print(w)

# 9
l5=[1,2,3,45,123,1,2,2,345,2,2,2,3]
l5.reverse()
print(l5)

# 10
l6=[1,2,3,45,123,1,2,2,345,2,2,6,7,8,9,0,55,543,2,3]
l6.sort()
print(l6)

# 11
dict2={'abbu','jigar','dada'}
dict3={'baloo','tiger',22}
f= dict2 | dict3
print(f)

# 12
dict4 = {'naame':'lalith','age':'23','country':'India'}
dict4.clear()
print(dict4)

# 13
sports=['tennis','football']
sports.append('kabaddi')
sports.sort()
print(sports)

# 14

subjects=['telugu','hindi','english','maths','science','social']
subject=input("enter the subject you dont like:")
for i in subjects:
   if i == subject:
       subjects.remove(subject)
        print(subjects)
        break
else:
    print('choose a valid subject')

# 15

fav_foods = {}
for i in range(1, 5):
    food = input(f"enter your {i} favorite food: ")
    fav_foods[str(i)] = food
print("your favorite foods are:")
for food_num, food_name in fav_foods.items():
    print(f"{food_num}: {food_name}")
least_fav = input("enter the number of food you dont like ")
if least_fav in fav_foods:
    del fav_foods[least_fav]
    print("removed least fav food from your fav foods.")
else:
    print("invalid input. Please enter a valid number.")
print("your updated favorite foods are:")
for food_num, food_name in fav_foods.items():
    print(f"{food_num}: {food_name}")

# 16

colors=['red','blue','green','orange','yellow','orange','pink',
        'black','white','purple','cyan','voilet']
user_colors=[]
while len(user_colors) < 5:
    c = input("inter a color from the list (excluding the first and last): ")
    if c in colors and c not in [colors[0], colors[-1]]:
        user_colors.append(c)
    else:
      print("invalid color choice. Please try again.")
print("user colors:")
for color in user_colors:
    print(color)

# 17
countries=("ind","nzl","usa","aus","pak")
list(countries)
print(countries)
one_counrty=input("enter one country that have been shown:")
if one_counrty in countries:
    print(countries.index(one_counrty))
num=input("enter the number")
if num (countries):
    print("country at the index:",num(index()))

# 18

Sports=['cricket','football']
user_sport=input("enter your fav sport:")
Sports.append(user_sport)
print(Sports)

# 19

Subjects = ['english','maths','physics','chemistry','biology','social']
dl=input("enter the subject you dont like:")
if dl in Subjects:
    Subjects.remove(dl)
    print(Subjects)"""

# 21

"""Colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white"]

start_num = int(input("Enter a starting number between 0 and 4: "))
end_num = int(input("Enter an end number between 5 and 9: "))

if 0 <= start_num <= 4 and 5 <= end_num <= 9:
    selected_colors = Colors[start_num:end_num+1]
    print("Selected colors:")
    for Colors in selected_colors:
        print(Colors)
else:
    print("Invalid input. Please enter numbers within the specified ranges.")"""














# 22


"""numbers = [123, 456, 789, 321]
print("Here are the numbers in the list:")
for number in numbers:
    print(number)
user_input = int(input("Please enter a three-digit number: "))
if user_input in numbers:
    position = numbers.index(user_input)  # Get the index of the number
    print(f"The number {user_input} is at position {position} in the list.")
else:
    print("That is not in the list.")

# 23

nums = []
for _ in range(3):
    number = input("Enter a number: ")
    nums.append(number)
    print("Current list:", nums)
keep_last = input("Do you want to keep the last number you entered? (yes/no): ").strip().lower()
if keep_last == "no":
    nums.pop()
print("Final list:", nums)






# 
# #  USER INPUTS
# 
# # 1
# 
# print("hello",input("name:"),input("surname:"))"""
#
# # 2
# """a=int(input("enter the 1st number:"))
# b=int(input("enter the 2nd number:"))
# total=a+b
# print(total)"""
#
# # 3
# # """a=int(input("enter the 1st number:"))
# # b=int(input("enter the 2nd number:"))
# # c=int(input("enter the 3rd number:"))
# # sum=a+b
# # ans=(sum*c)
# # print("the answer is:",ans)"""
#
# # 4
# """total_pizza_slices=int(input("total slices of pizza:"))
# eaten_slices=int(input("eaten slices:"))
# remaing_slices=(total_pizza_slices-eaten_slices)
# print("remaining slices are:",remaing_slices)"""
#
# # 5
# """name= input("enter your name:")
# age=int(input("enter your age:"))
# nxt=(age+1)
# print(name,"for next birthday your age will be:",nxt)"""
#
# # 6
# """total_bill=int(input("total dinner bill:"))
# dinners=int(input("no of dinners:"))
# split=(total_bill/dinners)
# print("for each person  the bill will be:",split)"""



# If statements

# 1
# num1=int(input("enter 1st number:"))
# num2=int(input("enter 2nd number:"))
# if num1>num2:
#     print(num2,num1)
# else:
#     print(num1,num2)

# 2
# num =int(input("enter the number under 20:"))
# if num>=20:
#     print("number is higher or equal to '20'")
# else:
#     print("okay , Thank you!!")

# 3
# num=int(input("enter a number between 10 and 20:"))
# if num in range(10,20):
#     print("Thank You!")
# else:
#     print("incorrect Answer!!")

# 4
# fav_color=(input("enter your fav color:"))
# if fav_color.lower()=="red":
#     print("i like red too")
# else:
#     print(f"i dont like {fav_color}")

# 5
# rain=str(input("Is it raining ?"))
# if rain.lower()=="yes":
#     wind = str(input("is it windy?"))
#     if wind.lower()=="yes":
#         print("it is too windy for an umberella")
#     else:
#         print("take an uberella")
# else:
#     print("have nice day")

# 6
# age=int(input("enter your age:"))
# if age >= 18:print("you can vote!")
# elif age==17:print("you can learn driving")
# elif age==16:print("you can buy lottry ticket")
# elif age<16:print("you can go to tickor training")

# 7
# num=int(input("enter 1,2 or 3 : "))
# if num == 1:
#     print("Thank you")
# elif num==2:
#     print("well done")
# elif num==3:
#     print("correct")
# else:
#     print("ERROR")

# strigs


# 1
# name=str(input("enter your name:"))
# length=len(name)
# print("length of name:",length)

# 2
# fname=str(input("enter your fname:"))
# sname=str(input("enter your sname:"))
# fullname=( fname + sname)
# print(f"{fname} {sname}","\ntotal length is:",len(fullname))

# 3
# fname=str(input("enter your fname in lower case:"))
# sname=str(input("enter your sname in lower case:"))
# s=fname.title()
# p=sname.title()
# print(f"{s} {p}")

# 4
# ryme=str(input("enter tha rhyme: "))
# print("length of rhyme:",len(ryme))
# u=int(input("enter the num1:"))
# p=int(input("enter the num2:"))
# q=ryme[u:p]
# print(q)

# 5
# word=str(input("enter the word:"))
# r=word.upper()
# print(r)

# 6
# fname=str(input("enter fname:"))
# if len(fname)<5:
#     sname=str(input("enter sname"))
#     print(fname.upper()+sname.upper())
# else:
#     print(fname.lower())

#for loop

# 1
# name=input("enter the name:")
# number=int(input("enter the number:"))
# for i in range(number):
#     print(name)

# 3
# name=input("enter the name:")
# number=int(input("enter the number:"))
# for i in range(number):
#     for i in name:
#         print(i)
#     print()

# 4
# num=int(input("enter the number between 1 and 12 :"))
# if 1<= num <= 12:
#     print(f"times table for {num}: ")
#     for i in range(1,13):
#         print(f"{num} x {i} = {num*i}")

# 5
# name=(input("enter the name:"))
# num=int(input("enter the umber"))
# if num <= 10:
#     for i in range(num):
#         print(name)
# else:
#     e=("too high")
#     for i in range(3):
#         print(e)

# 6
# total = 0
# for i in range(5):
#     inpt=int(input(f"enter the number {i+1} : "))
#     sn=input("do you want to inclue this number? (yes/no):").strip().lower()
#     if sn== "yes":
#         total+=inpt
#     print(f"The total of the included numbers is: {total}")

# 8
# num=int(input("how many members do you intive to the party:"))
# if num < 10:
#     for i in range(num):
#         guest=input("enter the  guest name:")
#         print(f"{guest} has invited to the party")
# else:
#     print("too many guests!!")

#  While loop

# 1
# total = 0
# while total <= 50:
#     number = int(input("Enter a number: "))
#     total += number
#     print(f"The total is {total}")
# print("The total is over 50. Stopping the loop.")

# 2
# while True:
#     number = int(input("Enter a number: "))
#     if number > 5:
#         print(f"The last number you entered was a {number}")
#         break

# 3
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# total = number1 + number2
# while True:
#     add = input("Do you want to add another number? (y/n): ").strip().lower()
#     if add == "y":
#         another_number = int(input("Enter another number: "))
#         total += another_number
#     else:
#         break
# print(f"The total is {total}")

# 4
# count = 0
# while True:
#     name = input("Enter the name of someone you want to invite to the party: ")
#     print(f"{name} has now been invited.")
#     count += 1
#     invite_more = input("Do you want to invite someone else? (yes/no): ").strip().lower()
#     if invite_more != "yes":
#         break
# print(f"You have {count} people coming to the party.")

# 5
# compnum = 50
# count = 0
# while True:
#     guess = int(input("Enter a number: "))
#     count += 1
#     if guess < compnum:
#         print("Your guess is too low. Try again!")
#     elif guess > compnum:
#         print("Your guess is too high. Try again!")
#     else:
#         print(f"Well done, you took {count} attempts!")

# 6
# while True:
#     number = int(input("Enter a number between 10 and 20: "))
#     if number < 10:
#         print("Too low. Try again!")
#     elif number > 20:
#         print("Too high. Try again!")
#     else:
#         print("Thank you!")
#         break

# functions

import random
def display_menu():
    print("Menu:")
    print("1). Addition")
    print("2). Subtraction")
    choice = input("Enter 1 or 2: ")
    return choice
def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    correct_answer = num1 + num2
    user_answer = int(input(f"What is {num1} + {num2}? "))
    return user_answer, correct_answer
def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    correct_answer = num1 - num2
    user_answer = int(input(f"What is {num1} - {num2}? "))
    return user_answer, correct_answer
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect, the answer is {correct_answer}.")
choice = display_menu()
if choice == '1':
    user_answer, correct_answer = addition()
    check_answer(user_answer, correct_answer)
elif choice == '2':
    user_answer, correct_answer = subtraction()
    check_answer(user_answer, correct_answer)
else:
    print("Invalid choice. Please select 1 or 2.")
