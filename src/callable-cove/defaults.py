def str_to_list(string: str, header: list = [], repeat: int = 1) -> list:
    """Naïve function to convert a string into a list of characters"""
    for i in range(repeat):
        for i in string:
            header.append(i)

    return header


def main():
    # Get a tuple with the function's default values
    print(f"{str_to_list.__defaults__=}")

    # Looks like it's working correctly!
    print(f"{str_to_list('hello')=}")

    # But the default is a mutable object :S
    print(f"{str_to_list('HOLA')=}")

    # The default value changed by calling the function :/
    print(f"{str_to_list.__defaults__=}")

    # Not the best implementation
    print(f"{str_to_list('HOLA', header=[])=}")


if __name__ == "__main__":
    main()
