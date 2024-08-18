# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thorlabs_pm_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_wMainWindow(object):
    def setupUi(self, wMainWindow):
        if not wMainWindow.objectName():
            wMainWindow.setObjectName(u"wMainWindow")
        wMainWindow.resize(1150, 640)
        wMainWindow.setMinimumSize(QSize(1150, 640))
        wMainWindow.setMaximumSize(QSize(1150, 640))
        self.groupBox = QGroupBox(wMainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 291, 111))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.entrySN = QLineEdit(self.groupBox)
        self.entrySN.setObjectName(u"entrySN")

        self.gridLayout.addWidget(self.entrySN, 0, 1, 1, 1)

        self.buttonInit = QPushButton(self.groupBox)
        self.buttonInit.setObjectName(u"buttonInit")

        self.gridLayout.addWidget(self.buttonInit, 0, 2, 1, 1)

        self.labelConnectionMsg = QLabel(self.groupBox)
        self.labelConnectionMsg.setObjectName(u"labelConnectionMsg")
        self.labelConnectionMsg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelConnectionMsg, 1, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(wMainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 130, 291, 227))
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.labelSensorModel = QLineEdit(self.groupBox_2)
        self.labelSensorModel.setObjectName(u"labelSensorModel")
        self.labelSensorModel.setEnabled(False)
        self.labelSensorModel.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelSensorModel)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.labelSensorSN = QLineEdit(self.groupBox_2)
        self.labelSensorSN.setObjectName(u"labelSensorSN")
        self.labelSensorSN.setEnabled(False)
        self.labelSensorSN.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelSensorSN)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.labelSensorCalmsg = QLineEdit(self.groupBox_2)
        self.labelSensorCalmsg.setObjectName(u"labelSensorCalmsg")
        self.labelSensorCalmsg.setEnabled(False)
        self.labelSensorCalmsg.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.labelSensorCalmsg)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.labelSensorType = QLineEdit(self.groupBox_2)
        self.labelSensorType.setObjectName(u"labelSensorType")
        self.labelSensorType.setEnabled(False)
        self.labelSensorType.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.labelSensorType)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.labelSensorSubtype = QLineEdit(self.groupBox_2)
        self.labelSensorSubtype.setObjectName(u"labelSensorSubtype")
        self.labelSensorSubtype.setEnabled(False)
        self.labelSensorSubtype.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.labelSensorSubtype)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.labelSensorFlag = QLineEdit(self.groupBox_2)
        self.labelSensorFlag.setObjectName(u"labelSensorFlag")
        self.labelSensorFlag.setEnabled(False)
        self.labelSensorFlag.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.labelSensorFlag)


        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(wMainWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 370, 291, 253))
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelZeroUnit = QLabel(self.groupBox_3)
        self.labelZeroUnit.setObjectName(u"labelZeroUnit")

        self.gridLayout_4.addWidget(self.labelZeroUnit, 7, 4, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 6, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_10, 0, 4, 1, 1)

        self.entryWavelength = QLineEdit(self.groupBox_3)
        self.entryWavelength.setObjectName(u"entryWavelength")
        self.entryWavelength.setEnabled(False)
        self.entryWavelength.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.entryWavelength, 0, 2, 1, 2)

        self.entryAvg = QSpinBox(self.groupBox_3)
        self.entryAvg.setObjectName(u"entryAvg")
        self.entryAvg.setEnabled(False)
        self.entryAvg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.entryAvg.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.entryAvg.setMinimum(1)
        self.entryAvg.setMaximum(500)
        self.entryAvg.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.entryAvg, 1, 2, 1, 3)

        self.checkbuttonAutoRange = QCheckBox(self.groupBox_3)
        self.checkbuttonAutoRange.setObjectName(u"checkbuttonAutoRange")
        self.checkbuttonAutoRange.setEnabled(False)
        font = QFont()
        font.setKerning(True)
        self.checkbuttonAutoRange.setFont(font)
        self.checkbuttonAutoRange.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkbuttonAutoRange.setCheckable(True)

        self.gridLayout_4.addWidget(self.checkbuttonAutoRange, 4, 2, 1, 3)

        self.comboBoxUnits = QComboBox(self.groupBox_3)
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.addItem("")
        self.comboBoxUnits.setObjectName(u"comboBoxUnits")
        self.comboBoxUnits.setEnabled(False)
        self.comboBoxUnits.setMaxVisibleItems(2)

        self.gridLayout_4.addWidget(self.comboBoxUnits, 5, 2, 1, 3)

        self.labelZeroValue = QLineEdit(self.groupBox_3)
        self.labelZeroValue.setObjectName(u"labelZeroValue")
        self.labelZeroValue.setEnabled(False)
        self.labelZeroValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.labelZeroValue.setReadOnly(True)

        self.gridLayout_4.addWidget(self.labelZeroValue, 7, 2, 1, 2)

        self.buttonZero = QPushButton(self.groupBox_3)
        self.buttonZero.setObjectName(u"buttonZero")
        self.buttonZero.setEnabled(False)

        self.gridLayout_4.addWidget(self.buttonZero, 7, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_11, 1, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 5, 1, 1, 1)

        self.checkbuttonLPF = QCheckBox(self.groupBox_3)
        self.checkbuttonLPF.setObjectName(u"checkbuttonLPF")
        self.checkbuttonLPF.setEnabled(False)
        self.checkbuttonLPF.setFont(font)
        self.checkbuttonLPF.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkbuttonLPF.setCheckable(True)

        self.gridLayout_4.addWidget(self.checkbuttonLPF, 3, 2, 1, 3)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(wMainWindow)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(319, 20, 811, 601))
        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 20, 151, 61))
        font1 = QFont()
        font1.setPointSize(50)
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(240, 250, 301, 131))
        font2 = QFont()
        font2.setPointSize(100)
        self.label_15.setFont(font2)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(570, 300, 151, 61))
        self.label_16.setFont(font1)

        self.retranslateUi(wMainWindow)

        QMetaObject.connectSlotsByName(wMainWindow)
    # setupUi

    def retranslateUi(self, wMainWindow):
        wMainWindow.setWindowTitle(QCoreApplication.translate("wMainWindow", u"Lyte Thorlabs PM100USB", None))
        self.groupBox.setTitle(QCoreApplication.translate("wMainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("wMainWindow", u"SN:", None))
        self.entrySN.setText(QCoreApplication.translate("wMainWindow", u"1924380", None))
        self.buttonInit.setText(QCoreApplication.translate("wMainWindow", u"Connect", None))
        self.labelConnectionMsg.setText(QCoreApplication.translate("wMainWindow", u"Enter SN and press Connect", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("wMainWindow", u"Sensor Info", None))
        self.label_3.setText(QCoreApplication.translate("wMainWindow", u"Model:", None))
        self.label_4.setText(QCoreApplication.translate("wMainWindow", u"SN:", None))
        self.label_5.setText(QCoreApplication.translate("wMainWindow", u"Cal msg:", None))
        self.label_6.setText(QCoreApplication.translate("wMainWindow", u"Type:", None))
        self.label_7.setText(QCoreApplication.translate("wMainWindow", u"Subtype:", None))
        self.label_8.setText(QCoreApplication.translate("wMainWindow", u"Flag:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("wMainWindow", u"Device", None))
        self.labelZeroUnit.setText(QCoreApplication.translate("wMainWindow", u"W", None))
        self.label_13.setText(QCoreApplication.translate("wMainWindow", u"Zero Adjust", None))
        self.label_10.setText(QCoreApplication.translate("wMainWindow", u"nm", None))
        self.entryWavelength.setText(QCoreApplication.translate("wMainWindow", u"1280", None))
        self.checkbuttonAutoRange.setText(QCoreApplication.translate("wMainWindow", u"Auto Range", u"0"))
        self.comboBoxUnits.setItemText(0, QCoreApplication.translate("wMainWindow", u"W", None))
        self.comboBoxUnits.setItemText(1, QCoreApplication.translate("wMainWindow", u"dBm", None))

        self.labelZeroValue.setText(QCoreApplication.translate("wMainWindow", u"0", None))
        self.buttonZero.setText(QCoreApplication.translate("wMainWindow", u"Zero", None))
        self.label_11.setText(QCoreApplication.translate("wMainWindow", u"Averaging:", None))
        self.label_9.setText(QCoreApplication.translate("wMainWindow", u"Wavelength:", None))
        self.label_12.setText(QCoreApplication.translate("wMainWindow", u"Units:", None))
        self.checkbuttonLPF.setText(QCoreApplication.translate("wMainWindow", u"Low Pass Filter", u"0"))
        self.groupBox_4.setTitle("")
        self.label_14.setText(QCoreApplication.translate("wMainWindow", u"Power", None))
        self.label_15.setText(QCoreApplication.translate("wMainWindow", u"--", None))
        self.label_16.setText(QCoreApplication.translate("wMainWindow", u"mW", None))
    # retranslateUi

