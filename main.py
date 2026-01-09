import pyperclip


def check_clipboard():
    content = pyperclip.paste()

    if not content:
        content
    else:
        print(content[:50])


if __name__ == "__main__":
    check_clipboard()
