# Hello World
print('Remember the Python')
# Integer - Float
print(56 / 7)  # equals 8
print(54.25 / 7.1)  # 7.64
# Variables
a = 10
b = 3
c = a + b
print(c)
a, b = b, a  # relocate
print(a, b)
print(a)
i = 5
i += 1
# Mathematics Operators
print(345 // 7)  # integer division
print(13 % 4)  # remainder
print(4 ** 3)  # exponent
print(4 ** 0.5)  # sqrt
#  Strings
print('Ilyurek Kilic')
x = "Gender"
print(x[3])  # returns d
print(x[-3])  # returns d
print(x[0:3])  # returns Gen
print(x[::-1])  # reverse
# Properties of Strings
print(len(x))  # length
y = "Man"
print(x + y)
# str does not support item assignment

# Type conversion

# integer to float
a = 43
a = float(a)
print(a)

# float to integer
b = 4.7
b = int(b)
print(b)

# integer to string
a = 24
a = str(a)
print(a)

# Print and Format
print("ilyurek")
print("İlyurek","Kılıç",2429157)

# /n and /t
print("İlyurek\nKılıç")
print("İlyurek\tKılıç")

# parameters of print function
print("İlyurek","Kılıç",2429157,sep="\n")
print("06","04","1997",sep="/")
# *
print(*"Python",sep="/")
print(*"TBMM",sep=".")
# format function
a = 3
b = 4
print("{} + {} equals {}".format(a,b,a+b))
