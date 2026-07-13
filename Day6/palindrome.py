def is_palin(s):
    txt=s.lower()
    return txt == txt[::-1]

    word=input("Enter a string")
    if is_palin(word):
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is not a palindrome')
    
    