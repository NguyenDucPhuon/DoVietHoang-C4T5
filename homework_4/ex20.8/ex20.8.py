sentence = input("Enter a sentence")
sentence = sentence.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_counts = {}
for letter in sentence:
    if letter in alphabet:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

for keys, values in letter_counts.items():
    print(keys, values)