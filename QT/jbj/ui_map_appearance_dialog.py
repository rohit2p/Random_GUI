# Generated with pyuic5
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapAppearanceDialog(object):
    def setupUi(self, MapAppearanceDialog):
        MapAppearanceDialog.setObjectName("MapAppearanceDialog")
        MapAppearanceDialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(MapAppearanceDialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.cbDrawGraticule = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawGraticule.setObjectName("cbDrawGraticule")
        self.verticalLayout.addWidget(self.cbDrawGraticule)

        self.cbDrawCoastlines = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawCoastlines.setChecked(True)
        self.cbDrawCoastlines.setObjectName("cbDrawCoastlines")
        self.verticalLayout.addWidget(self.cbDrawCoastlines)

        self.cbLabelFlightTrack = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbLabelFlightTrack.setObjectName("cbLabelFlightTrack")
        self.verticalLayout.addWidget(self.cbLabelFlightTrack)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.cbFillWaterBodies = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbFillWaterBodies.setEnabled(True)
        self.cbFillWaterBodies.setMinimumSize(QtCore.QSize(145, 0))
        self.cbFillWaterBodies.setChecked(True)
        self.cbFillWaterBodies.setObjectName("cbFillWaterBodies")
        self.horizontalLayout.addWidget(self.cbFillWaterBodies)

        self.btWaterColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btWaterColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaterColour.setFlat(False)
        self.btWaterColour.setObjectName("btWaterColour")
        self.horizontalLayout.addWidget(self.btWaterColour)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.cbFillContinents = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbFillContinents.setMinimumSize(QtCore.QSize(145, 0))
        self.cbFillContinents.setObjectName("cbFillContinents")
        self.horizontalLayout_2.addWidget(self.cbFillContinents)

        self.btLandColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btLandColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btLandColour.setObjectName("btLandColour")
        self.horizontalLayout_2.addWidget(self.btLandColour)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.cbDrawMarker = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawMarker.setObjectName("cbDrawMarker")
        self.verticalLayout.addWidget(self.cbDrawMarker)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.cbDrawFlightTrack = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawFlightTrack.setMinimumSize(QtCore.QSize(145, 0))
        self.cbDrawFlightTrack.setObjectName("cbDrawFlightTrack")
        self.horizontalLayout_3.addWidget(self.cbDrawFlightTrack)

        self.btWaypointsColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btWaypointsColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaypointsColour.setObjectName("btWaypointsColour")
        self.horizontalLayout_3.addWidget(self.btWaypointsColour)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.cbDrawSurface = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawSurface.setObjectName("cbDrawSurface")
        self.verticalLayout.addWidget(self.cbDrawSurface)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.cbFillSurface = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbFillSurface.setMinimumSize(QtCore.QSize(145, 0))
        self.cbFillSurface.setObjectName("cbFillSurface")
        self.horizontalLayout_4.addWidget(self.cbFillSurface)

        self.btSurfaceColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btSurfaceColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btSurfaceColour.setObjectName("btSurfaceColour")
        self.horizontalLayout_4.addWidget(self.btSurfaceColour)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.buttonBox = QtWidgets.QDialogButtonBox(MapAppearanceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MapAppearanceDialog)
        self.buttonBox.accepted.connect(MapAppearanceDialog.accept)
        self.buttonBox.rejected.connect(MapAppearanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MapAppearanceDialog)

    def retranslateUi(self, MapAppearanceDialog):
        _translate = QtCore.QCoreApplication.translate
        MapAppearanceDialog.setWindowTitle(_translate("MapAppearanceDialog", "Map Appearance"))
        self.cbDrawGraticule.setText(_translate("MapAppearanceDialog", "Draw graticule"))
        self.cbDrawCoastlines.setText(_translate("MapAppearanceDialog", "Draw coastlines"))
        self.cbLabelFlightTrack.setText(_translate("MapAppearanceDialog", "Label flight track"))
        self.cbFillWaterBodies.setText(_translate("MapAppearanceDialog", "Fill water bodies"))
        self.btWaterColour.setText(_translate("MapAppearanceDialog", "Colour..."))
        self.cbFillContinents.setText(_translate("MapAppearanceDialog", "Fill continents"))
        self.btLandColour.setText(_translate("MapAppearanceDialog", "Colour..."))
        self.cbDrawMarker.setText(_translate("MapAppearanceDialog", "Draw waypoints"))
        self.btWaypointsColour.setText(_translate("MapAppearanceDialog", "Colour..."))
        self.cbDrawFlightTrack.setText(_translate("MapAppearanceDialog", "Draw flight track"))
        self.cbDrawSurface.setText(_translate("MapAppearanceDialog", "Draw surface"))
        self.btSurfaceColour.setText(_translate("MapAppearanceDialog", "Colour..."))
