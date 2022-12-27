import sys
import random
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, QObject, QEvent

form_class = uic.loadUiType('./main.ui')[0]  # 페이지 UI불러옴

# 이벤트 핸들러 생성 #사용자 정의 시그널 사용
# connect(instance) Q~클래스로 만들어진 객체를 가지고 옴.

#"상가업소번호","상호명","지점명","상권업종대분류코드","상권업종대분류명","상권업종중분류코드","상권업종중분류명","상권업종소분류코드",
    # "상권업종소분류명","표준산업분류코드","표준산업분류명","시도코드","시도명","시군구코드","시군구명","행정동코드","행정동명","법정동코드",
            # "법정동명","지번코드","대지구분코드","대지구분명","지번본번지","지번부번지","지번주소","도로명코드","도로명","건물본번지","건물부번지",
# "건물관리번호","건물명","도로명주소","구우편번호","신우편번호","동정보","층정보","호정보","경도","위도"

class Main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f"SELECT * FROM Gwangju")

        self.Header = c.fetchone()
        self.allList = c.fetchall()
        c.close()
        self.pushButton.clicked.connect(self.Search)
        self.comboBox_1.currentIndexChanged.connect(self.combobox)
        self.comboBox_2.currentIndexChanged.connect(self.combobox2)
        # self.ChangeLabel()



    def Search(self):
        self.tableWidget.clearContents()
        Searchlist =[]
        searchtext = self.lineEdit.text()
        # DB 생성 (오토 커밋)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT * FROM Gwangju WHERE 상호명 LIKE "%{searchtext}%"')
        # c.execute('SELECT * FROM table1 WHERE id=?', param1)
        Searchlist = c.fetchall()
        c.close()

        # 테이블 위젯의 행과 열에 데이터 넣어줌
        self.tableWidget.setRowCount(len(Searchlist))
        self.tableWidget.setColumnCount(len(Searchlist[0]))
        for i in range(len(Searchlist)):
            for j in range(len(Searchlist[i])):
                # i번째 줄의 j번째 칸에 데이터를 넣어줌
                self.tableWidget.setItem(i, j, QTableWidgetItem(Searchlist[i][j]))
        self.tableWidget.setHorizontalHeaderLabels(self.Header)




    def combobox(self):
        self.comboBox_2.clear()
        CB_String = self.comboBox_1.currentText()
        # DB 생성 (오토 커밋)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        Codelist=[]
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT DISTINCT 중분류코드 FROM Shop_Code WHERE 중분류코드 LIKE "%{CB_String}%"')
        Codelist = c.fetchall()
        Codelist.sort()
        print(Codelist)
        c.close()
        for x in Codelist :
            self.comboBox_2.addItem(x[0])
        # self.ChangeLabel()

    # def ChangeLabel(self):
    #     conn = sqlite3.connect("Shop2.db", isolation_level=None)
    #     Codelist = []
    #     # 커서 획득
    #     c = conn.cursor()
    #     c.execute('DROP VIEW CodeView')
    #     c.execute('CREATE VIEW CodeView AS \
    #             SELECT DISTINCT 대분류코드,대분류명\
    #             FROM Person')
    #     c.execute('SELECT DISTINCT 대분류코드 FROM CodeView')
    #
    #     Codelist = c.fetchall()
    #     Codelist.sort()
    #     print(Codelist)
    #     c.close()
    def combobox2(self):
        self.comboBox_3.clear()
        CB_String = self.comboBox_2.currentText()
        # DB 생성 (오토 커밋)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        Codelist=[]
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT DISTINCT 소분류코드 FROM Shop_Code WHERE 소분류코드 LIKE "%{CB_String}%"')
        Codelist = c.fetchall()
        Codelist.sort()
        c.close()
        for x in Codelist :
            self.comboBox_3.addItem(x[0])



if __name__ == "__main__":
    app = QApplication(sys.argv)


    mainWindow = Main()  # 상동
    mainWindow.show()
    app.exec_()

