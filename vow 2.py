from itertools import product
def count_sorted_vowel_strings(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    combinations = product(vowels, repeat=n)
    sorted_strings = filter(lambda x: x == tuple(sorted(x)), combinations)
    return len(list(sorted_strings))
n = 1
print(count_sorted_vowel_strings(n))  
