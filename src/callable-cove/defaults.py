
def str_to_list(
    string: str, header: list = [], repeat: int = 1
) -> list:
    for i in range(repeat):
        for i in string:
            header.append(i)

    return header


def main():
    # Get a tuple with the default values
    print(str_to_list.__defaults__)

    # Looks like it's working correctly!
    hello = str_to_list("hello")
    print(hello)

    # But the default is a mutable object :S
    hola = str_to_list("hola")
    print(hola)

    # Tthe default value changed just by calling the function :S
    print(str_to_list.__defaults__)

    c = str_to_list("HOLA", header=[])
    print(c)


if __name__ == "__main__":
    main()
