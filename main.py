import pyperclip
from weasyprint import HTML
import html


def check_clipboard():
    content = pyperclip.paste()

    if not content:
        return

    safe_content = html.escape(content)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <style>
            @page {{ margin: 1cm; }}
            body {{ 
                font-family: 'Courier New', monospace; /* Моноширинный шрифт для кода */
                background-color: #f5f5f5;
                font-size: 10pt;
            }}
            .content-block {{ white-space: pre-wrap; 
                word-wrap: break-word;
                color: #222; }}
        </style>
    </head>
    <body>
        <div class="content">{safe_content}</div>
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
