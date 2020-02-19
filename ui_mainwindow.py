# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 781, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_Depth = QtWidgets.QFrame(self.tab)
        self.frame_Depth.setGeometry(QtCore.QRect(30, 90, 349, 351))
        self.frame_Depth.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_Depth.setAcceptDrops(True)
        self.frame_Depth.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Depth.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Depth.setObjectName("frame_Depth")
        self.depth_label = QtWidgets.QLabel(self.frame_Depth)
        self.depth_label.setGeometry(QtCore.QRect(10, 10, 321, 321))
        self.depth_label.setText("")
        self.depth_label.setObjectName("depth_label")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(410, 30, 291, 32))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_Color = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_Color.setObjectName("pushButton_Color")
        self.horizontalLayout_4.addWidget(self.pushButton_Color)
        self.frame_Color = QtWidgets.QFrame(self.tab)
        self.frame_Color.setGeometry(QtCore.QRect(400, 90, 349, 351))
        self.frame_Color.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_Color.setAcceptDrops(True)
        self.frame_Color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Color.setObjectName("frame_Color")
        self.color_label = QtWidgets.QLabel(self.frame_Color)
        self.color_label.setGeometry(QtCore.QRect(10, 10, 321, 321))
        self.color_label.setText("")
        self.color_label.setObjectName("color_label")
        self.pushButton_Run = QtWidgets.QPushButton(self.tab)
        self.pushButton_Run.setGeometry(QtCore.QRect(190, 470, 381, 32))
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 291, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_Depth = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Depth.setEnabled(True)
        self.pushButton_Depth.setObjectName("pushButton_Depth")
        self.horizontalLayout.addWidget(self.pushButton_Depth)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.pushButton_Depth.clicked.connect(self.browImage)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Color"))
        self.pushButton_Color.setText(_translate("MainWindow", "Browse"))
        self.pushButton_Run.setText(_translate("MainWindow", "Run RGBD"))
        self.label.setText(_translate("MainWindow", "Depth"))
        self.pushButton_Depth.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    def browImage(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Browse Image", "/Users/nghiato/master-research/open3d", "Image Files (*.png *.jpg *.bmp *.JPG)")
        print(fileName)
        print(fileName[0])

        # lb = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap(fileName[0])
        # height_label = 100
        # lb.resize(self.width(), height_label)
        self.color_label.setPixmap(pixmap.scaled(self.color_label.size(), QtCore.Qt.IgnoreAspectRatio))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
