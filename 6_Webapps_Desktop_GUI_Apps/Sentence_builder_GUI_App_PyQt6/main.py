from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')  # name on top of the widget of your app

window.show()
app.exec()


