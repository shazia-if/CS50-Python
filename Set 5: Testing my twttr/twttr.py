def main():
    word= input("Say something here:")
    chat= shorten(word)
    print(chat)

def shorten(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    Word=""
    for character in word:
        if character in vowels:
           continue
        else:
            Word=Word+character
    return Word


if __name__ == "__main__":
    main()
