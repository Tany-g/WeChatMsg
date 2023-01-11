# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainviewUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.sign_up = QtWidgets.QPushButton(Dialog)
        self.sign_up.setGeometry(QtCore.QRect(680, 10, 93, 28))
        self.sign_up.setObjectName("sign_up")
        self.message = QtWidgets.QTextBrowser(Dialog)
        self.message.setGeometry(QtCore.QRect(480, 50, 780, 520))
        self.message.setObjectName("message")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(480, 600, 800, 120))
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(1240, 0, 47, 51))
        self.toolButton.setObjectName("toolButton")
        self.btn_sendMsg = QtWidgets.QPushButton(Dialog)
        self.btn_sendMsg.setGeometry(QtCore.QRect(1162, 670, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sendMsg.setFont(font)
        self.btn_sendMsg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_sendMsg.setMouseTracking(False)
        self.btn_sendMsg.setAutoFillBackground(False)
        self.btn_sendMsg.setStyleSheet("QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    \n"
"    padding: 10px;\n"
"    color:rgb(5,180,104);\n"
"}")
        self.btn_sendMsg.setIconSize(QtCore.QSize(40, 40))
        self.btn_sendMsg.setCheckable(False)
        self.btn_sendMsg.setAutoDefault(True)
        self.btn_sendMsg.setObjectName("btn_sendMsg")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(480, 570, 800, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(480, 50, 800, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(480, 0, 3, 720))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(460, 50, 16, 671))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1260, 50, 16, 520))
        self.verticalScrollBar_2.setStyleSheet("background-color: #f0f0f0;")
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 50, 300, 80))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 111, 562))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_chat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_chat.setObjectName("btn_chat")
        self.verticalLayout_2.addWidget(self.btn_chat)
        self.btn_contact = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_contact.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_contact.setObjectName("btn_contact")
        self.verticalLayout_2.addWidget(self.btn_contact)
        self.btn_addC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addC.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_addC.setObjectName("btn_addC")
        self.verticalLayout_2.addWidget(self.btn_addC)
        self.btn_delC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_delC.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_delC.setObjectName("btn_delC")
        self.verticalLayout_2.addWidget(self.btn_delC)
        self.btn_create_group = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_create_group.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_create_group.setObjectName("btn_create_group")
        self.verticalLayout_2.addWidget(self.btn_create_group)
        self.btn_add_group = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add_group.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_add_group.setObjectName("btn_add_group")
        self.verticalLayout_2.addWidget(self.btn_add_group)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.myavatar = QtWidgets.QLabel(Dialog)
        self.myavatar.setGeometry(QtCore.QRect(10, 30, 100, 100))
        self.myavatar.setObjectName("myavatar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sign_up.setText(_translate("Dialog", "退出登录"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.btn_sendMsg.setText(_translate("Dialog", "发送"))
        self.btn_chat.setText(_translate("Dialog", "聊天"))
        self.btn_contact.setText(_translate("Dialog", "联系人"))
        self.btn_addC.setText(_translate("Dialog", "添加联系人"))
        self.btn_delC.setText(_translate("Dialog", "删除联系人"))
        self.btn_create_group.setText(_translate("Dialog", "建群"))
        self.btn_add_group.setText(_translate("Dialog", "加群"))
        self.pushButton_6.setText(_translate("Dialog", "设置"))
        self.myavatar.setText(_translate("Dialog", "avatar"))
