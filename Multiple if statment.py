a = int(input("Enter your age :"))

#if statement 1
if(a%2==0):
    print("a is even")
# end statement 1


#if statement 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering invalid age.")

elif(a==0):
    print("You are entering 0 is not valid age")

else:
    print("You are below the age of consent")
# end statement 2


print("End of program.")
