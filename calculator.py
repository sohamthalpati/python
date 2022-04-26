a = input("Enter a number")
b = input("Enter a operator ")
c = input("Enter num2")

a = int(a)
c = int(c)

if b == '/':
    print( a / c)

elif b == '*':
    print(a * c)

elif b == '+':
    print(a + c)

elif b == '-':
    print(a - c)

else:
    print("Invalid Operation")

print('Thankyou for using the calculator')
