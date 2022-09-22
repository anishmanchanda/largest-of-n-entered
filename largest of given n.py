#largest out of given n

n = int(input("enter number of numbers"))
max=-9999
for i in range(1,n+1):
    num=int(input("enter a number"))
    if num>=max:
        max=num

print("largest out of entered numbers is",max)

