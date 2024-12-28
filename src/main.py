from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QFontDatabase
import sys
import os
from windows.main_window import MainWindow

def load_fonts():
        poppins_dir = '../assets/fonts/Poppins'
        poppins_font_files = os.listdir(poppins_dir)

        for font_file in poppins_font_files:
            font_id = QFontDatabase.addApplicationFont(f'{poppins_dir}/{font_file}')
            if font_id == -1:
                print(f"err: font failed to load {font_file}:{font_id}")

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    load_fonts()
    loader = QUiLoader()
    window = loader.load("ui/heading.ui", None)
    # window = MainWindow()
    window.show()
    app.exec()