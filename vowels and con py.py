def count_vowels_and_consonants(sentence):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    num_vowels = 0
    num_consonants = 0
    
    for char in sentence:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
            
    return num_vowels, num_consonants

sentence = input("Enter a sentence: ")
vowels, consonants = count_vowels_and_consonants(sentence)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
