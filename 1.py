# By directly taking the input
# a = "America"
# b = "Japan"
# print("The concatenated string is", a[0] + b[0] + a[3] + b[2] +a[-1] + b[-1])


a = input("enter your first string:\n")
b = input("enter your next string:\n")

def mid(c):
    length = len(c)
    middle = length // 2
    # print("the middle character is\n")
    print(c[middle])

c = a
d = b



print("\nthe concatenated string of first and last characters is\t")
# print(a[0]+b[0], end = "")
# mid(c)
# print(end = "")
# mid(d)
# print(end = "")
# print(a[-1]+b[-1])
c = a
d = b
print(a[0]+b[0], mid(c), mid(d), a[-1]+b[-1])

#I tried to conctenated the characters but unable to add the middle characters




