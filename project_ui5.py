# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created: Fri Jul  8 09:59:28 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgProject(object):
    def setupUi(self, dlgProject):
        dlgProject.setObjectName("dlgProject")
        dlgProject.resize(987, 578)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(dlgProject)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabProject = QtWidgets.QTabWidget(dlgProject)
        self.tabProject.setObjectName("tabProject")
        self.tabInformation = QtWidgets.QWidget()
        self.tabInformation.setObjectName("tabInformation")
        self.formLayout = QtWidgets.QFormLayout(self.tabInformation)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tabInformation)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.leProjectName = QtWidgets.QLineEdit(self.tabInformation)
        self.leProjectName.setObjectName("leProjectName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leProjectName)
        self.lbProjectFilePath = QtWidgets.QLabel(self.tabInformation)
        self.lbProjectFilePath.setObjectName("lbProjectFilePath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lbProjectFilePath)
        self.label_7 = QtWidgets.QLabel(self.tabInformation)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.dteDate = QtWidgets.QDateTimeEdit(self.tabInformation)
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName("dteDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dteDate)
        self.label_6 = QtWidgets.QLabel(self.tabInformation)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.teDescription = QtWidgets.QPlainTextEdit(self.tabInformation)
        self.teDescription.setObjectName("teDescription")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.teDescription)
        self.lbTimeFormat = QtWidgets.QLabel(self.tabInformation)
        self.lbTimeFormat.setObjectName("lbTimeFormat")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.lbTimeFormat)
        self.rbSeconds = QtWidgets.QRadioButton(self.tabInformation)
        self.rbSeconds.setChecked(True)
        self.rbSeconds.setObjectName("rbSeconds")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rbSeconds)
        self.rbHMS = QtWidgets.QRadioButton(self.tabInformation)
        self.rbHMS.setObjectName("rbHMS")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.rbHMS)
        self.tabProject.addTab(self.tabInformation, "")
        self.tabConfiguration = QtWidgets.QWidget()
        self.tabConfiguration.setObjectName("tabConfiguration")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabConfiguration)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.twBehaviors = QtWidgets.QTableWidget(self.tabConfiguration)
        self.twBehaviors.setAutoFillBackground(False)
        self.twBehaviors.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twBehaviors.setMidLineWidth(0)
        self.twBehaviors.setAlternatingRowColors(True)
        self.twBehaviors.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twBehaviors.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twBehaviors.setObjectName("twBehaviors")
        self.twBehaviors.setColumnCount(8)
        self.twBehaviors.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(7, item)
        self.twBehaviors.horizontalHeader().setSortIndicatorShown(True)
        self.twBehaviors.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_11.addWidget(self.twBehaviors)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pbAddBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbAddBehavior.setObjectName("pbAddBehavior")
        self.verticalLayout_11.addWidget(self.pbAddBehavior)
        self.pbCloneBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbCloneBehavior.setObjectName("pbCloneBehavior")
        self.verticalLayout_11.addWidget(self.pbCloneBehavior)
        self.pbRemoveBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbRemoveBehavior.setObjectName("pbRemoveBehavior")
        self.verticalLayout_11.addWidget(self.pbRemoveBehavior)
        self.pbRemoveAllBehaviors = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbRemoveAllBehaviors.setObjectName("pbRemoveAllBehaviors")
        self.verticalLayout_11.addWidget(self.pbRemoveAllBehaviors)
        self.pbBehaviorsCategories = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbBehaviorsCategories.setObjectName("pbBehaviorsCategories")
        self.verticalLayout_11.addWidget(self.pbBehaviorsCategories)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.pbExclusionMatrix = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbExclusionMatrix.setObjectName("pbExclusionMatrix")
        self.verticalLayout_11.addWidget(self.pbExclusionMatrix)
        self.pbImportBehaviorsFromProject = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbImportBehaviorsFromProject.setObjectName("pbImportBehaviorsFromProject")
        self.verticalLayout_11.addWidget(self.pbImportBehaviorsFromProject)
        self.pbImportFromJWatcher = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbImportFromJWatcher.setEnabled(True)
        self.pbImportFromJWatcher.setObjectName("pbImportFromJWatcher")
        self.verticalLayout_11.addWidget(self.pbImportFromJWatcher)
        self.pbImportFromTextFile = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbImportFromTextFile.setObjectName("pbImportFromTextFile")
        self.verticalLayout_11.addWidget(self.pbImportFromTextFile)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.lbObservationsState = QtWidgets.QLabel(self.tabConfiguration)
        self.lbObservationsState.setObjectName("lbObservationsState")
        self.verticalLayout_5.addWidget(self.lbObservationsState)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.tabProject.addTab(self.tabConfiguration, "")
        self.tabSubjects = QtWidgets.QWidget()
        self.tabSubjects.setObjectName("tabSubjects")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tabSubjects)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.twSubjects = QtWidgets.QTableWidget(self.tabSubjects)
        self.twSubjects.setAutoFillBackground(False)
        self.twSubjects.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twSubjects.setMidLineWidth(0)
        self.twSubjects.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twSubjects.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twSubjects.setObjectName("twSubjects")
        self.twSubjects.setColumnCount(3)
        self.twSubjects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_12.addWidget(self.twSubjects)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pbAddSubject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbAddSubject.setObjectName("pbAddSubject")
        self.verticalLayout_15.addWidget(self.pbAddSubject)
        self.pbRemoveSubject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbRemoveSubject.setObjectName("pbRemoveSubject")
        self.verticalLayout_15.addWidget(self.pbRemoveSubject)
        self.pbImportSubjectsFromProject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbImportSubjectsFromProject.setObjectName("pbImportSubjectsFromProject")
        self.verticalLayout_15.addWidget(self.pbImportSubjectsFromProject)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem1)
        self.horizontalLayout_12.addLayout(self.verticalLayout_15)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.lbSubjectsState = QtWidgets.QLabel(self.tabSubjects)
        self.lbSubjectsState.setObjectName("lbSubjectsState")
        self.verticalLayout_14.addWidget(self.lbSubjectsState)
        self.verticalLayout_16.addLayout(self.verticalLayout_14)
        self.tabProject.addTab(self.tabSubjects, "")
        self.tabIndependentVariables = QtWidgets.QWidget()
        self.tabIndependentVariables.setObjectName("tabIndependentVariables")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tabIndependentVariables)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.twVariables = QtWidgets.QTableWidget(self.tabIndependentVariables)
        self.twVariables.setAutoFillBackground(False)
        self.twVariables.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twVariables.setMidLineWidth(0)
        self.twVariables.setAlternatingRowColors(True)
        self.twVariables.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twVariables.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twVariables.setObjectName("twVariables")
        self.twVariables.setColumnCount(5)
        self.twVariables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(4, item)
        self.twVariables.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_13.addWidget(self.twVariables)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pbAddVariable = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbAddVariable.setObjectName("pbAddVariable")
        self.verticalLayout_12.addWidget(self.pbAddVariable)
        self.pbRemoveVariable = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbRemoveVariable.setObjectName("pbRemoveVariable")
        self.verticalLayout_12.addWidget(self.pbRemoveVariable)
        self.pbImportVarFromProject = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbImportVarFromProject.setObjectName("pbImportVarFromProject")
        self.verticalLayout_12.addWidget(self.pbImportVarFromProject)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.verticalLayout_18.addLayout(self.horizontalLayout_13)
        self.tabProject.addTab(self.tabIndependentVariables, "")
        self.tabObservations = QtWidgets.QWidget()
        self.tabObservations.setObjectName("tabObservations")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabObservations)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.twObservations = QtWidgets.QTableWidget(self.tabObservations)
        self.twObservations.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twObservations.setDragDropOverwriteMode(False)
        self.twObservations.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twObservations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twObservations.setObjectName("twObservations")
        self.twObservations.setColumnCount(4)
        self.twObservations.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.twObservations)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbRemoveObservation = QtWidgets.QPushButton(self.tabObservations)
        self.pbRemoveObservation.setObjectName("pbRemoveObservation")
        self.verticalLayout.addWidget(self.pbRemoveObservation)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabProject.addTab(self.tabObservations, "")
        self.verticalLayout_6.addWidget(self.tabProject)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pbCancel = QtWidgets.QPushButton(dlgProject)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_4.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(dlgProject)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_4.addWidget(self.pbOK)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.retranslateUi(dlgProject)
        self.tabProject.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(dlgProject)

    def retranslateUi(self, dlgProject):
        _translate = QtCore.QCoreApplication.translate
        dlgProject.setWindowTitle(_translate("dlgProject", "Project"))
        self.label.setText(_translate("dlgProject", "Project name"))
        self.lbProjectFilePath.setText(_translate("dlgProject", "Project file path:"))
        self.label_7.setText(_translate("dlgProject", "Date"))
        self.dteDate.setDisplayFormat(_translate("dlgProject", "yyyy-MM-dd hh:mm"))
        self.label_6.setText(_translate("dlgProject", "Description"))
        self.lbTimeFormat.setText(_translate("dlgProject", "Time format"))
        self.rbSeconds.setText(_translate("dlgProject", "seconds"))
        self.rbHMS.setText(_translate("dlgProject", "hh:mm:ss.mss"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabInformation), _translate("dlgProject", "Information"))
        self.twBehaviors.setSortingEnabled(True)
        item = self.twBehaviors.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Behavior type"))
        item = self.twBehaviors.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Key"))
        item = self.twBehaviors.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Code"))
        item = self.twBehaviors.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Description"))
        item = self.twBehaviors.horizontalHeaderItem(4)
        item.setText(_translate("dlgProject", "Category"))
        item = self.twBehaviors.horizontalHeaderItem(5)
        item.setText(_translate("dlgProject", "Modifiers"))
        item = self.twBehaviors.horizontalHeaderItem(6)
        item.setText(_translate("dlgProject", "Exclusion"))
        item = self.twBehaviors.horizontalHeaderItem(7)
        item.setText(_translate("dlgProject", "Modifiers coding map"))
        self.pbAddBehavior.setText(_translate("dlgProject", "Add behavior"))
        self.pbCloneBehavior.setText(_translate("dlgProject", "Clone behavior"))
        self.pbRemoveBehavior.setText(_translate("dlgProject", "Remove behavior"))
        self.pbRemoveAllBehaviors.setText(_translate("dlgProject", "Remove all behaviors"))
        self.pbBehaviorsCategories.setText(_translate("dlgProject", "Behavioral categories"))
        self.pbExclusionMatrix.setText(_translate("dlgProject", "Exclusion matrix"))
        self.pbImportBehaviorsFromProject.setText(_translate("dlgProject", "Import behaviors\n"
"from a BORIS project"))
        self.pbImportFromJWatcher.setText(_translate("dlgProject", "Import from JWatcher"))
        self.pbImportFromTextFile.setText(_translate("dlgProject", "Import from text file"))
        self.lbObservationsState.setText(_translate("dlgProject", "TextLabel"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabConfiguration), _translate("dlgProject", "Ethogram"))
        self.twSubjects.setSortingEnabled(True)
        item = self.twSubjects.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Key"))
        item = self.twSubjects.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Subject name"))
        item = self.twSubjects.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Description"))
        self.pbAddSubject.setText(_translate("dlgProject", "Add subject"))
        self.pbRemoveSubject.setText(_translate("dlgProject", "Remove subject"))
        self.pbImportSubjectsFromProject.setText(_translate("dlgProject", "Import subjects\n"
"from a BORIS project"))
        self.lbSubjectsState.setText(_translate("dlgProject", "TextLabel"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabSubjects), _translate("dlgProject", "Subjects"))
        self.twVariables.setSortingEnabled(True)
        item = self.twVariables.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Label"))
        item = self.twVariables.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Description"))
        item = self.twVariables.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Type"))
        item = self.twVariables.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Predefined value"))
        item = self.twVariables.horizontalHeaderItem(4)
        item.setText(_translate("dlgProject", "Set of values"))
        self.pbAddVariable.setText(_translate("dlgProject", "Add variable"))
        self.pbRemoveVariable.setText(_translate("dlgProject", "Remove variable"))
        self.pbImportVarFromProject.setText(_translate("dlgProject", "Import variables\n"
"from a BORIS project"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabIndependentVariables), _translate("dlgProject", "Independent variables"))
        item = self.twObservations.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "id"))
        item = self.twObservations.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Date"))
        item = self.twObservations.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Description"))
        item = self.twObservations.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Media"))
        self.pbRemoveObservation.setText(_translate("dlgProject", "Remove observation"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabObservations), _translate("dlgProject", "Observations"))
        self.pbCancel.setText(_translate("dlgProject", "Cancel"))
        self.pbOK.setText(_translate("dlgProject", "OK"))

