# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trade_entry_form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QSizePolicy, QTimeEdit,
    QWidget)

class Ui_tradeEntryDialog(object):
    def setupUi(self, tradeEntryDialog):
        if not tradeEntryDialog.objectName():
            tradeEntryDialog.setObjectName(u"tradeEntryDialog")
        tradeEntryDialog.resize(638, 425)
        self.buttonBox = QDialogButtonBox(tradeEntryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(250, 360, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.tradeDetailsFrame = QFrame(tradeEntryDialog)
        self.tradeDetailsFrame.setObjectName(u"tradeDetailsFrame")
        self.tradeDetailsFrame.setGeometry(QRect(20, 10, 760, 291))
        self.tradeDetailsFrame.setMinimumSize(QSize(760, 240))
        self.tradeDetailsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tradeDetailsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.tradeDetailsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, -10, 457, 43))
        self.widget = QWidget(self.tradeDetailsFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 581, 244))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 7, 1, 1, 1)

        self.underlying = QLineEdit(self.widget)
        self.underlying.setObjectName(u"underlying")

        self.gridLayout.addWidget(self.underlying, 5, 2, 1, 1)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 2, 1, 1)

        self.premium = QLineEdit(self.widget)
        self.premium.setObjectName(u"premium")

        self.gridLayout.addWidget(self.premium, 3, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)

        self.netAmount = QLineEdit(self.widget)
        self.netAmount.setObjectName(u"netAmount")

        self.gridLayout.addWidget(self.netAmount, 3, 3, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.strike = QLineEdit(self.widget)
        self.strike.setObjectName(u"strike")

        self.gridLayout.addWidget(self.strike, 5, 1, 1, 1)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 7, 3, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 1)

        self.fees = QLineEdit(self.widget)
        self.fees.setObjectName(u"fees")

        self.gridLayout.addWidget(self.fees, 3, 2, 1, 1)

        self.symbol = QLineEdit(self.widget)
        self.symbol.setObjectName(u"symbol")

        self.gridLayout.addWidget(self.symbol, 5, 3, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 3, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        self.contracts = QLineEdit(self.widget)
        self.contracts.setObjectName(u"contracts")

        self.gridLayout.addWidget(self.contracts, 3, 0, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)

        self.dateEdit_2 = QDateEdit(self.widget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.gridLayout.addWidget(self.dateEdit_2, 5, 0, 1, 1)

        self.limitPrice = QLineEdit(self.widget)
        self.limitPrice.setObjectName(u"limitPrice")

        self.gridLayout.addWidget(self.limitPrice, 8, 0, 1, 1)

        self.tradeNarrative = QLineEdit(self.widget)
        self.tradeNarrative.setObjectName(u"tradeNarrative")

        self.gridLayout.addWidget(self.tradeNarrative, 6, 0, 1, 4)

        self.timeEdit = QTimeEdit(self.widget)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 1, 3, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.position = QComboBox(self.widget)
        self.position.setObjectName(u"position")

        self.gridLayout.addWidget(self.position, 1, 0, 1, 2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)

        self.highOfDay = QLineEdit(self.widget)
        self.highOfDay.setObjectName(u"highOfDay")

        self.gridLayout.addWidget(self.highOfDay, 8, 1, 1, 1)

        self.lowOfDay = QLineEdit(self.widget)
        self.lowOfDay.setObjectName(u"lowOfDay")

        self.gridLayout.addWidget(self.lowOfDay, 8, 2, 1, 1)

        self.score = QLineEdit(self.widget)
        self.score.setObjectName(u"score")

        self.gridLayout.addWidget(self.score, 8, 3, 1, 1)


        self.retranslateUi(tradeEntryDialog)
        self.buttonBox.accepted.connect(tradeEntryDialog.accept)
        self.buttonBox.rejected.connect(tradeEntryDialog.reject)

        QMetaObject.connectSlotsByName(tradeEntryDialog)
    # setupUi

    def retranslateUi(self, tradeEntryDialog):
        tradeEntryDialog.setWindowTitle(QCoreApplication.translate("tradeEntryDialog", u"Dialog", None))
#if QT_CONFIG(accessibility)
        self.tradeDetailsFrame.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("tradeEntryDialog", u"Trade Details", None))
        self.label_5.setText(QCoreApplication.translate("tradeEntryDialog", u"Expiration", None))
        self.label_14.setText(QCoreApplication.translate("tradeEntryDialog", u"High of Day", None))
        self.label_15.setText(QCoreApplication.translate("tradeEntryDialog", u"Low of Day", None))
        self.label_6.setText(QCoreApplication.translate("tradeEntryDialog", u"Strike", None))
        self.label_9.setText(QCoreApplication.translate("tradeEntryDialog", u"Contracts", None))
        self.label_10.setText(QCoreApplication.translate("tradeEntryDialog", u"Premium", None))
        self.label_13.setText(QCoreApplication.translate("tradeEntryDialog", u"Limit Price", None))
        self.label_16.setText(QCoreApplication.translate("tradeEntryDialog", u"Score", None))
        self.label_7.setText(QCoreApplication.translate("tradeEntryDialog", u"Symbol", None))
        self.label_12.setText(QCoreApplication.translate("tradeEntryDialog", u"Net Amount", None))
        self.label_11.setText(QCoreApplication.translate("tradeEntryDialog", u"Fees", None))
        self.label_8.setText(QCoreApplication.translate("tradeEntryDialog", u"Underlying", None))
        self.label_4.setText(QCoreApplication.translate("tradeEntryDialog", u"Time", None))
        self.label_3.setText(QCoreApplication.translate("tradeEntryDialog", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("tradeEntryDialog", u"Position", None))
    # retranslateUi

