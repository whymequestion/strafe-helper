import keyboard, time, threading
import sys, pypresence,pickle,os
from pathlib import Path
from PyQt6.QtWidgets import QApplication,  QWidget, QLabel, QLineEdit, QPushButton,  QVBoxLayout
import PyQt6.QtCore as QtCore
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
class main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('idk what this is')
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setStretch(0, 1)
        self.heading = QLabel(
            'Welcome.',
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.stop = False
        self.heading.setObjectName('heading')
        self.btn = QPushButton('Start')
        layout.addWidget(self.heading)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.start)
        self.show()
    def start(self):
        global thread
        self.stop= False
        thread = threading.Thread(target=self.main, args=())
        self.btn.setText('Stop')
        self.btn.clicked.connect(self.stopping)
        thread.start()
    def stopping(self):
        self.btn.setText('Start')
        self.btn.clicked.connect(self.start)
        self.stop = True
    def main(self):
        ignore = False
        while True and not self.stop:
            if keyboard.is_pressed('a') or keyboard.is_pressed('d'):
                if keyboard.is_pressed('d') and not ignore:
                    keyboard.release('a')
                    while True:
                        if keyboard.is_pressed('d') and keyboard.is_pressed('a'):
                            pass
                        else:
                            ignore = True  
                            break
                if keyboard.is_pressed('a'):
                    keyboard.release('d')
                    while True:
                        if keyboard.is_pressed('d') and keyboard.is_pressed('a'):
                            pass
                        else:
                            ignore=False 
                            break
            time.sleep(0.1)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('start.css').read_text())
    window = main()

    sys.exit(app.exec())