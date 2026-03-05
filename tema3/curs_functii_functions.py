# curs functii
def is_even(n = 0) -> bool:
    return n % 2 == 0
# print(is_even(2), is_even(3))

def maxim(a = 0, b = 0):
    return a if a > b else b
# print(maxim(2, 3))

def vowel_count(s = "") -> int:
    vowels = "aeiou"
    cnt = 0
    for i in s:
        if(i in vowels):
            cnt += 1
    return cnt
# print(vowel_count("lorem"))


def list_sum(l = []) -> int:
    suma = 0
    for i in l:
        suma += i
    return suma
# print(list_sum([1, 2, 3]))

def number_check(l = [], n = 0) -> bool:
    return (n in l)
# print(number_check([1, 2, 3], 4))

def analyze_word(word = "python") -> tuple:
    return len(word), vowel_count(word), word.upper()
# print(analyze_word("lorem"))

def minim_list(l = []) -> int:
    minim = l[0]
    for i in l:
        if i < minim:
            minim = i
    return minim

def maxim_list(l = []) -> int:
    maxim = l[0]
    for i in l:
        if i > maxim:
            maxim = i
    return maxim

def average(l = []) -> float:
    return list_sum(l) / len(l)

def odd_numbers_cnt(l = []) -> int:
    cnt = 0
    for i in l:
        if not(is_even(i)):
            cnt += 1
    return cnt

def number_stats(numbers = []) -> tuple:
    return minim_list(numbers), maxim_list(numbers), average(numbers), odd_numbers_cnt(numbers)
# print(number_stats([1, 2, 3, 4]))