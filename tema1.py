import operator
# a = 6
# b = 3

# # operatori logici
# print(a > 1 and b < 3)
# print(a > 1 or b < 3)
# print(not (a > 3))



# # bitwise
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)

# print(a << 1)
# print(a >> 1)

a = int(input('first number '))
b = int(input('second number '))
# print(a > b)

operations = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv
}
operation = input('enter operation ')

print(operations[operation](a, b))