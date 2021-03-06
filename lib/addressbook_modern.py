# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/addressbook_modern.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout.addWidget(self.treeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuF_le = QtWidgets.QMenu(self.menubar)
        self.menuF_le.setObjectName("menuF_le")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd_Contact = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Add Contact/contact-new-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Contact.setIcon(icon)
        self.actionAdd_Contact.setObjectName("actionAdd_Contact")
        self.actionImport_Contacts = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Import Contacts/address-book-new-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_Contacts.setIcon(icon1)
        self.actionImport_Contacts.setObjectName("actionImport_Contacts")
        self.actionExport_Contacts = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Export/document-send-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_Contacts.setIcon(icon2)
        self.actionExport_Contacts.setObjectName("actionExport_Contacts")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Exit/window-close-symbolic.symbolic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon3)
        self.actionClose.setObjectName("actionClose")
        self.menuF_le.addAction(self.actionAdd_Contact)
        self.menuF_le.addAction(self.actionImport_Contacts)
        self.menuF_le.addAction(self.actionExport_Contacts)
        self.menuF_le.addAction(self.actionClose)
        self.menubar.addAction(self.menuF_le.menuAction())
        self.toolBar.addAction(self.actionAdd_Contact)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionImport_Contacts)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExport_Contacts)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", " Email Address"))
        self.menuF_le.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAdd_Contact.setText(_translate("MainWindow", "Add Contact"))
        self.actionImport_Contacts.setText(_translate("MainWindow", "Import Contacts"))
        self.actionExport_Contacts.setText(_translate("MainWindow", "Export Contacts"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
import resources_rc
