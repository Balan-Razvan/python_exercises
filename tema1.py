import operator
a = int(input('first number '))
b = int(input('second number '))


# operatori logici
print("and", a > 1 and b < 3)
print("or", a > 1 or b < 3)
print("not", not(a > 3))

# bitwise
print('&', a & b) # AND
print('|', a | b) # OR
print('^', a ^ b) # XOR
print(~a)         # NOT
print(a << 1)     # left shift
print(a >> 1)     # right shift

# operatori comparatie
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# operatori de assignment
a = 5
a += 1
a -= 2
a *= 2
a /= 2
a %= 3
a //= 2
a **= 2
a &= 3
a |= 3
a ^= 3
a <<= 3
a >>= 3

# special operators
print('a' in 'apple')
print('a' not in 'apple')
print ('a' is 'a')



# calculator
operations = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv
}
operation = input('enter operation ')

print(operations[operation](a, b))