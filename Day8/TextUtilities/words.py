from collections import Counter

def count_words(text):
    words = text.split()
    word_count =len(words)
    return word_count
    
def unique_words(text):
    unique_words=set(text.split())
    return unique_words

def reverse_word(text):
    words=text.split()
    return words[::-1]

def main():
    print("1.count words")
    print("2.unique words")
    print("3.reverse words")
    print("4.exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        text=input("Enter the text:")
        print("Word count:",count_words(text))
    elif choice==2:
        text=input("Enter the text:")
        print("Unique words:",unique_words(text))
    elif choice==3:
        text=input("Enter the text:")
        print("Reversed words:",reverse_word(text))
    elif choice ==4:
        print("Exiting the program.")
    else:
        print("Invalid choice.")
if __name__=="__main__":
    main()