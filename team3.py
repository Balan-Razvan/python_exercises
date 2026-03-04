# curs functii

# practice

def is_even(n = 0):
    return n % 2 == 0

def maxim(a = 0, b = 0):
    return a if a > b else b

def vowel_count(s = ""):
    vowels = "aeiou"
    cnt = 0
    for i in s:
        if(i in vowels):
            cnt += 1
    return cnt

def list_sum(l = []):
    suma = 0
    for i in l:
        suma += i
    return suma

def number_check(s =  "", n = 0):
    return (str(n) in s)

# homework_1

def analyze_word(word = "python"):
    return len(word), vowel_count(word), word.upper()

# homework_2
def minim_list(l = []):
    minim = l[0]
    for i in l:
        if i < minim:
            minim = i
    return minim

def maxim_list(l = []):
    maxim = l[0]
    for i in l:
        if i > maxim:
            maxim = i
    return maxim

def average(l = []):
    return list_sum(l) / len(l)

def odd_numbers_cnt(l = []):
    cnt = 0
    for i in l:
        if not(is_even(i)):
            cnt += 1
    return cnt

def number_stats(numbers = []):
    return minim_list(numbers), maxim_list(numbers), average(numbers), odd_numbers_cnt(numbers)
# print(number_stats([1, 2, 3, 4, 5, 6]))



# curs data structures 2

# practice

def eliminare_dupes(l = []):
    return set(l)

def maxim_varsta(l = []):
    maxim = l[0][1]
    nume = l[0][0]
    for i in l:
        if i[1] > maxim:
            maxim = i[1]
            nume = i[0]
    return nume
# print(maxim_varsta([("ion", 23), ("vasile", 55), ("ioana", 54)]))

def nr_frecvent(l = ()):
    dictionar = {}
    for i in l:
        if i not in dictionar:
            dictionar[i] = 1
        else:
            dictionar[i] += 1
    aparitii = 0
    nr_maxim = 0
    for key, value in dictionar.items():
        if(value > aparitii):
            nr_maxim = key
            aparitii = value
    return nr_maxim
# print(nr_frecvent((1, 2, 2, 2, 3, 4)))

def cuvant_frecvent(s = ""):
    lista_cuvinte = s.split(' ')
    dictionar = {}
    for cuvant in lista_cuvinte:
        if cuvant not in dictionar:
            dictionar[cuvant] = 1
        else:
            dictionar[cuvant] += 1
    
    aparitii = 0
    cuvant = ""
    for key, value in dictionar.items():
        if(value > aparitii):
            cuvant = key
            aparitii = value
    return cuvant
#print(cuvant_frecvent("apple banana banana banana apple orange banana apple"))

def switch_chei_valori(dictionar = {}):
    dictionar2 = {}
    for key, value in dictionar.items():
        dictionar2[value] = key
    return dictionar2
# print(switch_chei_valori({"test": 3, "test2": 4}))



# homework 1

list1 = [(1, "apple"), (3, "orange"), (5, "banana")]
list2 = [(2, "grape"), (4, "kiwi"), (6, "melon")]

def homework(list1, list2):
    lista = list1 + list2
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][0] > lista[j][0]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
# print(homework(list1, list2))


# homework 2

people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"}
}

def oldest(dictionar = {}):
    oldest = ""
    varsta_maxim = 0
    for key, value in dictionar.items():
        if(value["age"] > varsta_maxim):
            varsta_maxim = value["age"]
            oldest = key
    return oldest, varsta_maxim

def list_new_york(dictionar = {}):
    lista = []
    for key, value in dictionar.items():
        if value["city"] == "New York":
            lista.append(key)
    return lista

# print(list_new_york(people))