def eliminare_dupes(l= []):
    return set(l)

def maxim_varsta(l= []) -> str:
    maxim = l[0][1]
    nume = l[0][0]
    for i in l:
        if i[1] > maxim:
            maxim = i[1]
            nume = i[0]
    return nume
# print(maxim_varsta([("ion", 23), ("vasile", 55), ("ioana", 54)]))

def nr_frecvent(l = ()) -> int:
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

def cuvant_frecvent(s = "") -> str:
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
# print(cuvant_frecvent("apple banana banana banana apple orange banana apple"))

def switch_chei_valori(dictionar = {}) -> dict:
    dictionar2 = {}
    for key, value in dictionar.items():
        dictionar2[value] = key
    return dictionar2
# print(switch_chei_valori({"test": 3, "test2": 4}))



list1 = [(1, "apple"), (3, "orange"), (5, "banana")]
list2 = [(2, "grape"), (4, "kiwi"), (6, "melon")]

def homework(list1, list2) -> list[tuple]:
    lista = list1 + list2
    for i in range(0, len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][0] > lista[j][0]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
# print(homework(list1, list2))


people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"}
}

def oldest(dictionar = {}) -> tuple[str, int]:
    oldest = ""
    varsta_maxim = 0
    for key, value in dictionar.items():
        if(value["age"] > varsta_maxim):
            varsta_maxim = value["age"]
            oldest = key
    return oldest, varsta_maxim
# print(oldest(people))

def list_new_york(dictionar = {}) -> list[str]:
    lista = []
    for key, value in dictionar.items():
        if value["city"] == "New York":
            lista.append(key)
    return lista

# print(list_new_york(people))