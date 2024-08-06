# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(515, 307)
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbOK = QPushButton(w_LoginForm)
        self.pbOK.setObjectName(u"pbOK")

        self.gridLayout.addWidget(self.pbOK, 2, 0, 1, 1)

        self.pbCancel = QPushButton(w_LoginForm)
        self.pbCancel.setObjectName(u"pbCancel")

        self.gridLayout.addWidget(self.pbCancel, 2, 1, 1, 1)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.leUserID = QLineEdit(self.groupBox)
        self.leUserID.setObjectName(u"leUserID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leUserID)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lePassword = QLineEdit(self.groupBox)
        self.lePassword.setObjectName(u"lePassword")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lePassword)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.lbMessage = QLabel(w_LoginForm)
        self.lbMessage.setObjectName(u"lbMessage")

        self.gridLayout.addWidget(self.lbMessage, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)


        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Sample Application", None))
        self.pbOK.setText(QCoreApplication.translate("w_LoginForm", u"Ok", None))
        self.pbCancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Welcome! Please Login", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"Password", None))
        self.lbMessage.setText(QCoreApplication.translate("w_LoginForm", u"Message", None))
    # retranslateUi

