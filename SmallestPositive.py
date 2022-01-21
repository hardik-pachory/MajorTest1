n = int(input("Number of elements : "))
li = []
num = -1
for i in range(n):
    t = int(input())
    li.append(t)
for i in range(1, n+1):
    if i not in li:
        num = i
        break
if num <= n and num != -1:
    print("Output : ", num)
else:
    print("Output :", n+1)
