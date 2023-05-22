rmdir /s/q .\build
rmdir /s/q .\dist
rmdir /s/q .\env

python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
pyinstaller -w -i .\doc\icons\icon.ico .\src\main.py

del /F .\dist\main\PySide6\MSVCP140.dll
del /F .\dist\main\PySide6\MSVCP140_1.dll
del /F .\dist\main\PySide6\MSVCP140_2.dll
del /F .\dist\main\PySide6\Qt6Network.dll
del /F .\dist\main\PySide6\Qt6OpenGL.dll
del /F .\dist\main\PySide6\Qt6Pdf.dll
del /F .\dist\main\PySide6\Qt6Qml.dll
del /F .\dist\main\PySide6\Qt6QmlModels.dll
del /F .\dist\main\PySide6\Qt6Quick.dll
del /F .\dist\main\PySide6\Qt6Svg.dll
del /F .\dist\main\PySide6\Qt6VirtualKeyboard.dll

rmdir /s/q .\dist\main\babel
xcopy /E/C/I/Y .\doc dist\main\doc
copy .\bin\start.bat .\dist\学分清查工具.bat