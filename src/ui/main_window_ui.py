# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import main_window_res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1391, 1000)
        MainWindow.setStyleSheet(u"border: none")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Poppins"])
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.TopBar = QWidget(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        sizePolicy.setHeightForWidth(self.TopBar.sizePolicy().hasHeightForWidth())
        self.TopBar.setSizePolicy(sizePolicy)
        self.TopBar.setMaximumSize(QSize(16777215, 100))
        self.TopBar.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.TopBar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(self.TopBar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setPixmap(QPixmap(u":/logo/imgs/logo.png"))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.TopBar)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Poppins ExtraBold"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.TopBar)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Poppins Light"])
        font2.setPointSize(10)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(1000000000, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.TopBar)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setStyleSheet(u"background-color: rgb(31, 177, 65);\n"
"border-radius: 30px;")
        icon = QIcon()
        icon.addFile(u":/settings_icon/icons/settings-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 60))
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.TopBar, 0, Qt.AlignmentFlag.AlignLeft)

        self.MainViewScroll = QScrollArea(self.centralwidget)
        self.MainViewScroll.setObjectName(u"MainViewScroll")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainViewScroll.sizePolicy().hasHeightForWidth())
        self.MainViewScroll.setSizePolicy(sizePolicy3)
        self.MainViewScroll.setStyleSheet(u"border: 1px solid black;")
        self.MainViewScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.MainViewScroll.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1357, 629))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.MainView = QWidget(self.scrollAreaWidgetContents)
        self.MainView.setObjectName(u"MainView")
        sizePolicy.setHeightForWidth(self.MainView.sizePolicy().hasHeightForWidth())
        self.MainView.setSizePolicy(sizePolicy)
        self.MainView.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.MainView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.CameraView = QWidget(self.MainView)
        self.CameraView.setObjectName(u"CameraView")
        sizePolicy1.setHeightForWidth(self.CameraView.sizePolicy().hasHeightForWidth())
        self.CameraView.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.CameraView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 0, -1)
        self.cam_view_lbl = QLabel(self.CameraView)
        self.cam_view_lbl.setObjectName(u"cam_view_lbl")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(10)
        font3.setWeight(QFont.DemiBold)
        self.cam_view_lbl.setFont(font3)

        self.verticalLayout_3.addWidget(self.cam_view_lbl)

        self.cam_prev = QLabel(self.CameraView)
        self.cam_prev.setObjectName(u"cam_prev")
        self.cam_prev.setMaximumSize(QSize(640, 480))
        self.cam_prev.setPixmap(QPixmap(u":/rectangle/imgs/Rectangle.png"))

        self.verticalLayout_3.addWidget(self.cam_prev)

        self.CamButtons = QWidget(self.CameraView)
        self.CamButtons.setObjectName(u"CamButtons")
        sizePolicy.setHeightForWidth(self.CamButtons.sizePolicy().hasHeightForWidth())
        self.CamButtons.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.CamButtons)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.take_pic = QPushButton(self.CamButtons)
        self.take_pic.setObjectName(u"take_pic")
        sizePolicy1.setHeightForWidth(self.take_pic.sizePolicy().hasHeightForWidth())
        self.take_pic.setSizePolicy(sizePolicy1)
        self.take_pic.setStyleSheet(u"width: 50px;\n"
"height: 50px;\n"
"border-radius: 25px;\n"
"background-color: #1fb141;")
        icon1 = QIcon()
        icon1.addFile(u":/shutter_icon/icons/camera_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.take_pic.setIcon(icon1)
        self.take_pic.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.take_pic, 0, Qt.AlignmentFlag.AlignLeft)

        self.record = QPushButton(self.CamButtons)
        self.record.setObjectName(u"record")
        sizePolicy1.setHeightForWidth(self.record.sizePolicy().hasHeightForWidth())
        self.record.setSizePolicy(sizePolicy1)
        self.record.setMaximumSize(QSize(170, 50))
        font4 = QFont()
        font4.setFamilies([u"Poppins ExtraBold"])
        font4.setPointSize(16)
        self.record.setFont(font4)
        self.record.setStyleSheet(u"background-color: rgb(31, 177, 65);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"width: 150;\n"
"height: 50;")
        icon2 = QIcon()
        icon2.addFile(u":/rec_icon/icons/video-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.record.setIcon(icon2)
        self.record.setIconSize(QSize(36, 36))
        self.record.setFlat(True)

        self.horizontalLayout_3.addWidget(self.record)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.CamButtons)


        self.horizontalLayout_2.addWidget(self.CameraView)

        self.ToolsView = QWidget(self.MainView)
        self.ToolsView.setObjectName(u"ToolsView")
        self.ToolsViews = QVBoxLayout(self.ToolsView)
        self.ToolsViews.setObjectName(u"ToolsViews")
        self.ToolsViews.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalWidget = QWidget(self.ToolsView)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy2.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_7 = QLabel(self.horizontalWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.pushButton_2 = QPushButton(self.horizontalWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: #1fb141; \n"
"border-radius: 8px;\n"
"width: 111px;\n"
"height: 23px;\n"
"margin-bottom: 5px;")
        icon3 = QIcon()
        icon3.addFile(u":/edit_icon/icons/edit_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout_4.addWidget(self.horizontalWidget)

        self.label_6 = QLabel(self.ToolsView)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(425, 228))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setPixmap(QPixmap(u":/rectangle/imgs/Rectangle.png"))

        self.verticalLayout_4.addWidget(self.label_6)


        self.ToolsViews.addLayout(self.verticalLayout_4)

        self.label_5 = QLabel(self.ToolsView)
        self.label_5.setObjectName(u"label_5")

        self.ToolsViews.addWidget(self.label_5)


        self.horizontalLayout_2.addWidget(self.ToolsView, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_4.addWidget(self.MainView)

        self.MainViewScroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.MainViewScroll, 0, Qt.AlignmentFlag.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fast Photo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"v1.0-dev", None))
        self.pushButton.setText("")
        self.cam_view_lbl.setText(QCoreApplication.translate("MainWindow", u"Camera View:", None))
        self.cam_prev.setText("")
        self.take_pic.setText("")
        self.record.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Frame View", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit Frame", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

