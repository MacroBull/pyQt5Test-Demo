# -*- coding: utf-8 -*-

"""
Module implementing Form0.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from PyQt5 import QtWidgets,  QtGui,  QtCore

from Ui_form0 import Ui_Form


class Form0(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super(Form0, self).__init__(parent)
        self.setupUi(self)

        self.label.rotation = 0
        self.label.paintEvent = self.labelRotatedPaintEvent

    def labelRotatedPaintEvent(self,  event):
#        QtWidgets.QLabel.paintEvent(self.label,  event)
        painter = QtWidgets.QStylePainter(self.label)
        opt = QtWidgets.QStyleOptionViewItem()
        painter.rotate(self.label.rotation)
        painter.drawItemText( QtCore.QRect(0, 0, 100, 100), QtCore.Qt.AlignLeft,
                             opt.palette,  True,  self.label.text(),  QtGui.QPalette.Text)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label.rotation = 0
        self.label.setText('Hello world!')

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self, value):
        """
        Slot documentation goes here.
        """
        value /= 99
        self.label.rotation = value * 90
        self.label.setText(str(value))
