#1)
#Addition(+)
# num1=23
# num2=35
# result=num1+num2
# print(result)

#Subtraction(-)
# num1=29
# num2=22
# result=num1-num2
# print(result)

#Multiplication(*)
# num1=10
# num2=24
# result=num1*num2
# print(result)

#Division(/)
# num1=200
# num2=10
# result=num1/num2
# print(result)

#Modulus(%)
# num1=30
# num2=20
# result=num1%num2
# print(result)

#Exponentiation(**)
# num1=2
# num2=3
# result=num1**num2
# print(result)

#Floor Division(//)
# num1=8
# num2=6
# result=num1//num2
# print(result)


#2)
#Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw,print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.

# balance = 1000
# try:
#     withdrawal_amount = float(input("Enter the amount to withdraw: Rs."))
#     if withdrawal_amount > balance:
#         print("Insufficient balance. Transaction failed.")
#     else:
#         balance -= withdrawal_amount
#         print("Withdrawal successful. Remaining balance: Rs.{}".format(balance))
#         if balance < 500:
#             print("Alert: Your account balance is Rs.{}. Please keep your account balance above Rs.500 to avoid unwanted charges.".format(balance))
# except ValueError:
#     print("Invalid input. Please enter a valid numerical amount.")


#3)
#Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same
# num1=float(input("Enter the first number:"))
# num2=float(input("Enter the second number:"))
# num3=float(input("Enter the third number:"))
# if(num1==num2==num3):
#     print("Equal")
# elif(num1>num2) and (num1>num3):
#     print("num1 is greater")
# elif(num2>num1) and (num2>num3):
#     print("num2 is greater")
# else:
#     print("num3 is greater")


#4)
#Python program to check the number taken as an input is even or odd,print invalid input if user enters anything other than integers
# Input=input("Enter the number:")
# if Input.isdigit():
#     num=int(Input)
#     if(num%2==0):
#         print("The number is even")
#     else:
#         print("The number is odd")
# else:
#     print("Invalid input")


#5)
"""Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above,
B+ if 70 or above and so on... 
print failed if the score is below 50, if score > 100 print invalid"""

# score=float(input("Enter the score:"))
# if(score>100):
#     print("Invalid")
# elif(score>=90):
#     print("Grade:A+")
# elif(score>=80):
#     print("Grade:A")
# elif(score>=70):
#     print("Grade:B+")
# elif(score>=60):
#     print("Grade:B")
# elif(score>=50):
#     print("Grade:C+")
# else:
#     print("Failed")

#6)
#Python program to print all even/odd numbers in the range given by user
# def print_even_odd_numbers(start, end, even=True):
#     numbers = [num for num in range(start, end + 1) if (num % 2 == 0) == even]
#     label = "even" if even else "odd"
    
#     if numbers:
#         print("All {} numbers between {} and {}: {}".format(label, start, end, numbers))
#     else:
#         print("No {} numbers in the given range.".format(label))

# try:
#     start = int(input("Enter the starting number: "))
#     end = int(input("Enter the ending number: "))
    
#     choice = input("Do you want to print even or odd numbers? Enter 'even' or 'odd': ").lower()
    
#     if choice == 'even':
#         print_even_odd_numbers(start, end, even=True)
#     elif choice == 'odd':
#         print_even_odd_numbers(start, end, even=False)
#     else:
#         print("Invalid choice. Please enter 'even' or 'odd'.")
# except ValueError:
#     print("Invalid input. Please enter valid numerical values.")



#7)
"""Python program to print the multiplication table of any number 
(number should be taken as input and user decides the end limit of the table)"""

# num=int(input("Enter the number:"))
# end_limit=int(input("Enter the endlimit"))
# for i in range(1,end_limit):
#     num1=i*num
#     print(f"{i}*{num}=={num1}")


#8)
#Find the factorial of a number taken as input using for loop
# num=int(input("Enter the number:"))
# if(num<0):
#     print("Factorial is not defined for negative numbers")
# elif(num==0):
#     print(1)
# else:
#     factorial=1
#     for i in range(1, num + 1):
#         factorial*= i
#     print(factorial)


#9)
#Find the factorial of a number taken as input using while loop
# num=int(input("Enter the number:"))
# factorial=1
# while(num>=1):
#     factorial*=num
#     num-=1
# print(factorial)


#10)
#Find the sum of all even numbers between the range given by user
# range1=int(input("Enter the starting range:"))
# range2=int(input("Enter the end range:"))
# if range1>range2:
#     print("Invalid")
# else:
#     evenSum=0
#     for num in range(range1,range2+1):
#         if num%2==0:
#             evenSum+=num
#     print(evenSum)


#11)
#Find the sum of all odd numbers between the range given by user using while loop
# range1=int(input("Enter the starting range:"))
# range2=int(input("Enter the ending range:"))
# if range1>range2:
#     print("Invalid")
# else:
#     oddSum=0
#     while(range1<=range2):
#         if range1%2!=0:
#             oddSum+=range1
#         range1+=1
#     print(oddSum)


#12)
#Print first 10 fibonacci numbers using 'for' and 'while' loops

#a)
        #     *
        #    * *
        #   * * *
        #  * * * *


# def print_pyramid(rows):
#     for i in range(1, rows + 1):
#         for j in range(rows - i):
#             print("", end=" ")

#         for k in range(i):
#             print("*", end=" ")
#         print()
# num_rows = 4 
# print_pyramid(num_rows)

#b)
#         o
#         1 2
#         3 4 5
#         6 7 8 9
# rows = 4
# counter = 0
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(counter, end="")
#         counter += 1
#     print()

#c)
# 	    o
# 		1 1
# 		2 2 2
# 		3 3 3 3

# rows = 4
# for i in range(rows):
#     for j in range(i + 1):
#         print(i, end="")
#     print()
#d)
        # *
		# * *
		# * * *
		# * * * *

# for i in range(1,6):
#     print('* '*i)