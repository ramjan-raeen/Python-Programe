num=int(input("Enter a number:"))
fact=1
for num in range(1,num+1):
    fact=fact*num
print("factorial of {} is: {}".format(num,fact))
