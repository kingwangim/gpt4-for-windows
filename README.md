# GPT-4 For Windows

## 介绍
本项目是一个基于GPT-4人工智能的Windows客户端，用户可以在图形化界面中输入问题，程序将自动调用GPT-4生成回答。数据通过 https://www.steamship.com/ 获得，使用PySide6制作成Gui，用pyinstaller打包成Windows客户端。

## 环境配置
Python 3.7及以上版本
PySide6 6.1.2及以上版本
steamship 1.0.0及以上版本

### 安装
安装Python，可在Python官网下载对应版本的安装程序进行安装。
在命令行中运行以下命令安装所需的Python库：
```
pip install PySide6
pip install steamship
```
下载本项目源代码或使用git clone命令从github上克隆本项目代码。

## 使用
在命令行中进入项目根目录。
运行以下命令启动程序：
```
python main.py
```
或下载并运行 [GPT-4.exe](https://github.com/kingwangim/gpt4-for-windows/raw/main/GPT-4.exe)，程序启动后，在输入框中输入问题，点击“发送”按钮获取回答。

## 第一次使用
第一次运行程序后，浏览器会自动跳转打开 https://www.steamship.com/ 网站，需注册对应账号，方可使用。登陆后，后续无需再次登录。

## 注意事项
- 使用本程序需要拥有有效的steamship API密钥，可以在 https://www.steamship.com/ 上申请。
- 本程序依赖于互联网连接，请确保计算机联网。
- 本程序不对GPT-4生成的回答内容负责，回答内容仅供参考，不代表真实情况。
- steamship Plan 截止至 2023/03/19 支持数量上限为500条。
- LICENSE: Apache-2.0

Author:
- kingwang
- ChatGPT
