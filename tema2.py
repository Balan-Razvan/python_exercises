# practice

# numar pozitiv, negativ sau 0
a = int(input('introdu numarul '))
if (a > 0):
    print('pozitiv')
elif (a < 0):
    print('negativ')
else:
    print('zero')

# unmarul par/impar
if(a % 2 == 0):
    print('par')
else:
    print('impar')

# litera vocala sau consoana
vocale = 'aeiou'
litera = input('introdu o litera ').lower()
if len(litera) == 1 and litera.isalpha():
    if litera in vocale:
        print('vocala')
    else:
        print('consoana')
else:
    print('litera invalida')

# varsta
varsta = int(input('introdu varsta '))
if(varsta > 65 or varsta < 18):
    print('reducere')
else:
    print('nu are parte de reducere')


# an bisect

an = int(input('introduceti anul '))
if(an % 4 == 0):
    print('an bisect')
else:
    print('nu este an bisect')


####################
# homework 1

password = input('introduceti parola ')
if(len(password) > 7 and any(i.isupper() for i in password) and any(i.isdigit() for i in password)):
    print('valid password')
else: 
    print('password too weak')



# homework 2
vocale = "aeiou"
word = input('introdu un cuvant')
cnt = 0

for i in word:
    if i in vocale:
        cnt += 1
        print(i)
