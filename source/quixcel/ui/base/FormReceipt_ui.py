# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FormReceipt.ui'
#
# Created: Thu Aug 15 22:21:00 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormReceipt(object):
    def setupUi(self, FormReceipt):
        FormReceipt.setObjectName(_fromUtf8("FormReceipt"))
        FormReceipt.resize(658, 158)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormReceipt.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormReceipt)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FormReceipt)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_3 = QtGui.QComboBox(self.groupBox)
        self.comboBox_3.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setDuplicatesEnabled(True)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setDuplicatesEnabled(True)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.dateEdit_2 = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox)
        self.comboBox_6.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setDuplicatesEnabled(True)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.horizontalLayout_3.addWidget(self.comboBox_6)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.comboBox_7 = QtGui.QComboBox(self.groupBox)
        self.comboBox_7.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setDuplicatesEnabled(True)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.horizontalLayout_3.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(FormReceipt)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.pushButton_Cancel = QtGui.QPushButton(FormReceipt)
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.pushButton_Save = QtGui.QPushButton(FormReceipt)
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.horizontalLayout_4.addWidget(self.pushButton_Save)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FormReceipt)
        QtCore.QMetaObject.connectSlotsByName(FormReceipt)

    def retranslateUi(self, FormReceipt):
        FormReceipt.setWindowTitle(_translate("FormReceipt", "FormReceipt", None))
        self.groupBox.setTitle(_translate("FormReceipt", "收款记录/退款记录", None))
        self.label_7.setText(_translate("FormReceipt", "金 额：", None))
        self.label_5.setText(_translate("FormReceipt", "客 户：", None))
        self.label_4.setText(_translate("FormReceipt", "发货单：", None))
        self.label_6.setText(_translate("FormReceipt", "日 期：", None))
        self.label_8.setText(_translate("FormReceipt", "收/付款银行", None))
        self.label_13.setText(_translate("FormReceipt", "记 录：", None))
        self.label_2.setText(_translate("FormReceipt", "备注：", None))
        self.pushButton_Cancel.setText(_translate("FormReceipt", "取 消 (&C)", None))
        self.pushButton_Save.setText(_translate("FormReceipt", "保 存 (&S)", None))

