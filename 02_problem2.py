# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))

# check for total parcentage
Total_parcentage = (100*(marks1 + marks2 + marks3))/300

if(Total_parcentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Your pass: ",Total_parcentage)

else:
    print("You failed, try again next year : ",Total_parcentage)
