def is_even(n: int = 0) -> bool:
    return n % 2 == 0
# print(is_even(2), is_even(3))

def maxim(a: int = 0, b: int = 0):
    return a if a > b else b
# print(maxim(2, 3))

def vowel_count(s: str = "") -> int:
    vowels = "aeiou"
    cnt = 0
    for i in s:
        if(i in vowels):
            cnt += 1
    return cnt
# print(vowel_count("lorem"))


def list_sum(l: list[int] = []) -> int:
    suma = 0
    for i in l:
        suma += i
    return suma
# print(list_sum([1, 2, 3]))

def number_check(s: list =  [], n: int = 0) -> bool:
    return (n in s)
# print(number_check([1, 2, 3], 4))

def analyze_word(word: str = "python") -> tuple:
    return len(word), vowel_count(word), word.upper()
# print(analyze_word("lorem"))

def minim_list(l: list[int] = []) -> int:
    minim = l[0]
    for i in l:
        if i < minim:
            minim = i
    return minim

def maxim_list(l: list[int] = []) -> int:
    maxim = l[0]
    for i in l:
        if i > maxim:
            maxim = i
    return maxim

def average(l: list[int] = []) -> float:
    return list_sum(l) / len(l)

def odd_numbers_cnt(l: list[int] = []) -> int:
    cnt = 0
    for i in l:
        if not(is_even(i)):
            cnt += 1
    return cnt

def number_stats(numbers: list[int] = []) -> tuple:
    return minim_list(numbers), maxim_list(numbers), average(numbers), odd_numbers_cnt(numbers)
# print(number_stats([1, 2, 3, 4]))