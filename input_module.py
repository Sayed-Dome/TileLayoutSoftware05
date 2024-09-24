import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class InputModule(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Input Module')

        layout = QVBoxLayout()

        label_width = QLabel('Width (mm):')
        self.width_input = QLineEdit()
        layout.addWidget(label_width)
        layout.addWidget(self.width_input)

        label_length = QLabel('Length (mm):')
        self.length_input = QLineEdit()
        layout.addWidget(label_length)
        layout.addWidget(self.length_input)

        label_pattern = QLabel('Layout Pattern:')
        self.pattern_input = QLineEdit()
        layout.addWidget(label_pattern)
        layout.addWidget(self.pattern_input)

        button_submit = QPushButton('Submit')
        button_submit.clicked.connect(self.submit)
        layout.addWidget(button_submit)

        self.setLayout(layout)

    def submit(self):
        width = float(self.width_input.text())
        length = float(self.length_input.text())
        pattern = self.pattern_input.text()
        self.close()
        return width, length, pattern

    def get_room_dimensions(self):
        return self.submit()

    def get_tile_size(self):
        return self.submit()

    def get_layout_pattern(self):
        return self.submit()

if __name__ == "__main__":
    app = QApplication([])
    input_module = InputModule()
    input_module.show()
    app.exec_()
