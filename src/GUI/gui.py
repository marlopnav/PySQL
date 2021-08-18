# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .icons_rc import *

class Ui_DBViewerWindow(object):
    def setupUi(self, DBViewerWindow):
        if not DBViewerWindow.objectName():
            DBViewerWindow.setObjectName(u"DBViewerWindow")
        DBViewerWindow.resize(515, 387)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DBViewerWindow.sizePolicy().hasHeightForWidth())
        DBViewerWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 101, 153, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 101, 153, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        DBViewerWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/icons/icons/Coreso.png", QSize(), QIcon.Normal, QIcon.Off)
        DBViewerWindow.setWindowIcon(icon)
        self.actionReload = QAction(DBViewerWindow)
        self.actionReload.setObjectName(u"actionReload")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReload.setIcon(icon1)
        self.actionSaveTable = QAction(DBViewerWindow)
        self.actionSaveTable.setObjectName(u"actionSaveTable")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveTable.setIcon(icon2)
        self.actionExportTable = QAction(DBViewerWindow)
        self.actionExportTable.setObjectName(u"actionExportTable")
        self.actionExportTable.setCheckable(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/ms-excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExportTable.setIcon(icon3)
        self.actionExportTable.setIconVisibleInMenu(True)
        self.centralwidget = QWidget(DBViewerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelStatus = QLabel(self.centralwidget)
        self.LabelStatus.setObjectName(u"LabelStatus")

        self.verticalLayout.addWidget(self.LabelStatus)

        self.ListTables = QListWidget(self.centralwidget)
        self.ListTables.setObjectName(u"ListTables")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ListTables.sizePolicy().hasHeightForWidth())
        self.ListTables.setSizePolicy(sizePolicy1)
        self.ListTables.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.ListTables)

        self.TableViewer = QTableWidget(self.centralwidget)
        self.TableViewer.setObjectName(u"TableViewer")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TableViewer.sizePolicy().hasHeightForWidth())
        self.TableViewer.setSizePolicy(sizePolicy2)
        self.TableViewer.verticalHeader().setVisible(False)
        self.TableViewer.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.TableViewer)

        DBViewerWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(DBViewerWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        DBViewerWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionReload)
        self.toolBar.addAction(self.actionSaveTable)
        self.toolBar.addAction(self.actionExportTable)

        self.retranslateUi(DBViewerWindow)

        QMetaObject.connectSlotsByName(DBViewerWindow)
    # setupUi

    def retranslateUi(self, DBViewerWindow):
        DBViewerWindow.setWindowTitle(QCoreApplication.translate("DBViewerWindow", u"Coreso SQLite Viewer", None))
        self.actionReload.setText(QCoreApplication.translate("DBViewerWindow", u"ReloadDB", None))
#if QT_CONFIG(tooltip)
        self.actionReload.setToolTip(QCoreApplication.translate("DBViewerWindow", u"Reload table and delete changes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionReload.setShortcut(QCoreApplication.translate("DBViewerWindow", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveTable.setText(QCoreApplication.translate("DBViewerWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSaveTable.setToolTip(QCoreApplication.translate("DBViewerWindow", u"Update table to DB", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSaveTable.setShortcut(QCoreApplication.translate("DBViewerWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionExportTable.setText(QCoreApplication.translate("DBViewerWindow", u"Export Excel", None))
#if QT_CONFIG(tooltip)
        self.actionExportTable.setToolTip(QCoreApplication.translate("DBViewerWindow", u"Export current table to Excel", None))
#endif // QT_CONFIG(tooltip)
        self.LabelStatus.setText("")
        self.toolBar.setWindowTitle(QCoreApplication.translate("DBViewerWindow", u"toolBar", None))
    # retranslateUi

