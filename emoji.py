n = int(input())
if (n<=3):
    print("Not Composite")
else:
    for i in range(4, n):
        if n % i == 0:
            print("Number is composite")
        else:
            print("Number is prime")