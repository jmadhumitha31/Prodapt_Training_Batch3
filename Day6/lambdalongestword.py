find_word=lambda sentence:max(sentence.split(),key=len)
sentence=input("Enter the word")
largest_word=find_word(sentence)
print("Largest Word:",largest_word)
