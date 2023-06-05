s = str(input())
str = []

for z in s:
    str.append(z)
#isalnum
#isalpha
#isdigit
#islower
#isupper

arr = []
a = False
d = False
l = False
s = False


for i in str:
    a = a + i.isalnum()
    d = i.isalpha()
    l = i.isdigit()
    s = i.isupper()
arr.append(a)
arr.append(d)
arr.append(l)
arr.append(s)

for x in arr:
    print(arr)


