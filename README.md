## Генератор визуальной структуры каталогов и файлов
#### Эта программа создает визуальный каталог файловой системы, отображая файлы и папки в виде иерархической древовидной структуры.

#### Пример вывода:

<p align="left">
  <img src="readme_md/example.png" alt="Alt Text" width="50%">
</p>

#### Как использовать:
- Просто скопируйте ваш путь к каталогу и вставьте его в приложении **[Dir Tree Generator.exe](https://github.com/brendan8c/Dir_Tree_Generator/releases)**
- Обратите внимание изначально в приложении указано игнорировать такие каталоги как: **.git**, **.vscode**, **node_modules** а также будут проигнорированы все файлы и подкаталоги внутри этих папок. У вас есть возможность добавлять или удалять каталоги.
- Также вы можете использовать вместо приложения файл **fast_DirTreeGenerator.bat**.
  Для того чтобы добавить или удалить каталог, вам нужно будет отредактировать в файле **fast_DirTreeGenerator.py** значение переменной `IGNORED_FOLDERS = ['.git', '.vscode', 'node_modules']`.
<p align="left">
  <img src="readme_md/001.gif" alt="Alt Text" width="100%">
</p>

- Если вы хотите сами собрать проект используйте эти ключи.  
For Linux: `pyinstaller --onefile --windowed --icon=app.png DirTreeGenerator.py`  
For macOS: `pyinstaller --onefile --windowed --icon=app.icns DirTreeGenerator.py`  
For Windows: `pyinstaller --onefile --windowed --icon=app.ico DirTreeGenerator.py`  


- Установите необходимые зависимости:  
`pip install pyinstaller`, `pip instal pyqt5`, `pip install pyqt5-tools`  


- Для того чтобы добавить свой шрифт, вам нужно преобразовать его в формат base64, для этого в файле **Font_base64.py** отредактируйте эту строку `font_file = "TiltNeon-Regular.ttf"` изменив значение переменной на название вашего шрифта., Запустите данный файл, после чего он создаст текстовый файл **Font_base64.txt** который будет содержать нужную вам кодировку., Затем в файле **DirTreeGenerator\.py** измените значение переменной `base64_font = 'your_base64_here'` на ваши символы base64.  


- Если у вас есть какие-то предложения или вопросы вы можете их задать в этом репозитории! :speech_balloon:  
- Делайте свой вклад в этот проект! :wink:  