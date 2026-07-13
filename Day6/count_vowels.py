
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count

word = input("Enter the word: ")
c = count_vowels(word)
print("Number of vowels:", c)