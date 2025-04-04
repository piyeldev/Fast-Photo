from PySide6.QtWidgets import QWidget, QStackedLayout, QLabel, QSizePolicy, QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

class PictureItem(QWidget):
    def __init__(self, img_path:str):
        super().__init__()
        self.layout = QStackedLayout()
        self.layout.setContentsMargins(6, 0, 6, 0)
        self.layout.setStackingMode(QStackedLayout.StackAll)
        self.setLayout(self.layout)

        print(f'{__name__}: {img_path}')
        
        self.image = QPixmap(img_path)
        self.lbl = QLabel()
        self.lbl.setPixmap(self.image)
        self.layout.addWidget(self.lbl)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # overlay
        self.overlay = QWidget(self)
        self.overlay.setStyleSheet("background-color: #99000000")
        self.overlay.setFixedSize(214, 160)
        print(f'geometry: {self.overlay.geometry()}')
        self.overlay.hide()
        self.overlay.setAutoFillBackground(True)
        self.layout.addWidget(self.overlay)


        overlay_layout = QHBoxLayout()
        self.overlay.setLayout(overlay_layout)
        delete_btn = QPushButton()
        delete_icon = QIcon("../assets/icons/trash_icon.png")
        delete_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        delete_btn.setIcon(delete_icon) 
        delete_btn.setCursor(Qt.CursorShape.OpenHandCursor)
        delete_btn.setStyleSheet(f"background-color: #CC474747; border-radius: 0.4em; padding: 5px;")
        delete_btn.setFlat(True)

        delete_btn.clicked.connect(self.delete_self)
        overlay_layout.addWidget(delete_btn)

        


    def delete_self(self):
        from components.captures_list import CapturesList
        self.captures_list = CapturesList()
        self.captures_list.removePicture(self)

    def enterEvent(self, event):
        super().enterEvent(event)
        print("show")
        self.layout.setCurrentIndex(1)


    def leaveEvent(self, event):
        super().leaveEvent(event)
        print("hide")
        self.layout.setCurrentIndex(0)


    def setPixmapSize(self, size:QSize):
        self.lbl.setPixmap(self.image.scaled(size, Qt.KeepAspectRatio))


        
