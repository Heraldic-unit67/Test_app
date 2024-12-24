def main():
    name = input("what is your name??")
    print(hello(name))

def hello(to="world"):
    return f"hello,{to}"


if __name__ == "__main__":
    main()