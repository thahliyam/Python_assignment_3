# Name your file: MonthNames.py
# 1 Write a program that reads an integer value between 1 and 12
# from the user and prints output the corresponding month of the year.

x=int(input('Enter a month number (1- 12): '))
if x==1:
 print('Month',x,'is January')
elif x==2:
 print('Month', x, 'is February')
elif x==3:
 print('Month', x, 'is March')
elif x==4:
 print('Month', x, 'is April')
elif x==5:
 print('Month', x, 'is May')
elif x == 6:
 print('Month', x, 'is June')
elif x == 7:
 print('Month', x, 'is July')
elif x == 8:
 print('Month', x, 'is August')
elif x == 9:
 print('Month', x, 'is September')
elif x == 10:
 print('Month', x, 'is October')
elif x == 11:
 print('Month', x, 'is November')
elif x == 12:
 print('Month', x, 'is December')
else:
 print('Wrong month number')

# 2 A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than
# 16 years old, and for a third of the price for people who are 60
# years old or more.

Age=int(input('Enter your age: '))
if Age<16:
 print('Your ticket costs ','\u00A33.00')
elif Age>=60:
 print('Your ticket costs ','\u00A32.00')
else:
 print('Your ticket costs ','\u00A36.00')
