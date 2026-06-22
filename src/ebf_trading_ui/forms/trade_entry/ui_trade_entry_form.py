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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

from ebf_ui.widgets.custom.date_line_edit import DateLineEdit
from ebf_ui.widgets.custom.date_time_line_edit import DateTimeLineEdit
from ebf_ui.widgets.custom.int_line_edit import IntLineEdit
from ebf_ui.widgets.custom.money_line_edit import MoneyLineEdit

class Ui_tradeEntryDialog(object):
    def setupUi(self, tradeEntryDialog):
        if not tradeEntryDialog.objectName():
            tradeEntryDialog.setObjectName(u"tradeEntryDialog")
        tradeEntryDialog.resize(784, 425)
        self.verticalLayout = QVBoxLayout(tradeEntryDialog)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.tradeDetailsFrame = QFrame(tradeEntryDialog)
        self.tradeDetailsFrame.setObjectName(u"tradeDetailsFrame")
        self.tradeDetailsFrame.setMinimumSize(QSize(760, 240))
        self.tradeDetailsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tradeDetailsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.tradeDetailsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -10, 541, 43))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self.tradeDetailsFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 581, 244))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 7, 1, 1, 1)

        self.underlying = QLineEdit(self.layoutWidget)
        self.underlying.setObjectName(u"underlying")

        self.gridLayout.addWidget(self.underlying, 5, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 7, 2, 1, 1)

        self.premium = MoneyLineEdit(self.layoutWidget)
        self.premium.setObjectName(u"premium")
        self.premium.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.premium, 3, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)

        self.netAmount = MoneyLineEdit(self.layoutWidget)
        self.netAmount.setObjectName(u"netAmount")
        self.netAmount.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.netAmount.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.netAmount.setReadOnly(True)

        self.gridLayout.addWidget(self.netAmount, 3, 3, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.strike = MoneyLineEdit(self.layoutWidget)
        self.strike.setObjectName(u"strike")
        self.strike.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.strike, 5, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 7, 3, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 3, 1, 1)

        self.fees = MoneyLineEdit(self.layoutWidget)
        self.fees.setObjectName(u"fees")
        self.fees.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.fees, 3, 2, 1, 1)

        self.symbol = QLineEdit(self.layoutWidget)
        self.symbol.setObjectName(u"symbol")
        self.symbol.setEnabled(False)
        self.symbol.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.symbol, 5, 3, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 3, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        self.contracts = IntLineEdit(self.layoutWidget)
        self.contracts.setObjectName(u"contracts")
        self.contracts.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.contracts, 3, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)

        self.limitPrice = MoneyLineEdit(self.layoutWidget)
        self.limitPrice.setObjectName(u"limitPrice")
        self.limitPrice.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.limitPrice, 8, 0, 1, 1)

        self.tradeNarrative = QLineEdit(self.layoutWidget)
        self.tradeNarrative.setObjectName(u"tradeNarrative")
        self.tradeNarrative.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.gridLayout.addWidget(self.tradeNarrative, 6, 0, 1, 4)

        self.highOfDay = MoneyLineEdit(self.layoutWidget)
        self.highOfDay.setObjectName(u"highOfDay")
        self.highOfDay.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.highOfDay, 8, 1, 1, 1)

        self.lowOfDay = MoneyLineEdit(self.layoutWidget)
        self.lowOfDay.setObjectName(u"lowOfDay")
        self.lowOfDay.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lowOfDay, 8, 2, 1, 1)

        self.score = QLineEdit(self.layoutWidget)
        self.score.setObjectName(u"score")
        self.score.setEnabled(False)
        self.score.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.score.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.score, 8, 3, 1, 1)

        self.expiration = DateLineEdit(self.layoutWidget)
        self.expiration.setObjectName(u"expiration")

        self.gridLayout.addWidget(self.expiration, 5, 0, 1, 1)

        self.position = QComboBox(self.layoutWidget)
        self.position.setObjectName(u"position")

        self.gridLayout.addWidget(self.position, 1, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.action = QComboBox(self.layoutWidget)
        self.action.setObjectName(u"action")

        self.gridLayout.addWidget(self.action, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 2)

        self.fillTime = DateTimeLineEdit(self.layoutWidget)
        self.fillTime.setObjectName(u"fillTime")
        self.fillTime.setMaximumSize(QSize(281, 16777215))

        self.gridLayout.addWidget(self.fillTime, 1, 2, 1, 2)


        self.verticalLayout.addWidget(self.tradeDetailsFrame)

        self.saveButtonBox = QDialogButtonBox(tradeEntryDialog)
        self.saveButtonBox.setObjectName(u"saveButtonBox")
        self.saveButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.saveButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.saveButtonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.saveButtonBox)

        QWidget.setTabOrder(self.position, self.action)
        QWidget.setTabOrder(self.action, self.fillTime)
        QWidget.setTabOrder(self.fillTime, self.contracts)
        QWidget.setTabOrder(self.contracts, self.premium)
        QWidget.setTabOrder(self.premium, self.fees)
        QWidget.setTabOrder(self.fees, self.expiration)
        QWidget.setTabOrder(self.expiration, self.strike)
        QWidget.setTabOrder(self.strike, self.underlying)
        QWidget.setTabOrder(self.underlying, self.tradeNarrative)
        QWidget.setTabOrder(self.tradeNarrative, self.limitPrice)
        QWidget.setTabOrder(self.limitPrice, self.highOfDay)
        QWidget.setTabOrder(self.highOfDay, self.lowOfDay)
        QWidget.setTabOrder(self.lowOfDay, self.score)
        QWidget.setTabOrder(self.score, self.symbol)

        self.retranslateUi(tradeEntryDialog)
        self.saveButtonBox.accepted.connect(tradeEntryDialog.accept)
        self.saveButtonBox.rejected.connect(tradeEntryDialog.reject)

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
        self.position.setPlaceholderText(QCoreApplication.translate("tradeEntryDialog", u"Choose a position...", None))
        self.label_2.setText(QCoreApplication.translate("tradeEntryDialog", u"Position", None))
        self.label_3.setText(QCoreApplication.translate("tradeEntryDialog", u"Transaction", None))
        self.label_4.setText(QCoreApplication.translate("tradeEntryDialog", u"Fill Time", None))
    # retranslateUi

