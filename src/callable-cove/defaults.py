from io import StringIO


def markdown_to_html(text: str, template={"#": "<h1>", "##": "<h2>"}) -> list:
    html = StringIO()

    for line in text.splitlines():
        if "# " in line:
            html.write("<h1>")
            html.write(template[0] + line.replace("# ", "") + template[-1])
            html.write("</h1>")

        elif "## " in line:
            html.write(line)

    return html.getvalue()


def main():
    print(markdown_to_html("# A title"))
    print(markdown_to_html("A paragraph"))
    print(markdown_to_html("# A title"))
    print(markdown_to_html("# A title"))
    print(markdown_to_html("A paragraph"))


# def str_to_list(string: str, header: list = [], repeat: int = 1) -> list:
#     """Naïve function to convert a string into a list of characters"""
#     for i in range(repeat):
#         for i in string:
#             header.append(i)

#     return header

# def main():
#     # Get a tuple with the function's default values
#     print(f"{str_to_list.__defaults__=}")

#     # Looks like it's working correctly!
#     print(f"{str_to_list('hello')=}")

#     # Looks like it's working correctly!
#     print(f"{str_to_list('hello', header=['>'])=}")

#     # But the default is a mutable object :S
#     print(f"{str_to_list('HOLA')=}")

#     # The default value changed by calling the function :/
#     print(f"{str_to_list.__defaults__=}")

#     # Not the best implementation
#     print(f"{str_to_list('HOLA', header=[])=}")


if __name__ == "__main__":
    main()
