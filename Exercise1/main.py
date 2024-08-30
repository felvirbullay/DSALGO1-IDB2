#Exer1 prices
wii=100
money=int(input("How much money can you spend?"))
number=int(money / wii)
needed=int(wii - money)
more=abs(money - wii)-wii

if money >= wii:
    print("The amount of units you can buy is ",number)
    print("You will need ",more,"to get ",number+1)
else :
    print("You will need ",needed)
print("Dont mind the negative in your balance")
print()
#Exer2 factorial
sum=1
numbers=int(input("Enter a number"))
for x in range(1,numbers+1):
    sum=sum * x
print(sum," is the factorial of the numbers 1-",numbers)
#Exer3 factor
print()
factorList=[]#array
x=int(input("Enter a number: "))
for a in range (1,x+1):
    if x%a ==0:
        factorList.append(a)
print("The factors of ",x," are",factorList)
