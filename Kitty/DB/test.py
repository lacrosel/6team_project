import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

#============================  class 설정 부분  =======================================
def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('main.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass( QMainWindow, form_class):
    def __init__(self):
        super( ).__init__( )
        self.setupUi(self)
#==========================  Signal & Setting 부분  ===================================
        #----------버튼1,2,3,4 화살표 설정-----------------------
        self.tool_1.setArrowType(Qt.UpArrow)
        self.tool_2.setArrowType(Qt.DownArrow)
        self.tool_3.setArrowType(Qt.LeftArrow)
        self.tool_4.setArrowType(Qt.RightArrow)
        self.tool_4.setAutoRaise(True)

        #---------버튼5,6,7 메뉴 팝업 설정---------------------

        menu = QMenu()
        menu.addAction('Action1')
        menu.addAction('Action2')


        self.tool_5.setIconSize(QSize(41,41))
        self.tool_5.setMenu(menu)
        self.tool_5.setPopupMode(QToolButton.DelayedPopup)


        self.tool_6.setIconSize(QSize(41,41))
        self.tool_6.setMenu(menu)
        self.tool_6.setPopupMode(QToolButton.MenuButtonPopup)


        self.tool_7.setIconSize(QSize(41,41))
        self.tool_7.setMenu(menu)
        self.tool_7.setPopupMode(QToolButton.InstantPopup)


        # ---------버튼8 setDefaultAction 설정---------------------

        act = QAction()

        act.setToolTip("example")
        self.tool_8.setIconSize(QSize(41,41))
        self.tool_8.setDefaultAction(act)

        #----------버튼9,10,11,12 아이콘과 텍스트 배열 설정-----------

        self.tool_9.setIconSize(QSize(10,10))
        self.tool_9.setText('test')
        self.tool_9.setToolButtonStyle(Qt.ToolButtonIconOnly)


        self.tool_10.setIconSize(QSize(10,10))
        self.tool_10.setText('test')
        self.tool_10.setToolButtonStyle(Qt.ToolButtonTextOnly)


        self.tool_11.setIconSize(QSize(10,10))
        self.tool_11.setText('test')
        self.tool_11.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.tool_12.setIconSize(QSize(10,10))
        self.tool_12.setText('test')
        self.tool_12.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
#===============================  Slot 부분   =========================================

#==============================  app 실행 부분  =======================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass( )
    myWindow.show( )
    app.exec_( )