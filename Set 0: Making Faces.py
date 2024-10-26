def convert(y):
    y= y.replace(":)", "🙂", len(y))
    y= y.replace(":(", "🙁", len(y))
    return(y)


def main():
    x= input("Enter your text here")
    new_text= convert(x)
    print(new_text)

main()
