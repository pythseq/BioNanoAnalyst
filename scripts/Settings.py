# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

try:
    from PyQt4 import QtGui,QtCore
except ImportError:
    from PySide import QtGui,QtCore

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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(430, 356)
        Settings.setMinimumSize(QtCore.QSize(430, 356))
        Settings.setMaximumSize(QtCore.QSize(430, 356))
        self.verticalLayout = QtGui.QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tools_frame = QtGui.QFrame(Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_frame.sizePolicy().hasHeightForWidth())
        self.tools_frame.setSizePolicy(sizePolicy)
        self.tools_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.tools_frame.setLineWidth(2)
        self.tools_frame.setObjectName(_fromUtf8("tools_frame"))
        self.gridLayout = QtGui.QGridLayout(self.tools_frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tools_location_label = QtGui.QLabel(self.tools_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_location_label.sizePolicy().hasHeightForWidth())
        self.tools_location_label.setSizePolicy(sizePolicy)
        self.tools_location_label.setObjectName(_fromUtf8("tools_location_label"))
        self.gridLayout.addWidget(self.tools_location_label, 1, 0, 1, 1)
        self.tools_location_selecet_bn = QtGui.QPushButton(self.tools_frame)
        self.tools_location_selecet_bn.setObjectName(_fromUtf8("tools_location_selecet_bn"))
        self.gridLayout.addWidget(self.tools_location_selecet_bn, 1, 2, 1, 1)
        self.tools_location_input = QtGui.QLineEdit(self.tools_frame)
        self.tools_location_input.setObjectName(_fromUtf8("tools_location_input"))
        self.gridLayout.addWidget(self.tools_location_input, 1, 1, 1, 1)
        self.tools_label = QtGui.QLabel(self.tools_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_label.sizePolicy().hasHeightForWidth())
        self.tools_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tools_label.setFont(font)
        self.tools_label.setObjectName(_fromUtf8("tools_label"))
        self.gridLayout.addWidget(self.tools_label, 0, 0, 1, 1)
        self.tools_location_clear_bn = QtGui.QPushButton(self.tools_frame)
        self.tools_location_clear_bn.setObjectName(_fromUtf8("tools_location_clear_bn"))
        self.gridLayout.addWidget(self.tools_location_clear_bn, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.tools_frame)
        self.frame = QtGui.QFrame(Settings)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.scripts_label = QtGui.QLabel(self.frame)
        self.scripts_label.setGeometry(QtCore.QRect(10, 10, 81, 22))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scripts_label.sizePolicy().hasHeightForWidth())
        self.scripts_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.scripts_label.setFont(font)
        self.scripts_label.setObjectName(_fromUtf8("scripts_label"))
        self.scripts_location_label = QtGui.QLabel(self.frame)
        self.scripts_location_label.setGeometry(QtCore.QRect(10, 40, 63, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scripts_location_label.sizePolicy().hasHeightForWidth())
        self.scripts_location_label.setSizePolicy(sizePolicy)
        self.scripts_location_label.setObjectName(_fromUtf8("scripts_location_label"))
        self.scripts_location_input = QtGui.QLineEdit(self.frame)
        self.scripts_location_input.setGeometry(QtCore.QRect(80, 40, 141, 27))
        self.scripts_location_input.setObjectName(_fromUtf8("scripts_location_input"))
        self.scripts_location_selecet_bn = QtGui.QPushButton(self.frame)
        self.scripts_location_selecet_bn.setGeometry(QtCore.QRect(230, 40, 85, 27))
        self.scripts_location_selecet_bn.setObjectName(_fromUtf8("scripts_location_selecet_bn"))
        self.scripts_location_clear_bn = QtGui.QPushButton(self.frame)
        self.scripts_location_clear_bn.setGeometry(QtCore.QRect(320, 40, 85, 27))
        self.scripts_location_clear_bn.setObjectName(_fromUtf8("scripts_location_clear_bn"))
        self.scripts_label.raise_()
        self.scripts_location_label.raise_()
        self.scripts_location_input.raise_()
        self.scripts_location_selecet_bn.raise_()
        self.scripts_location_clear_bn.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.assembly_frame = QtGui.QFrame(Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assembly_frame.sizePolicy().hasHeightForWidth())
        self.assembly_frame.setSizePolicy(sizePolicy)
        self.assembly_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.assembly_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.assembly_frame.setLineWidth(2)
        self.assembly_frame.setObjectName(_fromUtf8("assembly_frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.assembly_frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.iteration_label = QtGui.QLabel(self.assembly_frame)
        self.iteration_label.setObjectName(_fromUtf8("iteration_label"))
        self.gridLayout_2.addWidget(self.iteration_label, 3, 0, 1, 1)
        self.threads_label = QtGui.QLabel(self.assembly_frame)
        self.threads_label.setObjectName(_fromUtf8("threads_label"))
        self.gridLayout_2.addWidget(self.threads_label, 1, 0, 1, 1)
        self.threads_spinBox = QtGui.QSpinBox(self.assembly_frame)
        self.threads_spinBox.setObjectName(_fromUtf8("threads_spinBox"))
        self.gridLayout_2.addWidget(self.threads_spinBox, 1, 2, 1, 1)
        self.iteration_spinBox = QtGui.QSpinBox(self.assembly_frame)
        self.iteration_spinBox.setObjectName(_fromUtf8("iteration_spinBox"))
        self.gridLayout_2.addWidget(self.iteration_spinBox, 3, 2, 1, 1)
        self.output_clear_bn = QtGui.QPushButton(self.assembly_frame)
        self.output_clear_bn.setObjectName(_fromUtf8("output_clear_bn"))
        self.gridLayout_2.addWidget(self.output_clear_bn, 5, 5, 1, 1)
        self.output_select_bn = QtGui.QPushButton(self.assembly_frame)
        self.output_select_bn.setObjectName(_fromUtf8("output_select_bn"))
        self.gridLayout_2.addWidget(self.output_select_bn, 5, 4, 1, 1)
        self.jobs_spinBox = QtGui.QSpinBox(self.assembly_frame)
        self.jobs_spinBox.setMaximumSize(QtCore.QSize(61, 16777215))
        self.jobs_spinBox.setObjectName(_fromUtf8("jobs_spinBox"))
        self.gridLayout_2.addWidget(self.jobs_spinBox, 1, 5, 1, 1)
        self.gs_label = QtGui.QLabel(self.assembly_frame)
        self.gs_label.setObjectName(_fromUtf8("gs_label"))
        self.gridLayout_2.addWidget(self.gs_label, 3, 3, 1, 2)
        self.gs_input = QtGui.QLineEdit(self.assembly_frame)
        self.gs_input.setMaximumSize(QtCore.QSize(61, 16777215))
        self.gs_input.setObjectName(_fromUtf8("gs_input"))
        self.gridLayout_2.addWidget(self.gs_input, 3, 5, 1, 1)
        self.jobs_label = QtGui.QLabel(self.assembly_frame)
        self.jobs_label.setObjectName(_fromUtf8("jobs_label"))
        self.gridLayout_2.addWidget(self.jobs_label, 1, 3, 1, 1)
        self.output_input = QtGui.QLineEdit(self.assembly_frame)
        self.output_input.setObjectName(_fromUtf8("output_input"))
        self.gridLayout_2.addWidget(self.output_input, 5, 2, 1, 2)
        self.output_label = QtGui.QLabel(self.assembly_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_label.sizePolicy().hasHeightForWidth())
        self.output_label.setSizePolicy(sizePolicy)
        self.output_label.setObjectName(_fromUtf8("output_label"))
        self.gridLayout_2.addWidget(self.output_label, 5, 0, 1, 2)
        self.assembly_label = QtGui.QLabel(self.assembly_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assembly_label.sizePolicy().hasHeightForWidth())
        self.assembly_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.assembly_label.setFont(font)
        self.assembly_label.setObjectName(_fromUtf8("assembly_label"))
        self.gridLayout_2.addWidget(self.assembly_label, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.assembly_frame)
        self.setting_confirm_frame = QtGui.QDialogButtonBox(Settings)
        self.setting_confirm_frame.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.setting_confirm_frame.setObjectName(_fromUtf8("setting_confirm_frame"))
        self.verticalLayout.addWidget(self.setting_confirm_frame)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.tools_location_label.setText(_translate("Settings", "Location:", None))
        self.tools_location_selecet_bn.setText(_translate("Settings", "Select", None))
        self.tools_label.setText(_translate("Settings", "Tools", None))
        self.tools_location_clear_bn.setText(_translate("Settings", "Clear", None))
        self.scripts_label.setText(_translate("Settings", "Scripts", None))
        self.scripts_location_label.setText(_translate("Settings", "Location:", None))
        self.scripts_location_selecet_bn.setText(_translate("Settings", "Select", None))
        self.scripts_location_clear_bn.setText(_translate("Settings", "Clear", None))
        self.iteration_label.setText(_translate("Settings", "Iteration:", None))
        self.threads_label.setText(_translate("Settings", "Threads:", None))
        self.output_clear_bn.setText(_translate("Settings", "Clear", None))
        self.output_select_bn.setText(_translate("Settings", "Select", None))
        self.gs_label.setText(_translate("Settings", "Genome size (Mb):", None))
        self.jobs_label.setText(_translate("Settings", "Jobs:", None))
        self.output_label.setText(_translate("Settings", "Output location:", None))
        self.assembly_label.setText(_translate("Settings", "Parameters", None))