# CreditCheck

#### 介绍

自动解析pdf格式的培养方案和pdf格式的成绩单，生成学分清查通知单。

#### 软件架构

软件架构说明

#### 安装教程

如果使用powershell，需要在管理员状态下输入：

```powershell
Set-ExecutionPolicy RemoteSigned
```

创建虚拟环境并安装依赖：

```powershell
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

打包：

```powershell
pyinstaller -w -i .\doc\icons\icon.ico .\src\main.py
```

如果出现以下的提示，输入 `y`。

```plaintext
WARNING: The output directory "X:XXX\...\dist\main" and ALL ITS CONTENTS will be REMOVED! Continue?
```

删除不需要的包以缩小软件大小，并复制素材到可执行文件的目录：

```powershell
.\bin\remove_not_use.bat
```

将启动脚本复制到 `dist`目录下

```powershell
copy .\bin\start.bat .\dist\学分清查工具.bat
```

将 `dist`目录下的 `main`和 `学分清查工具.bat`打包即可发布

#### 使用说明

![图片](doc/images/main_window.png)
