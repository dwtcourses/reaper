# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 699)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStatusTip("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.introTab = QtWidgets.QWidget()
        self.introTab.setEnabled(True)
        self.introTab.setObjectName("introTab")
        self.gridLayout = QtWidgets.QGridLayout(self.introTab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_19 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_6.addWidget(self.label_19)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.introTab)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.introTab)
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setOpenExternalLinks(True)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 7, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_22 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_10.addWidget(self.label_22)
        self.label_38 = QtWidgets.QLabel(self.introTab)
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_10.addWidget(self.label_38)
        self.label_23 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_10.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_10.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.introTab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_10.addWidget(self.label_27)
        self.horizontalLayout_12.addLayout(self.verticalLayout_10)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)
        self.tabWidget.addTab(self.introTab, "")
        self.keyTab = QtWidgets.QWidget()
        self.keyTab.setStyleSheet("")
        self.keyTab.setObjectName("keyTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.keyTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_42 = QtWidgets.QLabel(self.keyTab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_2.addWidget(self.label_42)
        self.scrollArea = QtWidgets.QScrollArea(self.keyTab)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet("QAbstractScrollArea\n"
"{\n"
"background-color: transparent;\n"
"}\n"
"QWidget#scrollAreaWidgetContents{\n"
"background-color: transparent; /*or a colour*/\n"
"} ")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1038, 575))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.keyTab, "")
        self.sourceTab = QtWidgets.QWidget()
        self.sourceTab.setStyleSheet("")
        self.sourceTab.setObjectName("sourceTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sourceTab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.sourceTab)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.sourceTab)
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.sourcesTabs = QtWidgets.QTabWidget(self.sourceTab)
        self.sourcesTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.sourcesTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.sourcesTabs.setElideMode(QtCore.Qt.ElideNone)
        self.sourcesTabs.setUsesScrollButtons(True)
        self.sourcesTabs.setTabsClosable(False)
        self.sourcesTabs.setTabBarAutoHide(False)
        self.sourcesTabs.setObjectName("sourcesTabs")
        self.verticalLayout_8.addWidget(self.sourcesTabs)
        self.tabWidget.addTab(self.sourceTab, "")
        self.queueTab = QtWidgets.QWidget()
        self.queueTab.setObjectName("queueTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.queueTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.queueLayout = QtWidgets.QHBoxLayout()
        self.queueLayout.setObjectName("queueLayout")
        self.queueTools = QtWidgets.QVBoxLayout()
        self.queueTools.setObjectName("queueTools")
        self.queueUp = QtWidgets.QToolButton(self.queueTab)
        self.queueUp.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.queueUp.setIcon(icon)
        self.queueUp.setObjectName("queueUp")
        self.queueTools.addWidget(self.queueUp)
        self.queueDown = QtWidgets.QToolButton(self.queueTab)
        self.queueDown.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.queueDown.setIcon(icon1)
        self.queueDown.setObjectName("queueDown")
        self.queueTools.addWidget(self.queueDown)
        self.queueRemove = QtWidgets.QToolButton(self.queueTab)
        self.queueRemove.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.queueRemove.setIcon(icon2)
        self.queueRemove.setObjectName("queueRemove")
        self.queueTools.addWidget(self.queueRemove)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.queueTools.addItem(spacerItem5)
        self.queueLayout.addLayout(self.queueTools)
        self.verticalLayout.addLayout(self.queueLayout)
        self.label_29 = QtWidgets.QLabel(self.queueTab)
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.queueStart = QtWidgets.QPushButton(self.queueTab)
        self.queueStart.setObjectName("queueStart")
        self.horizontalLayout_2.addWidget(self.queueStart)
        self.queueStop = QtWidgets.QPushButton(self.queueTab)
        self.queueStop.setObjectName("queueStop")
        self.horizontalLayout_2.addWidget(self.queueStop)
        self.queueClear = QtWidgets.QPushButton(self.queueTab)
        self.queueClear.setObjectName("queueClear")
        self.horizontalLayout_2.addWidget(self.queueClear)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.queueSave = QtWidgets.QPushButton(self.queueTab)
        self.queueSave.setEnabled(False)
        self.queueSave.setObjectName("queueSave")
        self.horizontalLayout_2.addWidget(self.queueSave)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.queueTab, "")
        self.progressTab = QtWidgets.QWidget()
        self.progressTab.setObjectName("progressTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.progressTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.progressLayout = QtWidgets.QVBoxLayout()
        self.progressLayout.setObjectName("progressLayout")
        self.verticalLayout_6.addLayout(self.progressLayout)
        self.tabWidget.addTab(self.progressTab, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setEnabled(False)
        self.menuOpen.setObjectName("menuOpen")
        self.menuBackups = QtWidgets.QMenu(self.menuOpen)
        self.menuBackups.setObjectName("menuBackups")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setEnabled(False)
        self.menuSave.setObjectName("menuSave")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAPI_Key_file = QtWidgets.QAction(MainWindow)
        self.actionAPI_Key_file.setObjectName("actionAPI_Key_file")
        self.actionScraping_state = QtWidgets.QAction(MainWindow)
        self.actionScraping_state.setObjectName("actionScraping_state")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicenses = QtWidgets.QAction(MainWindow)
        self.actionLicenses.setObjectName("actionLicenses")
        self.actionAPI_Keys = QtWidgets.QAction(MainWindow)
        self.actionAPI_Keys.setObjectName("actionAPI_Keys")
        self.actionJob_Queue = QtWidgets.QAction(MainWindow)
        self.actionJob_Queue.setObjectName("actionJob_Queue")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setEnabled(False)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionReport_a_bug = QtWidgets.QAction(MainWindow)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionScraping = QtWidgets.QAction(MainWindow)
        self.actionScraping.setCheckable(True)
        self.actionScraping.setChecked(True)
        self.actionScraping.setObjectName("actionScraping")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setCheckable(True)
        self.actionHistory.setObjectName("actionHistory")
        self.actionHistory_2 = QtWidgets.QAction(MainWindow)
        self.actionHistory_2.setEnabled(False)
        self.actionHistory_2.setObjectName("actionHistory_2")
        self.actionAPI_Key_Database = QtWidgets.QAction(MainWindow)
        self.actionAPI_Key_Database.setEnabled(False)
        self.actionAPI_Key_Database.setObjectName("actionAPI_Key_Database")
        self.actionAdvanced_mode = QtWidgets.QAction(MainWindow)
        self.actionAdvanced_mode.setCheckable(True)
        self.actionAdvanced_mode.setObjectName("actionAdvanced_mode")
        self.actionWebsite = QtWidgets.QAction(MainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionQueue = QtWidgets.QAction(MainWindow)
        self.actionQueue.setObjectName("actionQueue")
        self.actionJob = QtWidgets.QAction(MainWindow)
        self.actionJob.setObjectName("actionJob")
        self.actionDark_mode = QtWidgets.QAction(MainWindow)
        self.actionDark_mode.setCheckable(True)
        self.actionDark_mode.setObjectName("actionDark_mode")
        self.menuBackups.addAction(self.actionQueue)
        self.menuBackups.addAction(self.actionJob)
        self.menuOpen.addAction(self.actionAPI_Key_file)
        self.menuOpen.addAction(self.actionJob_Queue)
        self.menuOpen.addAction(self.actionScraping_state)
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.menuBackups.menuAction())
        self.menuSave.addAction(self.actionAPI_Keys)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicenses)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionWebsite)
        self.menuView.addAction(self.actionHistory_2)
        self.menuView.addAction(self.actionAPI_Key_Database)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAdvanced_mode)
        self.menuView.addAction(self.actionDark_mode)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.sourcesTabs.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reaper"))
        MainWindow.setStatusTip(_translate("MainWindow", "Visit https://reaper.social for help & tutorials"))
        self.label_19.setText(_translate("MainWindow", "Welcome to Reaper!"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p>© The University of Queensland</p><p>Developed by <a href=\"https://github.com/ScriptSmith\"><span style=\" text-decoration: underline; color:#0000ff;\">Adam Smith</span></a></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "Reaper helps you gather social media data, no coding required."))
        self.label_23.setText(_translate("MainWindow", "Simply:"))
        self.label_24.setText(_translate("MainWindow", "1. Add & verify your API Keys"))
        self.label_25.setText(_translate("MainWindow", "2. Input your parameters"))
        self.label_26.setText(_translate("MainWindow", "3. Add your scraping instruction to the queue"))
        self.label_27.setText(_translate("MainWindow", "4. Download your data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.introTab), _translate("MainWindow", "0. Introduction"))
        self.label_42.setText(_translate("MainWindow", "By using these platforms, you are agreeing to their terms & conditions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.keyTab), _translate("MainWindow", "1. API Keys"))
        self.label_14.setText(_translate("MainWindow", "Select the source that you want to scrape from"))
        self.label_15.setText(_translate("MainWindow", "Double-click a node to see and select its edges"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sourceTab), _translate("MainWindow", "2. Sources"))
        self.queueUp.setText(_translate("MainWindow", "..."))
        self.queueDown.setText(_translate("MainWindow", "..."))
        self.queueRemove.setText(_translate("MainWindow", "..."))
        self.label_29.setText(_translate("MainWindow", "Queue Controls"))
        self.queueStart.setText(_translate("MainWindow", "Start"))
        self.queueStop.setText(_translate("MainWindow", "Stop"))
        self.queueClear.setText(_translate("MainWindow", "Clear"))
        self.queueSave.setText(_translate("MainWindow", "Save Queue to file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queueTab), _translate("MainWindow", "3. Job Queue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.progressTab), _translate("MainWindow", "4. Current Job"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.menuBackups.setTitle(_translate("MainWindow", "Backups"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAPI_Key_file.setText(_translate("MainWindow", "API Keys"))
        self.actionScraping_state.setText(_translate("MainWindow", "Scraping state"))
        self.actionAbout.setText(_translate("MainWindow", "About Reaper"))
        self.actionLicenses.setText(_translate("MainWindow", "Licenses"))
        self.actionAPI_Keys.setText(_translate("MainWindow", "API Keys"))
        self.actionJob_Queue.setText(_translate("MainWindow", "Job Queue"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionReport_a_bug.setText(_translate("MainWindow", "Report a bug"))
        self.actionScraping.setText(_translate("MainWindow", "Scraping"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionHistory_2.setText(_translate("MainWindow", "History"))
        self.actionAPI_Key_Database.setText(_translate("MainWindow", "API Key Database"))
        self.actionAdvanced_mode.setText(_translate("MainWindow", "Advanced mode"))
        self.actionWebsite.setText(_translate("MainWindow", "Website"))
        self.actionQueue.setText(_translate("MainWindow", "Queue"))
        self.actionJob.setText(_translate("MainWindow", "Job"))
        self.actionDark_mode.setText(_translate("MainWindow", "Dark mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

