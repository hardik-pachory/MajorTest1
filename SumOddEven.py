n = int(input())
sumOdd = 0
sumEven = 0
while(n != 0):
    r = n % 10
    if r % 2 == 0:
        sumEven = sumEven+r
    else:
        sumOdd = sumOdd+r
    n = n//10
print(sumEven, sumOdd)
