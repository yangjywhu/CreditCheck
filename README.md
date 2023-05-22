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

安装：

```powershell
# 删除已存在文件
rm -r .\build
rm -r .\dist
rm -r .\env

# 创建虚拟环境并打包
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
pyinstaller -w -i .\doc\icons\icon.ico .\src\main.py

# 删除不需要的文件并生成启动脚本
.\bin\remove_not_use.bat
copy .\bin\start.bat .\dist\学分清查工具.bat
```

如果出现以下的提示，输入 `y`。

```plaintext
WARNING: The output directory "X:XXX\...\dist\main" and ALL ITS CONTENTS will be REMOVED! Continue?
```

将 `dist`目录下的 `main`和 `学分清查工具.bat`打包即可发布

#### 使用说明

![图片](doc/images/main_window.png)

请点击【生成通知书】开始运行程序。完成后，点击【打开通知书目录】查看生成的通知书所在文件夹。

- 年级设置：当前年级1为大一，2为大二，以此类推；当前学期1为上学期，2为下学期。
- 必修类型：勾选的课程类型中，每一门课程会检查是否已修完并及格。如果成绩单中的课程名称（不包含字母）与培养方案相同，且学分大于或等于培养方案中该门课程的学分，则可以通过检查；如不符合则视为未修，请通知学生检查该门课程是否已转换成功。
- 分数设置：请正确输入等次成绩与百分制分数的对应关系。如果某门课的分数低于预警分数，则视为挂科，该门课的学分不能记录。
- 相同课程：已自动将除去字母后的课程名进行比对，如高等数学A（I）可转换为高等数学B1。但有一些相同的课程不符合此规则，一般为院内不同专业的可成，如图中所示。
- 其他课程：目前暂无法转换的课程，只能归为“其他课程”，不参与学分的计算
- 培养方案：包含pdf格式的培养方案的文件夹，文件名格式为【年级+专业代码+专业名称.pdf】，如【20211621_会计学.pdf】。
- 成绩单：所有人成绩单的pdf，注意是单个文件，每一页是一名同学的成绩单。
- 通知书模板：docx格式的Word文档，双大括号中的内容将会被替换。请参考示例文档。
- 通知书保存：每人一个Word文档，文件名为【班级_姓名.docx】。



输出文件夹中，`Summary.xlsx`是所有学生的学分清查结果总结，有如下几列（对应Word中双大括号中的内容）：

- 班级
- 姓名
- 学号
- 专业必完成科目
- 专业必GPA
- 必修课转换
- 专业选完成科目
- 选修课转换
- 必须完成的类型
- 必修未完成数目
- 必修未完成科目
- 专业选应
- 专业选实
- 通识选应
- 通识选实
