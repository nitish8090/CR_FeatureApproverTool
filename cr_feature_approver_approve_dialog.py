import os

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont

from qgis.core import QgsProject, QgsMapLayer, QgsField, edit, QgsPalLayerSettings, QgsTextFormat, QgsVectorLayerSimpleLabeling, QgsTextBufferSettings
from qgis.utils import iface

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'cr_feature_approver_approve_dialog.ui'))


class DialogBoxDockWidget(QtWidgets.QDockWidget, FORM_CLASS):
    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(DialogBoxDockWidget, self).__init__(parent)
        self.setupUi(self)
        #
        # self.selected_layer = None
        # self.selected_feature = None

        # UI Conncetions
        # self.combobox_layers

        self.cbox_roof_c

        # Button Connections
        # self.btn_refresh_layer.clicked.connect(self.refresh_layer_list)
        # self.btn_select_layer.clicked.connect(self.select_layer)
        #
        # self.btn_next.clicked.connect(self.next)
        # self.btn_previous.clicked.connect(self.previous)
        # self.btn_approve_next.clicked.connect(self.approve_and_next)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()