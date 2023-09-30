import sys
from PyQt5.QtWidgets import *
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.editor()
    def editor(self):
        about_text = "You must LOAD a file before saving a file."
        QMessageBox.about(self, "G-Editor", about_text)
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        open_action = QAction('Load', self)
        save_action = QAction('Save', self)
        ab = QAction("About",self)
        open_action.triggered.connect(self.load)
        save_action.triggered.connect(self.save)
        ab.triggered.connect(self.show_about_dialog)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addAction(ab)
        self.setWindowTitle('G-Editor - PyQT Edition')
        self.setGeometry(100, 100, 320, 240)
        self.current_file = None
    def load(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setPlainText(file.read())
                self.current_file = file_name
    def save(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text_edit.toPlainText())
        else:
            self.save_file_as()
    def show_about_dialog(self):
        about_text = "Text Editor\n\nCredits to OpenAI Inc © - ChatGPT - Okmeque1\nThis program has been written with ChatGPT in PyQT5.Thank you to OpenAI Inc © - ChatGPT for supporting this project."
        QMessageBox.about(self, "About", about_text)
app = QApplication(sys.argv)
editor = TextEditor()
editor.show()
sys.exit(app.exec_())
