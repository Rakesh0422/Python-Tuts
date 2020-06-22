#GCD by Loops
def computeGCD(x, y):

    if x>y:
        small=y
    else:
        small=x
    for i in range(1, small+1):
        if((x%i==0) and (y%i==0)):
            gcd=i
    return gcd

print("The gcd of 6 and 12 is : ", end="")
print(computeGCD(12,6))


#GCD using Euclidean Algorithm
def computeGCDE(x, y):

	while(y):
		x, y = y, x%y

	return x

print("The gcd using Euclidean Algo of 6 and 12 is : ", end="")
print(computeGCDE(12,6))