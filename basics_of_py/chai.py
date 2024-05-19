import math
import time 


# from hello_chai import chai

# chai("ginger tea")

# this is comment
# chai_list_string = ["hello","boob","you", "all", "are", "dumbass"]

# for new in chai_list_string:
#     if(new=="booby"):
#         print("i have boob")
#     elif(new=="all"):
#         print("we have all")



    
    
# def squre(num):
#     print(num**2)
# squre(4)


# age = int(input())
# if (age<25):
#     print("child")
# elif (age<40):
#     print("edult")
# elif(age>40):
#     print("old")

# age = int(input())
# day= input()
# price = 8 if age<=18 else 18

# if age<=18:
#     price = 8
# else:
#     price = 18
# if day=='wednesday':
    # price -= 2
# print(price)

#PASS CHECKER 
# user = input("enter your pass : \n")

# if len(user)<=6:
#     print("easy")
# elif len(user)<=10:
#     print("good")
# else:
#     print("strong")

#LEAP YEAR

# year = int(input("enter year : \n"))

# if (year%4==0) or (year%4 == 0 and year%100 != 0):
#     print("leap")
# else:
#     print("not leap year")      

# number = []
# for new in range(6):
#     num = int(input("enter the num : \n"))
#     number.append(num)

# count = 0

# for i in number:
#     if i<0:
#      count+=1

# print("all numbers we have : " , number)
# print("count of negative num : " ,  count)


# SUM OF EVEN NUMBERS

# number = []
# for new in range(6):
#     num = int(input("enter the num : \n"))
#     number.append(num)
# sum = 0
# for i in number:
#     if i%2==0:
#         sum+=i
# print("sum of even numbers : " , sum)

# multiply to 10 and skip 5th number

# num = int(input("enter the number : \n"))
# 
# for i in range(1,11):
    # if i == 5:
        # continue
    # else:
        # print(num , " x ", i , " = " , num*i)


# REVERSE STRING
# name = input("enter the name : \n")
# 
# rev_name = ""
# 
# for i in name:
    # rev_name = i + rev_name 
    # 
# print(rev_name)

#FIRST NON-REPEATED CHAR

# name = input()

# for i in name:
#     if name.count(i) == 1:
#         print(i)
#         break    

#Find fac using loop

# num = int(input("give a number : \n"))
# factorial = 1

# while num>0:
#     factorial *=num
#     num -= 1
# print(factorial)

#GIVE THE INPUT UNTIL USER FEED NUMBER BTW 0 TO 10
# while True:
#     num = int(input("give the number : \n"))
#     if num<=10:
#         print("thanks :")
#         break
#     else:
#         print("invalid num : \n")

#FIND PRIME NUMBER

# user_in = int(input("give a number : \n"))
# is_prime = True

# if user_in>1:
#     for i in range(2,user_in):
#         if user_in%i == 0:
#             is_prime = False
#             break
# print("is prime :",is_prime)

#FIND THE DUPLICATE IN LIST

#INCRAESE THE WAIT TIME AFTER EACH ATTEMPT

#BEHIND THE SCENE OF PYTHON IN LOOP

#FUNCTION
# def square(num):
#     result = num **2
#     return result


# squre_num = square(10)
# print(squre_num)

# def mul_pera(num1 , num2):
    #   return num1*num2
# print(mul_pera("tsa","toom"))                  
# print(mul_pera('t',3))  # PYTHON FOLLOWS POLYMORPHISM MEANS ONE OPERATOR DO DIFFERENT WORK
  
#FUNCTION THAT RETURN MULTIPLE VALUE
# def muiti_val(radius = 3):
#       area = math.floor(math.pi*(radius**2))
#       circumfar = math.floor((2*math.pi)*radius) 
#       return area , circumfar


# a = muiti_val(7)
# type_of = type(a)
# print(type_of)
# print(a )

#TAKING UNLIMITED VALUE
#TAKING UNLIMITED KEY AND VALUE

#YIELD

#RECURSIVE FUNCTION

#SCOPES , CLOSERS

#OOPs
#CLASS AND OBJECTS

class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model



my_car = Car("toyota" , "xor")
print(my_car.brand)
print(my_car.model)



 





 



        
            
        
             

