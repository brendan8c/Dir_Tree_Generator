import base64

font_file = "TiltNeon-Regular.ttf"
base64_file = "Font_base64.txt"

with open(font_file, "rb") as f:
    font_data = f.read()

base64_data = base64.b64encode(font_data).decode("utf-8")

with open(base64_file, "w") as f:
    f.write(base64_data)

print("Font encoded and saved to Font_base64.txt.")

# Данный скрипт преобразует шрифт "TiltNeon-Regular.ttf" в base64 сохранив его в "Font_base64.txt"
