#Write a program to find whether a given username contains less than 10
#characters or not.

username = input("Enter user name : ")

if(len(username)<10):
    print("Your username contains less than 10 characters")

else:
     print("Your username contains more than 10 characters")