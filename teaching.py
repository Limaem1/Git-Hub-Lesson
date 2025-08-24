number1 = 1
number2 = 5 
x = 0 

def add(number1,number2):
    return number1 + number2


def multiply(number1,number2):
    x = 0
    for i in range(number1):
        x = add(x,number2)
    return x


result1 = add(number1,number2)
result2 = multiply(number1,number2)
print(result1,result2)