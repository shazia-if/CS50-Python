def main():
    x= input("Greeting:")
    print(f"${value(x)}")


def value(x):
    greeting= x.casefold().strip()
    money=0

    if "hello" in greeting:
        money=0
    elif greeting.startswith("h"):
        money=20
    else:
        money=100

    return money



if __name__ == "__main__":
    main()
