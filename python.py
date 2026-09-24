# #count the number of digits in anumber
# number = int(input("Enter number :"))

# count = 0

# while number > 0:
#     number = number // 10
#     count = count + 1
 
#     print("number of digits:", count)

 #sum of digits in a number

# number = int(input("Enter number:"))

# total = 0

# while number > 0:
#     digit = number % 10
#     total = total + digit
#     number = number // 10

#     print("sum of digits:", total)

#  #reverse a number
# number = int(input("enter number :"))

# reverse = 0

# while number > 0:
#         digit = number % 10
#         number = number // 10
#         reverse = reverse * 10 + digit

# print("reverse :", reverse)


# # check if a number is prime
# number = int(input("enter number :"))

# count = 0

# for i in range(1, number + 1):
#     if number % i ==0:
#         count = count + 1

#     if count == 2:
#         print("prime number")

#     else:
#         print("not a prime number") 

# #find the largest number among 5 numbers entered by the users.
#  largest = None  
# for i in range(5):
#     number =int(input("enter a number"))
#     if largest is none or number> largest:
#         largest = largest
#         print("largest:", smallest)

# #count the numbers of positive and negative and zero number enterd by the user.
# positive = 0
# negative = 0
# user = 0

# for i in range (10):

#     number = int(input("enter a number:"))

#     if(number > 0):
#         positive = positive + 1
#     elif(number < 0):
#         negative = negative + 1
# else:
#     zero = zero + 1

# print("positive:", positive)
# print("negative:",negative)
# print("zero:",zero)    

#password check with limited attempts
correct_password = "python123"

for attempt in range(1 , 4):

    password = input("enter password")

    if password == correct_password:
        print("login successful")
        break
    print("wrong password")

else:
    print("account locked")


