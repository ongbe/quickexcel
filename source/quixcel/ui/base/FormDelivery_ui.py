# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FormDelivery.ui'
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

class Ui_FormDelivery(object):
    def setupUi(self, FormDelivery):
        FormDelivery.setObjectName(_fromUtf8("FormDelivery"))
        FormDelivery.resize(658, 188)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormDelivery.setFont(font)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FormDelivery)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(FormDelivery)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.lineEdit_SN = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_SN.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_SN.setObjectName(_fromUtf8("lineEdit_SN"))
        self.horizontalLayout_2.addWidget(self.lineEdit_SN)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(80, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.comboBox_Customer = QtGui.QComboBox(self.groupBox)
        self.comboBox_Customer.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_Customer.setEditable(True)
        self.comboBox_Customer.setDuplicatesEnabled(True)
        self.comboBox_Customer.setObjectName(_fromUtf8("comboBox_Customer"))
        self.horizontalLayout_2.addWidget(self.comboBox_Customer)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_Product = QtGui.QComboBox(self.groupBox)
        self.comboBox_Product.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_Product.setEditable(True)
        self.comboBox_Product.setDuplicatesEnabled(True)
        self.comboBox_Product.setObjectName(_fromUtf8("comboBox_Product"))
        self.horizontalLayout_2.addWidget(self.comboBox_Product)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(80, 0))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.doubleSpinBox_Price = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Price.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_Price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_Price.setObjectName(_fromUtf8("doubleSpinBox_Price"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_Price)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(80, 0))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_3.addWidget(self.label_14)
        self.doubleSpinBox_Num = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Num.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_Num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_Num.setDecimals(0)
        self.doubleSpinBox_Num.setMaximum(100000.0)
        self.doubleSpinBox_Num.setObjectName(_fromUtf8("doubleSpinBox_Num"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_Num)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.doubleSpinBox_Amount = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_Amount.setMinimumSize(QtCore.QSize(120, 0))
        self.doubleSpinBox_Amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_Amount.setObjectName(_fromUtf8("doubleSpinBox_Amount"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_Amount)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(80, 0))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox)
        self.comboBox_6.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_6.setEditable(True)
        self.comboBox_6.setDuplicatesEnabled(True)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.horizontalLayout.addWidget(self.comboBox_6)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(80, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.dateEdit_Date = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_Date.setMinimumSize(QtCore.QSize(120, 0))
        self.dateEdit_Date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateEdit_Date.setCalendarPopup(True)
        self.dateEdit_Date.setObjectName(_fromUtf8("dateEdit_Date"))
        self.horizontalLayout.addWidget(self.dateEdit_Date)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(80, 0))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout.addWidget(self.label_13)
        self.comboBox_7 = QtGui.QComboBox(self.groupBox)
        self.comboBox_7.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_7.setEditable(True)
        self.comboBox_7.setDuplicatesEnabled(True)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.horizontalLayout.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_10 = QtGui.QLabel(FormDelivery)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_4.addWidget(self.label_10)
        self.pushButton_Cancel = QtGui.QPushButton(FormDelivery)
        self.pushButton_Cancel.setObjectName(_fromUtf8("pushButton_Cancel"))
        self.horizontalLayout_4.addWidget(self.pushButton_Cancel)
        self.pushButton_Save = QtGui.QPushButton(FormDelivery)
        self.pushButton_Save.setObjectName(_fromUtf8("pushButton_Save"))
        self.horizontalLayout_4.addWidget(self.pushButton_Save)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(FormDelivery)
        QtCore.QMetaObject.connectSlotsByName(FormDelivery)

    def retranslateUi(self, FormDelivery):
        FormDelivery.setWindowTitle(_translate("FormDelivery", "FormDelivery", None))
        self.groupBox.setTitle(_translate("FormDelivery", "发货记录/退货记录", None))
        self.label_9.setText(_translate("FormDelivery", "发货单号：", None))
        self.label_5.setText(_translate("FormDelivery", "客 户：", None))
        self.label_4.setText(_translate("FormDelivery", "产 品：", None))
        self.label_7.setText(_translate("FormDelivery", "单 价：", None))
        self.label_14.setText(_translate("FormDelivery", "  数 量：", None))
        self.label_8.setText(_translate("FormDelivery", "金 额：", None))
        self.label_12.setText(_translate("FormDelivery", "业务员：", None))
        self.label_6.setText(_translate("FormDelivery", "日 期：", None))
        self.label_13.setText(_translate("FormDelivery", "记 录：", None))
        self.label_2.setText(_translate("FormDelivery", "备 注：", None))
        self.pushButton_Cancel.setText(_translate("FormDelivery", "取 消 (&C)", None))
        self.pushButton_Save.setText(_translate("FormDelivery", "保 存 (&S)", None))

