import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QEvent
from steamship import Steamship


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GPT-4")
        self.setGeometry(100, 100, 300, 300)

        # 创建输入文本框
        self.input_box = QTextEdit(self)
        self.input_box.setGeometry(20, 20, 260, 80)
        self.input_box.setPlaceholderText("请输入内容")
        self.input_box.setLineWrapMode(QTextEdit.NoWrap)  # 禁止换行
        self.input_box.setFontPointSize(12)
        self.input_box.installEventFilter(self)  # 安装事件过滤器

        # 创建发送按钮
        self.send_button = QPushButton("发送", self)
        self.send_button.setGeometry(100, 110, 80, 30)
        self.send_button.clicked.connect(self.send_input)

        # 创建输出文本框
        self.output_box = QTextEdit(self)
        self.output_box.setGeometry(20, 180, 260, 100)
        self.output_box.setReadOnly(True)
        self.output_box.setFontPointSize(10)
        self.output_box.setStyleSheet("background-color: #F5F5F5;")

        # 禁止窗口拖动
        self.setFixedSize(300, 300)
        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowMaximizeButtonHint)  # 禁止最大化按钮

    def eventFilter(self, obj, event):
        if obj == self.input_box and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.send_input()
            return True
        return super().eventFilter(obj, event)

    def send_input(self):
        # 获取输入框的文本
        input_text = self.input_box.toPlainText()
        # 下次输入内容时清除之前的结果
        self.output_box.clear()

        # GPT 响应内容
        answer = self.get_GPT(str(input_text))
        self.output_box.append("GPT 的回答是: \n" + answer)

        # 清空输入框的文本
        self.input_box.clear()

    def get_GPT(self, input_text):
        # Create a Steamship client
        client = Steamship(workspace="gpt-4")

        # Create an instance of this generator
        generator = client.use_plugin('gpt-4')

        # Get the questions
        question = input_text

        # Generate text
        task = generator.generate(text=input_text)

        # Wait for completion of the task.
        task.wait()

        # Print the output
        return (task.output.blocks[0].text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
