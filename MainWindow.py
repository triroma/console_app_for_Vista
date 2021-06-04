from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(800, 750)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(75, 50, 725, 600))
        self.stackedWidget.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.page_1)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_1.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_1.setRowCount(0)
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_1)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_4.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.page_7)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_7.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.page_8)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_8.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.page_9)
        self.tableWidget_9.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_9.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.tableWidget_10 = QtWidgets.QTableWidget(self.page_10)
        self.tableWidget_10.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_10.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_10.setRowCount(0)
        self.tableWidget_10.setObjectName("tableWidget_10")
        self.tableWidget_10.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.tableWidget_11 = QtWidgets.QTableWidget(self.page_11)
        self.tableWidget_11.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_11.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_11.setRowCount(0)
        self.tableWidget_11.setObjectName("tableWidget_11")
        self.tableWidget_11.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.tableWidget_12 = QtWidgets.QTableWidget(self.page_12)
        self.tableWidget_12.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_12.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_12.setRowCount(0)
        self.tableWidget_12.setObjectName("tableWidget_12")
        self.tableWidget_12.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.tableWidget_13 = QtWidgets.QTableWidget(self.page_13)
        self.tableWidget_13.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_13.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_13.setRowCount(0)
        self.tableWidget_13.setObjectName("tableWidget_13")
        self.tableWidget_13.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_13)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_3.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.page_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_5.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.page_6)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 725, 600))
        self.tableWidget_6.setMinimumSize(QtCore.QSize(725, 0))
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        self.stackedWidget.addWidget(self.page_6)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 0, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 25, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 50, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 75, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 100, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 125, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 150, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 175, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 200, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 225, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 250, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 275, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 300, 75, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_your_logis_is = QtWidgets.QLabel(self.centralwidget)
        self.label_your_logis_is.setGeometry(QtCore.QRect(450, 0, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_your_logis_is.setFont(font)
        self.label_your_logis_is.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_your_logis_is.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_your_logis_is.setAlignment(QtCore.Qt.AlignCenter)
        self.label_your_logis_is.setObjectName("label_your_logis_is")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(650, 0, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setWordWrap(True)
        self.label_user.setObjectName("label_user")
        self.New_btn = QtWidgets.QPushButton(self.centralwidget)
        self.New_btn.setGeometry(QtCore.QRect(20, 670, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.New_btn.setFont(font)
        self.New_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.New_btn.setObjectName("New_btn")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(180, 670, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.edit_btn.setObjectName("edit_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(340, 670, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.delete_btn.setObjectName("delete_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(650, 670, 140, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(255, 255, 255);")
        self.exit_btn.setObjectName("exit_btn")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Номер телефона"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата рождения"))
        self.pushButton_1.setText(_translate("MainWindow", "АБ"))
        self.pushButton_2.setText(_translate("MainWindow", "ВГ"))
        self.pushButton_3.setText(_translate("MainWindow", "ДЕ"))
        self.pushButton_4.setText(_translate("MainWindow", "ЖЗИЙ"))
        self.pushButton_5.setText(_translate("MainWindow", "КЛ"))
        self.pushButton_6.setText(_translate("MainWindow", "МН"))
        self.pushButton_7.setText(_translate("MainWindow", "ОП"))
        self.pushButton_8.setText(_translate("MainWindow", "РС"))
        self.pushButton_9.setText(_translate("MainWindow", "ТУ"))
        self.pushButton_10.setText(_translate("MainWindow", "ФХ"))
        self.pushButton_11.setText(_translate("MainWindow", "ЦЧШЩ"))
        self.pushButton_12.setText(_translate("MainWindow", "ЪЫЬЭ"))
        self.pushButton_13.setText(_translate("MainWindow", "ЮЯ"))
        self.label_your_logis_is.setText(_translate("MainWindow", "Вы вошли как:"))
        self.label_user.setText(_translate("MainWindow", ""))
        self.New_btn.setText(_translate("MainWindow", "Создать"))
        self.edit_btn.setText(_translate("MainWindow", "Редактировать"))
        self.delete_btn.setText(_translate("MainWindow", "Удалить"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти из аккаунта"))






