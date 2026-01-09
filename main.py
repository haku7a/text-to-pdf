import pyperclip
from weasyprint import HTML


def check_clipboard():
    content = pyperclip.paste()

    if not content:
        content

    html_template = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: sans-serif; padding: 20px; line-height: 1.6; }}
            .content {{ white-space: pre-wrap; }}
        </style>
    </head>
    <body>
        <div class="content">{content}</div>
    </body>
    </html>
"""

    try:
        output_file = "output.pdf"
        HTML(string=html_template).write_pdf(output_file)
        print(f"PDF Created")
    except Exception as e:
        print(f"PDF Generation Failed: {e}")


if __name__ == "__main__":
    check_clipboard()
