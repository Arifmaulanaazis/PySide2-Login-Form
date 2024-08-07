
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets

from qframelesswindow import FramelessMainWindow


from qfluentwidgets import CheckBox
from qfluentwidgets import PushButton
from qfluentwidgets import HorizontalSeparator
from qfluentwidgets import TitleLabel
from qfluentwidgets import HyperlinkLabel
from qfluentwidgets import LineEdit
from qfluentwidgets import PasswordLineEdit


class Login_Window(FramelessMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Login")
        self.titleBar.raise_()
        self.setObjectName(u"Login-window")
        self.resize(840, 530)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Arial Rounded MT Bold")
        self.setFont(font)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        pixmap = QPixmap("image.jpg")
        rounded_pixmap = self.getRoundedLeftEdgePixmap(pixmap, 450, 550, 20)
        self.label.setPixmap(rounded_pixmap)

        self.label.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 0, 9, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(32, 32))
        self.label_2.setPixmap(QPixmap(u"mail.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.LineEdit = LineEdit(self.widget_3)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMaximumSize(QSize(16777215, 35))
        self.LineEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
        "    color: black;\n"
        "    background-color: rgba(255, 255, 255, 0.7);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 1); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-radius: 5px;\n"
        "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
        "    padding: 0px 10px;\n"
        "    selection-background-color: rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "}\n"
        "\n"
        "TextEdit,\n"
        "PlainTextEdit {\n"
        "    padding: 2px 3px 2px 8px;\n"
        "}\n"
        "\n"
        "LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
        "    background-color: rgba(249, 249, 249, 0.5);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 1); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "LineEdit:focus {\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    "
                                "background-color: white;\n"
        "}\n"
        "\n"
        "TextEdit:focus,\n"
        "PlainTextEdit:focus {\n"
        "    border-bottom: 1px solid rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "    background-color: white;\n"
        "}\n"
        "\n"
        "LineEdit:disabled, TextEdit:disabled,\n"
        "PlainTextEdit:disabled {\n"
        "    color: rgba(0, 0, 0, 150);\n"
        "    background-color: rgba(249, 249, 249, 0.3);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "#lineEditButton {\n"
        "    background-color: transparent;\n"
        "    border-radius: 4px;\n"
        "    margin: 0;\n"
        "}\n"
        "\n"
        "#lineEditButton:hover {\n"
        "    background-color: rgba(0, 37, 115, 0.09); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "#lineEditButton:pressed {\n"
        "    background-color: rgba(0, 37, 115, 0.06); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "")

        self.gridLayout_3.addWidget(self.LineEdit, 3, 1, 1, 3)

        self.HyperlinkLabel = HyperlinkLabel(self.widget_3)
        self.HyperlinkLabel.setObjectName(u"HyperlinkLabel")
        self.HyperlinkLabel.setStyleSheet(u"HyperlinkLabel {\n"
        "    color: rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "    text-align: left;\n"
        "    padding: 0;\n"
        "    margin: 0;\n"
        "}\n"
        "\n"
        "HyperlinkLabel[underline=true] {\n"
        "    text-decoration: underline;\n"
        "}\n"
        "\n"
        "HyperlinkLabel[underline=false] {\n"
        "    text-decoration: none;\n"
        "}\n"
        "\n"
        "HyperlinkLabel:hover {\n"
        "    color: rgb(0, 37, 115); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "HyperlinkLabel:pressed {\n"
        "    color: rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "}\n"
        "")

        self.gridLayout_3.addWidget(self.HyperlinkLabel, 10, 3, 1, 1)

        self.HorizontalSeparator = HorizontalSeparator(self.widget_3)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")
        self.HorizontalSeparator.setMaximumSize(QSize(16777215, 10))

        self.gridLayout_3.addWidget(self.HorizontalSeparator, 12, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 4)

        self.TitleLabel = TitleLabel(self.widget_3)
        self.TitleLabel.setObjectName(u"TitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy1)
        self.TitleLabel.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.TitleLabel, 1, 0, 1, 4, Qt.AlignHCenter)

        self.PushButton = PushButton(self.widget_3)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.PushButton.setFont(font1)
        self.PushButton.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
        "    color: white;\n"
        "    background: rgb(0, 123, 255);\n"
        "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
        "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
        "    border-radius: 10px;\n"
        "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
        "    padding: 5px 12px 6px 12px;\n"
        "    outline: none;\n"
        "}\n"
        "\n"
        "ToolButton {\n"
        "    padding: 5px 9px 6px 8px;\n"
        "}\n"
        "\n"
        "PushButton[hasIcon=false] {\n"
        "    padding: 5px 12px 6px 12px;\n"
        "}\n"
        "\n"
        "PushButton[hasIcon=true] {\n"
        "    padding: 5px 12px 6px 36px;\n"
        "}\n"
        "\n"
        "DropDownToolButton, PrimaryDropDownToolButton {\n"
        "    padding: 5px 31px 6px 8px;\n"
        "}\n"
        "\n"
        "DropDownPushButton[hasIcon=false],\n"
        "PrimaryDropDownPushButton[hasIcon=false] {\n"
        "    padding: 5px 31px 6px 12px;\n"
        "}\n"
        "\n"
        "DropDownPushButton[hasIcon=true],\n"
        "PrimaryDropDownPushButton[hasIcon=true] {\n"
        "    padding: 5px 31px 6px 36px;\n"
        "}\n"
        "\n"
        "PushButton:hover, ToolButton:hover, ToggleButton:hover, ToggleToo"
                                "lButton:hover {\n"
        "    background: rgb(0, 105, 217);\n"
        "}\n"
        "\n"
        "PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
        "    color:rgb(255, 255, 255);\n"
        "    background: rgb(0, 105, 217);\n"
        "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
        "	border: 1px solid rgb(0, 59, 129);\n"
        "}\n"
        "\n"
        "PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
        "    color: rgba(0, 0, 0, 0.36);\n"
        "    background: rgb(0, 105, 217);\n"
        "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
        "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
        "}\n"
        "\n"
        "\n"
        "PrimaryPushButton,\n"
        "PrimaryToolButton,\n"
        "ToggleButton:checked,\n"
        "ToggleToolButton:checked {\n"
        "    color: white;\n"
        "    background-color: #009faa;\n"
        "    border: 1px solid #00a7b3;\n"
        "    border-bottom: 1px solid #007780;\n"
        "}\n"
        "\n"
        "PrimaryPushButton:hover,\n"
        "PrimaryToolButton:hover,\n"
        "ToggleButton:checked:hover,\n"
        "ToggleToolButton:checked:hover {\n"
        "    background-color: "
                                "#00a7b3;\n"
        "    border: 1px solid #2daab3;\n"
        "    border-bottom: 1px solid #007780;\n"
        "}\n"
        "\n"
        "PrimaryPushButton:pressed,\n"
        "PrimaryToolButton:pressed,\n"
        "ToggleButton:checked:pressed,\n"
        "ToggleToolButton:checked:pressed {\n"
        "    color: rgba(255, 255, 255, 0.63);\n"
        "    background-color: #3eabb3;\n"
        "    border: 1px solid #3eabb3;\n"
        "}\n"
        "\n"
        "PrimaryPushButton:disabled,\n"
        "PrimaryToolButton:disabled,\n"
        "ToggleButton:checked:disabled,\n"
        "ToggleToolButton:checked:disabled {\n"
        "    color: rgba(255, 255, 255, 0.9);\n"
        "    background-color: rgb(205, 205, 205);\n"
        "    border: 1px solid rgb(205, 205, 205);\n"
        "}\n"
        "\n"
        "SplitDropButton,\n"
        "PrimarySplitDropButton {\n"
        "    border-left: none;\n"
        "    border-top-left-radius: 0;\n"
        "    border-bottom-left-radius: 0;\n"
        "}\n"
        "\n"
        "#splitPushButton,\n"
        "#splitToolButton,\n"
        "#primarySplitPushButton,\n"
        "#primarySplitToolButton {\n"
        "    border-top-right-radius: 0;\n"
        "    border-bottom-right-radius: 0;\n"
        "}\n"
        "\n"
        "#splitPushButton:pressed,\n"
        "#sp"
                                "litToolButton:pressed,\n"
        "SplitDropButton:pressed {\n"
        "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
        "}\n"
        "\n"
        "PrimarySplitDropButton:pressed {\n"
        "    border-bottom: 1px solid #007780;\n"
        "}\n"
        "\n"
        "#primarySplitPushButton, #primarySplitToolButton {\n"
        "    border-right: 1px solid #3eabb3;\n"
        "}\n"
        "\n"
        "#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
        "    border-bottom: 1px solid #007780;\n"
        "}\n"
        "\n"
        "HyperlinkButton {\n"
        "    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
        "    padding: 6px 12px 6px 12px;\n"
        "    color: #009faa;\n"
        "    border: none;\n"
        "    border-radius: 6px;\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        "HyperlinkButton[hasIcon=false] {\n"
        "    padding: 6px 12px 6px 12px;\n"
        "}\n"
        "\n"
        "HyperlinkButton[hasIcon=true] {\n"
        "    padding: 6px 12px 6px 36px;\n"
        "}\n"
        "\n"
        "HyperlinkButton:hover {\n"
        "    color: #009faa;\n"
        "    background-color: rgba(0, 0, 0, 10);\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "HyperlinkButton:pressed {\n"
        "    color: #009f"
                                "aa;\n"
        "    background-color: rgba(0, 0, 0, 6);\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "HyperlinkButton:disabled {\n"
        "    color: rgba(0, 0, 0, 0.43);\n"
        "    background-color: transparent;\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "\n"
        "RadioButton {\n"
        "    min-height: 24px;\n"
        "    max-height: 24px;\n"
        "    background-color: transparent;\n"
        "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
        "    color: black;\n"
        "}\n"
        "\n"
        "RadioButton::indicator {\n"
        "    width: 18px;\n"
        "    height: 18px;\n"
        "    border-radius: 11px;\n"
        "    border: 2px solid #999999;\n"
        "    background-color: rgba(0, 0, 0, 5);\n"
        "    margin-right: 4px;\n"
        "}\n"
        "\n"
        "RadioButton::indicator:hover {\n"
        "    background-color: rgba(0, 0, 0, 0);\n"
        "}\n"
        "\n"
        "RadioButton::indicator:pressed {\n"
        "    border: 2px solid #bbbbbb;\n"
        "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
        "            stop:0 rgb(255, 255, 255),\n"
        "            stop:0.5 rgb(255, 255, 255),\n"
        "            stop:0.6 rg"
                                "b(225, 224, 223),\n"
        "            stop:1 rgb(225, 224, 223));\n"
        "}\n"
        "\n"
        "RadioButton::indicator:checked {\n"
        "    height: 22px;\n"
        "    width: 22px;\n"
        "    border: none;\n"
        "    border-radius: 11px;\n"
        "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
        "            stop:0 rgb(255, 255, 255),\n"
        "            stop:0.5 rgb(255, 255, 255),\n"
        "            stop:0.6 #009faa,\n"
        "            stop:1 #009faa);\n"
        "}\n"
        "\n"
        "RadioButton::indicator:checked:hover {\n"
        "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
        "            stop:0 rgb(255, 255, 255),\n"
        "            stop:0.6 rgb(255, 255, 255),\n"
        "            stop:0.7 #009faa,\n"
        "            stop:1 #009faa);\n"
        "}\n"
        "\n"
        "RadioButton::indicator:checked:pressed {\n"
        "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
        "            stop:0 rgb(255, 255, 255),\n"
        "            stop:0.5 rgb(255, 255, 255),\n"
        "            sto"
                                "p:0.6 #009faa,\n"
        "            stop:1 #009faa);\n"
        "}\n"
        "\n"
        "RadioButton:disabled {\n"
        "    color: rgba(0, 0, 0, 110);\n"
        "}\n"
        "\n"
        "RadioButton::indicator:disabled {\n"
        "    border: 2px solid #bbbbbb;\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        "RadioButton::indicator:disabled:checked {\n"
        "    border: none;\n"
        "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
        "            stop:0 rgb(255, 255, 255),\n"
        "            stop:0.5 rgb(255, 255, 255),\n"
        "            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
        "            stop:1 rgba(0, 0, 0, 0.2169));\n"
        "}\n"
        "\n"
        "TransparentToolButton,\n"
        "TransparentToggleToolButton,\n"
        "TransparentDropDownToolButton,\n"
        "TransparentPushButton,\n"
        "TransparentDropDownPushButton,\n"
        "TransparentTogglePushButton {\n"
        "    background-color: transparent;\n"
        "    border: none;\n"
        "    border-radius: 5px;\n"
        "    margin: 0;\n"
        "}\n"
        "\n"
        "TransparentToolButton:hover,\n"
        "TransparentToggleToolButton:hover,\n"
        "TransparentDropDownToolB"
                                "utton:hover,\n"
        "TransparentPushButton:hover,\n"
        "TransparentDropDownPushButton:hover,\n"
        "TransparentTogglePushButton:hover {\n"
        "    background-color: rgba(0, 0, 0, 9);\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "TransparentToolButton:pressed,\n"
        "TransparentToggleToolButton:pressed,\n"
        "TransparentDropDownToolButton:pressed,\n"
        "TransparentPushButton:pressed,\n"
        "TransparentDropDownPushButton:pressed,\n"
        "TransparentTogglePushButton:pressed {\n"
        "    background-color: rgba(0, 0, 0, 6);\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "TransparentToolButton:disabled,\n"
        "TransparentToggleToolButton:disabled,\n"
        "TransparentDropDownToolButton:disabled,\n"
        "TransprentPushButton:disabled,\n"
        "TransparentDropDownPushButton:disabled,\n"
        "TransprentTogglePushButton:disabled {\n"
        "    background-color: transparent;\n"
        "    border: none;\n"
        "}\n"
        "\n"
        "\n"
        "PillPushButton,\n"
        "PillPushButton:hover,\n"
        "PillPushButton:pressed,\n"
        "PillPushButton:disabled,\n"
        "PillPushButton:checked,\n"
        "PillPushButton:checked:hover,\n"
        "PillPushButton:c"
                                "hecked:pressed,\n"
        "PillPushButton:disabled:checked,\n"
        "PillToolButton,\n"
        "PillToolButton:hover,\n"
        "PillToolButton:pressed,\n"
        "PillToolButton:disabled,\n"
        "PillToolButton:checked,\n"
        "PillToolButton:checked:hover,\n"
        "PillToolButton:checked:pressed,\n"
        "PillToolButton:disabled:checked {\n"
        "    background-color: transparent;\n"
        "    border: none;\n"
        "}\n"
        "")

        self.gridLayout_3.addWidget(self.PushButton, 7, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 4)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.HyperlinkLabel_2 = HyperlinkLabel(self.widget_4)
        self.HyperlinkLabel_2.setObjectName(u"HyperlinkLabel_2")
        self.HyperlinkLabel_2.setStyleSheet(u"HyperlinkLabel {\n"
        "    color: rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "    border: none;\n"
        "    background-color: transparent;\n"
        "    text-align: left;\n"
        "    padding: 0;\n"
        "    margin: 0;\n"
        "}\n"
        "\n"
        "HyperlinkLabel[underline=true] {\n"
        "    text-decoration: underline;\n"
        "}\n"
        "\n"
        "HyperlinkLabel[underline=false] {\n"
        "    text-decoration: none;\n"
        "}\n"
        "\n"
        "HyperlinkLabel:hover {\n"
        "    color: rgb(0, 37, 115); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "HyperlinkLabel:pressed {\n"
        "    color: rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "}\n"
        "")

        self.gridLayout_4.addWidget(self.HyperlinkLabel_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 13, 0, 1, 4, Qt.AlignHCenter)

        self.CheckBox = CheckBox(self.widget_3)
        self.CheckBox.setObjectName(u"CheckBox")
        self.CheckBox.setStyleSheet(u"CheckBox {\n"
        "    color: black;\n"
        "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
        "    spacing: 8px;\n"
        "    min-width: 28px;\n"
        "    min-height: 22px;\n"
        "    outline: none;\n"
        "    margin-left: 1px;\n"
        "}\n"
        "\n"
        "CheckBox::indicator {\n"
        "    width: 18px;\n"
        "    height: 18px;\n"
        "    border-radius: 5px;\n"
        "    border: 1px solid rgba(0, 37, 115, 0.48); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    background-color: rgba(0, 37, 115, 0.022); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "CheckBox::indicator:hover {\n"
        "    border: 1px solid rgba(0, 37, 115, 0.56); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    background-color: rgba(0, 37, 115, 0.05); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "CheckBox::indicator:pressed {\n"
        "    border: 1px solid rgba(0, 37, 115, 0.27); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    background-color: rgba(0, 37, 115, 0.12); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "CheckBox::indicator:checked,\n"
        "CheckBox::indicator:"
                                "indeterminate {\n"
        "    border: 1px solid rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "    background-color: rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "}\n"
        "\n"
        "CheckBox::indicator:checked:hover,\n"
        "CheckBox::indicator:indeterminate:hover {\n"
        "    border: 1px solid rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "    background-color: rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "}\n"
        "\n"
        "CheckBox::indicator:checked:pressed,\n"
        "CheckBox::indicator:indeterminate:pressed {\n"
        "    border: 1px solid rgb(0, 37, 115); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    background-color: rgb(0, 37, 115); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "CheckBox:disabled {\n"
        "    color: rgba(0, 0, 0, 110);\n"
        "}\n"
        "\n"
        "CheckBox::indicator:disabled {\n"
        "    border: 1px solid rgba(0, 0, 0, 0.27);\n"
        "    background-color: transparent;\n"
        "}\n"
        "\n"
        "CheckBox::indicator:checked:disabled,\n"
        "CheckBox::indicator:indeterminate:disabled {\n"
        ""
                                "    border: 1px solid rgb(199, 199, 199);\n"
        "    background-color: rgb(199, 199, 199);\n"
        "}\n"
        "")

        self.gridLayout_3.addWidget(self.CheckBox, 6, 1, 1, 3)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(32, 32))
        self.label_3.setPixmap(QPixmap(u"key.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.PasswordLineEdit = PasswordLineEdit(self.widget_3)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setMaximumSize(QSize(16777215, 35))
        self.PasswordLineEdit.setStyleSheet(u"LineEdit, TextEdit, PlainTextEdit {\n"
        "    color: black;\n"
        "    background-color: rgba(255, 255, 255, 0.7);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 1); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-radius: 5px;\n"
        "    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
        "    padding: 0px 10px;\n"
        "    selection-background-color: rgb(0, 123, 255); /* Menggunakan warna rgb(0, 123, 255) */\n"
        "}\n"
        "\n"
        "TextEdit,\n"
        "PlainTextEdit {\n"
        "    padding: 2px 3px 2px 8px;\n"
        "}\n"
        "\n"
        "LineEdit:hover, TextEdit:hover, PlainTextEdit:hover {\n"
        "    background-color: rgba(249, 249, 249, 0.5);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 1); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "LineEdit:focus {\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    "
                                "background-color: white;\n"
        "}\n"
        "\n"
        "TextEdit:focus,\n"
        "PlainTextEdit:focus {\n"
        "    border-bottom: 1px solid rgb(0, 105, 218); /* Menggunakan warna rgb(0, 105, 218) */\n"
        "    background-color: white;\n"
        "}\n"
        "\n"
        "LineEdit:disabled, TextEdit:disabled,\n"
        "PlainTextEdit:disabled {\n"
        "    color: rgba(0, 0, 0, 150);\n"
        "    background-color: rgba(249, 249, 249, 0.3);\n"
        "    border: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "    border-bottom: 1px solid rgba(0, 37, 115, 0.13); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "#lineEditButton {\n"
        "    background-color: transparent;\n"
        "    border-radius: 4px;\n"
        "    margin: 0;\n"
        "}\n"
        "\n"
        "#lineEditButton:hover {\n"
        "    background-color: rgba(0, 37, 115, 0.09); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "\n"
        "#lineEditButton:pressed {\n"
        "    background-color: rgba(0, 37, 115, 0.06); /* Menggunakan warna rgb(0, 37, 115) */\n"
        "}\n"
        "")

        self.gridLayout_3.addWidget(self.PasswordLineEdit, 5, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer, 11, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 0, 1, 4)


        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)


        self.label.setText("")
        self.label_2.setText("")
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("self", u"Email Address", None))
        self.HyperlinkLabel.setText(QCoreApplication.translate("self", u"Forget Password?", None))
        self.TitleLabel.setText(QCoreApplication.translate("self", u"Login into account", None))
        self.PushButton.setText(QCoreApplication.translate("self", u"LOGIN", None))
        self.label_4.setText(QCoreApplication.translate("self", u"Don't have an account? ", None))
        self.HyperlinkLabel_2.setText(QCoreApplication.translate("self", u"Register here", None))
        self.CheckBox.setText(QCoreApplication.translate("self", u"Remember me", None))
        self.label_3.setText("")
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("self", u"Password", None))

        QMetaObject.connectSlotsByName(self)

        self._is_dragging = False
        self._drag_start_position = QPoint(0, 0)


    def getRoundedLeftEdgePixmap(self, pixmap, width, height, radius):
        rounded_pixmap = QtGui.QPixmap(width, height)
        rounded_pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(rounded_pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        path = QtGui.QPainterPath()

        path.moveTo(radius, 0)
        path.arcTo(0, 0, 2*radius, 2*radius, 90, 90) 
        path.lineTo(0, height - radius)
        path.arcTo(0, height - 2*radius, 2*radius, 2*radius, 180, 90)
        path.lineTo(width, height)
        path.lineTo(width, 0)
        path.closeSubpath()

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation))
        painter.end()

        return rounded_pixmap


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            offset = event.pos() - self._drag_start_position
            new_position = self.pos() + offset
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False


    



#runing
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    demo = Login_Window()
    demo.show()
    sys.exit(app.exec_())