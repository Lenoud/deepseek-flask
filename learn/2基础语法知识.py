import sys

print("%d" % 30)
print("%o" % 30)
print("%x" % 30)
print("\r \n \t \\ ")
sz1 = 1
zf1 = "string"
list1 = [1, 2]
dict1 = {"a": 1}
yz1 = (1, 2, 3)

# sys.exit()
shuzi = "123"
print(type(list(shuzi)))
print(list(shuzi))

print("{a:} {b:} {a:}".format(a=sz1, b=zf1))

print(shuzi.isdigit(), zf1.isdigit())
#
# for i in range(10, -10, -2):
#     print(i)

for i in range(100, 1000):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    sum = a ** 3 + b ** 3 + c ** 3
    if i == sum:
        print(i, "是水仙花数")

bl=0
while bl < 10000000000:
    bl+=1
    print(bl)
    if bl== 100000:
        break