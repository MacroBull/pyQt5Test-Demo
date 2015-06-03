# -*- coding: utf-8 -*-

"""
Module implementing Form0.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_main import Ui_Form


from PyQt5 import *

import cv2
import numpy as np

import time


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

        self.cam = cv2.VideoCapture(0)

        self.image = QtGui.QImage(0,  0,  QtGui.QImage.Format_RGB888)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(33)

        self.time_last = 0

    def closeEvent(self, event):
        self.cam.release()

    def paintEvent(self,  event):
        painter = QtGui.QPainter(self)
        painter.drawImage(QtCore.QPoint(0, 0),  self.image)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.timer.stop()
        self.cam.release()


    def tick(self):
        frame = self.cam.read()
        if frame[0]:
            frame = frame[1]

            frame = cv2.cvtColor(frame,  cv2.COLOR_BGR2RGB)

            Z = frame.reshape((-1,3))

            # convert to np.float32
            Z = np.float32(Z)

            # define criteria, number of clusters(K) and apply kmeans()
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

            K = 3

            ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

            # Now convert back into uint8, and make original image
            center = np.uint8(center)
            res = center[label.flatten()]
            frame = res.reshape((frame.shape))



            self.image = QtGui.QImage(frame.tobytes(), frame.shape[1],  frame.shape[0], QtGui.QImage.Format_RGB888)

            if frame.shape[0]/frame.shape[1]>self.width()/self.height():
                self.image = self.image.scaledToWidth(self.width())
            else:
                self.image = self.image.scaledToHeight(self.height())
        t = time.time()
        self.pushButton.setText("{:.2f}".format(1/(t - self.time_last)) + 'fps')
        self.time_last = t
        self.update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Form0()
    ui.show()
    r = app.exec_()
#    if ui: ui.cam.release()
    sys.exit(r)
