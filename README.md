<p align="center">
  <img src="readme_md/example.png" alt="Alt Text" width="80%">
</p>
  <div align="center">
    <!-- <div>
        <div>
            <a href="https://github.com/FFmpeg/FFmpeg">
                <img src=https://raw.githubusercontent.com/Brendan8c/FFMPEG_BAT/master/img/FFmpeg.svg width="70px" style="margin-top:-50px">
            </a>
        </div>
        <div>
            <a href="https://ko-fi.com/brendan8c">
                <img src="https://www.ko-fi.com/img/githubbutton_sm.svg" width="226px">
            </a>
        </div>
    </div> -->
    <div>
        <!-- <div>
            <a href="https://www.paypal.com/paypalme/artemguskov/5usd">
                <img src="https://raw.githubusercontent.com/Brendan8c/FFMPEG_BAT/master/img/PayPal.svg" width="100px">
            </a>
        </div> -->
        <div>
            <a href="https://img.shields.io/github/license/brendan8c/Dir_Tree_Generator">
                <img src="https://img.shields.io/badge/License-MIT-green.svg" width="100px">
            </a>
        </div>
    </div>
</div>


<details>
    <summary>---------------------------------------------:us: :us: :us: ENGLISH :us: :us: :us:---------------------------------------------</summary>
    <br />

## Visual directory and file structure generator.
#### This program creates a visual file system directory by displaying files and folders in a hierarchical tree structure.

#### How to use:
- Just copy your directory path and paste it in the app **[Dir Tree Generator.exe](https://github.com/brendan8c/Dir_Tree_Generator/releases)**
- Please note that initially the application was told to ignore such directories as: **.git**, **.vscode**, **node_modules** and will also ignore all files and subdirectories within those folders. You have the ability to add or remove directories.
- Also you can use file instead of application **fast_DirTreeGenerator.bat**.
  In order to add or remove a directory, you will need to edit the file **fast_DirTreeGenerator.py** variable value `IGNORED_FOLDERS = ['.git', '.vscode', 'node_modules']`.
<p align="left">
  <img src="readme_md/001.gif" alt="Alt Text" width="100%">
</p>

- If you want to build the project yourself, use these keys.  
For Linux: `pyinstaller --onefile --windowed --icon=app.png DirTreeGenerator.py`  
For macOS: `pyinstaller --onefile --windowed --icon=app.icns DirTreeGenerator.py`  
For Windows: `pyinstaller --onefile --windowed --icon=app.ico DirTreeGenerator.py`  


- Install required dependencies:  
`pip install pyinstaller`, `pip instal pyqt5`, `pip install pyqt5-tools`  


- In order to add your font, you need to convert it to base64 format, for this, in the file **Font_base64.py** edit this line `font_file = "TiltNeon-Regular.ttf"` by changing the value of the variable to the name of your font., Run this file, after which it will create a text file **Font_base64.txt** which will contain the encoding you need., then in the file **DirTreeGenerator\.py** change the value of the variable `base64_font = 'your_base64_here'` to your base64 characters.  


- If you have any suggestions or questions, you can ask them in this repository! :speech_balloon:  
- Please contribute to this project! :wink:  

</details>

<details>
    <summary>---------------------------------------------:ru: :ru: :ru: RUSSIAN :ru: :ru: :ru:---------------------------------------------</summary>
    <br />

## Генератор визуальной структуры каталогов и файлов.
#### Эта программа создает визуальный каталог файловой системы, отображая файлы и папки в виде иерархической древовидной структуры.

#### Как использовать:
- Просто скопируйте ваш путь к каталогу и вставьте его в приложении **[Dir Tree Generator.exe](https://github.com/brendan8c/Dir_Tree_Generator/releases)**
- Обратите внимание изначально в приложении указано игнорировать такие каталоги как: **.git**, **.vscode**, **node_modules** а также будут проигнорированы все файлы и подкаталоги внутри этих папок. У вас есть возможность добавлять или удалять каталоги.
- Также вы можете использовать вместо приложения файл **fast_DirTreeGenerator.bat**.
  Для того чтобы добавить или удалить каталог, вам нужно будет отредактировать в файле **fast_DirTreeGenerator.py** значение переменной `IGNORED_FOLDERS = ['.git', '.vscode', 'node_modules']`.
<p align="left">
  <img src="readme_md/001.gif" alt="Alt Text" width="100%">
</p>

- Если вы хотите сами собрать проект используйте эти ключи.  
Для Linux: `pyinstaller --onefile --windowed --icon=app.png DirTreeGenerator.py`  
Для macOS: `pyinstaller --onefile --windowed --icon=app.icns DirTreeGenerator.py`  
Для Windows: `pyinstaller --onefile --windowed --icon=app.ico DirTreeGenerator.py`  


- Установите необходимые зависимости:  
`pip install pyinstaller`, `pip instal pyqt5`, `pip install pyqt5-tools`  


- Для того чтобы добавить свой шрифт, вам нужно преобразовать его в формат base64, для этого в файле **Font_base64.py** отредактируйте эту строку `font_file = "TiltNeon-Regular.ttf"` изменив значение переменной на название вашего шрифта., Запустите данный файл, после чего он создаст текстовый файл **Font_base64.txt** который будет содержать нужную вам кодировку., Затем в файле **DirTreeGenerator\.py** измените значение переменной `base64_font = 'your_base64_here'` на ваши символы base64.  


- Если у вас есть какие-то предложения или вопросы вы можете их задать в этом репозитории! :speech_balloon:  
- Делайте свой вклад в этот проект! :wink:  

</details>
