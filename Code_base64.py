import base64

# You can specify any file to convert it to base64
# Можно указать любой файл, чтобы сконвертировать его в base64
font_file = "TiltNeon-Regular.ttf"
base64_file = "Code_base64.txt"

with open(font_file, "rb") as f:
    font_data = f.read()

base64_data = base64.b64encode(font_data).decode("utf-8")

with open(base64_file, "w") as f:
    f.write(base64_data)

print("Font encoded and saved to Font_base64.txt.")

# This script will convert the font "TiltNeon-Regular.ttf" to base64 and save it to "Code_base64.txt"
# Данный скрипт преобразует шрифт "TiltNeon-Regular.ttf" в base64 сохранив его в "Code_base64.txt"
