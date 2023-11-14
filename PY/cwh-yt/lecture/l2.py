# x=int(input("num1: "))
# y=int(input("num2: "))
# print(x+y)









# x=int(input("enter a num: " ))
# print(x%2)









# x=(input("enter:"))
# check.type=x


# x=(input("enter:"))
# check_type=type(x)
# print(type(x))

# x = input("Enter something: ")
# check_type = type(x)
# print("Input:", x)
# print("Type:", check_type)










# a=34
# b=80
# print(a<b)









# a=int(input("enter: "))
# b=int(input("enter: "))
# print("aver. is:",(a+b)/2)





# a=int(input("enter: "))
# b=int(input("enter: "))
# print("sq. is:",a*b)







# lecture:3




# x=input("enter the fucking name :")
# print("Good morning,",x)




# x=input("enter the fucking name :")
# y=input("enter the fucking date :")
# letter= f" Dear {x}, and you are selcted ! date:{y}"
# print(letter)

# letter = '''Dear <|NAME|>,
# You are selected!
# Date: <|DATE|>'''
# name = input ("Enter Your Name \n")
# date = input ("Enter Date \n")
# letter = letter.replace("<|NAME|>",name)
# letter = letter.replace("<|DATE|>",date)
# print(letter)







# x = str(input())
# if "  " in x:
#     print("Double space detected.")
# else:
#     print("No double space found.")



# f1=input("enter your fruitname:1:")
# f2=input("enter your fruitname:2:")
# f3=input("enter your fruitname:3:")
# f4=input("enter your fruitname:4:")
# f5=input("enter your fruitname:5:")
# list1=[f1,f2,f3,f4,f5]
# print(list1)


# a= (0, 10, 0, 13,0)
# count = len(a)
# print("The number of elements in the tuple is:", count)

# a = (0, 10, 0, 13, 0)
# count = a.count(0)
# print("The number of elements with zero in the tuple is:", count)


# chapter :5/


# mydict = { "go": "jana", "eat": "khao" }
# print("options are",mydict.keys())
# a=input("enter your word\n")
# print("the meaning of your word is:",mydict[a])


# def greet():
#     name=input()
#     print("good morning "+ name)
# greet()


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))



# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# def find_largest():
#     if a >= b and a >= c:
#         print("The largest number is:", a)
#     elif b >= a and b >= c:
#         print("The largest number is:", b)
#     else:
#         print("The largest number is:", c)


# a = int(input("Enter the celcius's value which you want to convert farenheit: "))
# def w():
#     x=(a* 9/5) + 32
#     print(x)
# w()

# print("Hello",end=' ')
# print("How",end=' ')
# print("are",end=' ')
# print("you?",end=' ')

# a=int(input("tell me the number :"))
# def w():
#     for x in range(0,a)
#     x=sum till a
#     w()




# def sum_of_numbers(a):
#     if a == 0:
#         return 0
#     else:
#         return (a) + sum_of_numbers(a - 1)

# a = int(input("Enter a number: "))
# result = sum_of_numbers(a)
# print(result)

# You cannot write return sum_of_numbers(a) + sum_of_numbers(a - 1) because it would create an infinite loop or recursion.When you call sum_of_numbers(a), it will keep calling itself with the same a value and the next smaller value (a - 1) over and over again. This will never reach the base case (a value of 0), and the recursion will continue infinitely, causing your program to crash or run indefinitely.Recursion should have a base case that stops the recursive calls, which is why you use if a == 0: to halt the recursion in the corrected code.

# n=6
# for i in range(n):
#     print("*" * (n-i))

def a(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
v = "   Ansh          is a good     " 
n=a(v,"Ansh")
print(n)
