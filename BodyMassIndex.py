#  Name your file: BodyMassIndex.py
#  3 Write a program to calculate your BMI and give weight status.
# Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.
# The metric BMI formula accepts weight in kilograms and height in meters:
# BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI range - kg/m2
# Category Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese
# An example run of the program (numbers in bold are typed in by the user)
# Enter your weight in (kg): 75 Enter your height in (m): 1.70 Your BMI is: 25.95
# You are in the “overweight” range.from math import factorial

# a=float(input('Enter your weight in (kg): '))
# b=float(input('Enter your height in (m): '))
# BMI=a/(b*b)
# print('Your BMI is: ',BMI)
# if BMI<18.5:
#     print('You are in "underweight"')
# elif 18.5<= BMI <=24.9:
#     print('You are in "normalweight"')
# elif 25<= BMI <=29.9:
#     print('You are in "over weight"')
# else:
#     print('You are in "Above obese"')
#
# # 4 Write a Python program to receive 3 numbers from the user and print
# # the greatest among them.
# a=float(input('Enter first number : '))
# b=float(input('Enter second number : '))
# c=float(input('Enter third number : '))
# print('The numbers are :',a ,b ,c)
# if b>a and b>c:
#     print('The greatest number is ',b)
# elif a>b and a>c:
#     print('The greatest number is ',a)
# else:
#     print('The greatest number is ',c)
#
# #  5 Find the factorial of a given number using loops(note the number is received from the user)
# num=int(input('Enter a number: '))
# factorial=1
# if num==0 or num==1:
#     print('factorial is 1')
# elif num<0:
#     print('Enter a positive number')
# else:
#     for i in range(1,num+1):
#      factorial=factorial*i
#     print('Factorial of the number is ',factorial)

# 6 Reverse a number using while loop
# x=int(input('Enter a number'))
# copy=x
# rev=0
# while x>0:
#     y=x%10
#     rev=rev*10+y
#     x=x//10
# print('Reverse of the number',copy,'is',rev)
#
# # 7 Finding the multiples of a number using loop
# x=int(input('Enter a number: '))
# print('Multiples of the number',x,'are: ')
# for i in range(1,11):
#     print(i*x,end=" ")
# print()

# 8 Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program :hello there hello there :finished finished :done Done

# while True:
#     x=input('Enter a value or(done to exit)')
#     print(x)
#     if x.lower()=='done':
#       break


# 9 Write a program that prints the numbers from 1 to 10. But for multiples
# of three print "Fizz" instead of the number and for the multiple of five print
# "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
for i in range(1,11):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)

# 10 Write a program to print the following pattern:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(5,0,-1):
  for j in range(i,0,-1):
    print(j,end=" ")
  print()


