#################

from PyQt5 import QtWidgets
from form0 import *

import sys
app = QtWidgets.QApplication(sys.argv)
ui = Form0()
ui.show()
sys.exit(app.exec_())
