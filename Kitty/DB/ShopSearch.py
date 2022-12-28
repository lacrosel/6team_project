import sys
import random
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, QObject, QEvent

form_class = uic.loadUiType('./main.ui')[0]  # 페이지 UI불러옴
Shopname = uic.loadUiType('./Shopname.ui')[0]
Review_window = uic.loadUiType('./review.ui')[0]
# 이벤트 핸들러 생성 #사용자 정의 시그널 사용
# connect(instance) Q~클래스로 만들어진 객체를 가지고 옴.

#"상가업소번호","상호명","지점명","상권업종대분류코드","상권업종대분류명","상권업종중분류코드","상권업종중분류명","상권업종소분류코드",
    # "상권업종소분류명","표준산업분류코드","표준산업분류명","시도코드","시도명","시군구코드","시군구명","행정동코드","행정동명","법정동코드",
            # "법정동명","지번코드","대지구분코드","대지구분명","지번본번지","지번부번지","지번주소","도로명코드","도로명","건물본번지","건물부번지",
# "건물관리번호","건물명","도로명주소","구우편번호","신우편번호","동정보","층정보","호정보","경도","위도"
class ChangeShopname(QDialog,Shopname):
    def __init__(self):
        super().__init__()
        self.shopnumber = ''
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Update)

    def Update(self):
        text = self.lineEdit.text()
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f"UPDATE Gwangju SET 상호명  = '{text}' WHERE 상가업소번호 =  '{self.shopnumber}' ")
        conn.commit()
        c.close()

class Reviewmanage(QDialog,Review_window):
    def __init__(self):
        super().__init__()
        self.shopnumber = ''
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.Reviewwirte_1.clicked.connect(self.moveWritepage)
        self.Reviewwirte_2.clicked.connect(self.moveWritepage)
        self.reviewManage_1.clicked.connect(self.moveManagepage)
        self.reviewManage_2.clicked.connect(self.moveManagepage)
        self.Review_search_1.clicked.connect(self.moveSearchpage)
        self.Review_search_2.clicked.connect(self.moveSearchpage)
        self.pushButton_Register.clicked.connect(self.writeReview)
        self.tableWidget_Manage.cellDoubleClicked.connect(self.reviewDelete)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS REVIEW (상가번호 TEXT,리뷰 TEXT,평점 TEXT)")
        c.close()
        self.makeReviewlist()


    def moveSearchpage(self):
        self.tableWidget_search.clearContents()
        self.makeReviewlist()
        self.tableWidget_search.setRowCount(len(self.ReviewList))
        self.tableWidget_search.setColumnCount(3)
        for i in range(len(self.ReviewList)):
            for j in range(len(self.ReviewList[i])):
                # i번째 줄의 j번째 칸에 데이터를 넣어줌
                self.tableWidget_search.setItem(i, j, QTableWidgetItem(self.ReviewList[i][j]))
        self.stackedWidget.setCurrentIndex(0)
    def moveWritepage(self):
        self.stackedWidget.setCurrentIndex(2)
    def moveManagepage(self):
        self.tableWidget_Manage.clearContents()
        self.makeReviewlist()
        self.tableWidget_Manage.setRowCount(len(self.ReviewList))
        self.tableWidget_Manage.setColumnCount(3)
        for i in range(len(self.ReviewList)):
            for j in range(len(self.ReviewList[i])):
                # i번째 줄의 j번째 칸에 데이터를 넣어줌
                self.tableWidget_Manage.setItem(i, j, QTableWidgetItem(self.ReviewList[i][j]))
        self.stackedWidget.setCurrentIndex(1)
    def makeReviewlist(self):
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f"SELECT * FROM REVIEW WHERE 상가번호 = '{self.shopnumber}'")
        self.ReviewList = c.fetchall()
        print(self.ReviewList)
        c.close()

    def writeReview(self):
        reviewtext = self.lineEdit_Review.text()
        print(reviewtext)
        reviewscore = self.spinBox_score.value()
        print(reviewscore)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f"INSERT INTO REVIEW VALUES ('{self.shopnumber}','{reviewtext}','{reviewscore}')")
        print("Success")
        c.close()
    def reviewDelete(self):
        option = QtWidgets.QMessageBox.question(self, "QMessageBox", "삭제하시겠습니까??",
                                                QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Yes)
        if option == QtWidgets.QMessageBox.Yes:
            QtWidgets.QMessageBox.information(self, "QMessageBox", "삭제되었습니다 다시 조회해주세요")
            conn = sqlite3.connect("Shop2.db", isolation_level=None)
            # 커서 획득
            c = conn.cursor()
            c.execute(f"DELETE FROM REVIEW WHERE 상가번호 = '{self.shopnumber}'")
            c.close()
        else:
            return
    def searchReview(self):
        pass
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
        self.pushButton_2.clicked.connect(self.Search2)
        self.comboBox_1.currentIndexChanged.connect(self.combobox)
        self.comboBox_2.currentIndexChanged.connect(self.combobox2)
        self.comboBox_3.currentIndexChanged.connect(self.ChangeLabel3)
        self.tableWidget.cellDoubleClicked.connect(self.openDialogue)
        self.tableWidget.cellClicked.connect(self.cellclicked)
        self.pushButton_3.clicked.connect(self.openDialogue2)
        self.show()
        self.shopnumber = ''
        # self.ChangeLabel()

    def openDialogue2(self):
        window_3 = Reviewmanage()
        print(window_3.shopnumber)
        shopnumber= self.tableWidget.item(self.row,0)
        window_3.shopnumber = shopnumber.text()
        print(window_3.shopnumber)
        window_3.exec_()

    def cellclicked(self,row,column):
        self.row = row
        self.column = column
    def openDialogue(self, row, column):
        window_2 = ChangeShopname()
        self.shopnumber = self.tableWidget.item(row, 0)
        window_2.shopnumber = self.shopnumber.text()

        window_2.exec_()
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
    def Search2(self):
        self.tableWidget.clearContents()
        Searchlist =[]
        searchtext = self.comboBox_3.currentText()

        # DB 생성 (오토 커밋)
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT * FROM Gwangju WHERE 상권업종소분류코드 LIKE "%{searchtext}%"')
        Searchlist = c.fetchall()
        c.close()
        if Searchlist == [] :
            return
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
        self.ChangeLabel()

    def ChangeLabel(self):
        CB_String = self.comboBox_1.currentText()
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        Codelist = []
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT 대분류코드,대분류명 FROM CodeView2 WHERE 대분류코드 LIKE "%{CB_String}%"')
        Codelist = c.fetchall()
        self.label.setText(Codelist[0][1])
        c.close()

    def ChangeLabel2(self):
        CB_String = self.comboBox_2.currentText()
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        Codelist = []
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT 중분류코드,중분류명 FROM CodeView WHERE 중분류코드 LIKE "%{CB_String}%"')
        Codelist = c.fetchall()
        self.label_2.setText(Codelist[0][1])
        c.close()


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
        self.ChangeLabel2()
    def ChangeLabel3(self):
        CB_String = self.comboBox_3.currentText()
        conn = sqlite3.connect("Shop2.db", isolation_level=None)
        Codelist = []
        # 커서 획득
        c = conn.cursor()
        c.execute(f'SELECT 소분류코드,소분류명 FROM CodeView3 WHERE 소분류코드 LIKE "%{CB_String}%"')
        Codelist = c.fetchall()
        self.label_3.setText(Codelist[0][1])
        c.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)


    mainWindow = Main()  # 상동
    mainWindow.show()
    app.exec_()

