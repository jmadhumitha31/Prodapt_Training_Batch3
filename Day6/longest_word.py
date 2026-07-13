def find_longest_word(word):
    highest=-1
    if(len(word)>highest):
        highest=len(word)
    print(highest)

text=input("Enter the word line")
list1=text.split(" ");
for i in list1:
     find_longest_word(i)

