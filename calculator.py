#take an input

a = input("Enter a number")
b = input("Enter a operator ")
c = input("Enter num2")

# convert input into integer

a = int(a)
c = int(c)

#checking b

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

#Thankyou

print('Thankyou for using the calculator')
