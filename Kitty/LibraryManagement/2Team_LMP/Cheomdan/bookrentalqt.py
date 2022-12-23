import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
import csv
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
to = QDate.currentDate().addDays(7)

form_widget = uic.loadUiType('borrow.ui')[0]


class Rental_page(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.id = ""
        self.row=0
        f = open('cheomdan.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        self.csv_list = []
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        f = open('Rent_list.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        self.bookrental = []
        for line in self.rdr:
            self.bookrental.append(line)
        f.close()
        self.rentstack.setCurrentIndex(0)
        self.YH_reset.clicked.connect(self.clear)
        self.YH_search.clicked.connect(lambda: self.search_Rental())
        self.YH_lineEdit.textChanged.connect(self.lineeditTextFunction)
        self.YH_lineEdit.returnPressed.connect(self.printTextFunction)
        self.YH_main.setColumnWidth(0, 40)
        self.YH_main.setColumnWidth(1, 80)
        self.YH_main.setColumnWidth(2, 320)
        self.YH_main_2.setColumnWidth(0, 40)
        self.YH_main_2.setColumnWidth(1, 80)
        self.YH_main_2.setColumnWidth(2, 465)
        self.YH_main_3.setColumnWidth(0, 40)
        self.YH_main_3.setColumnWidth(1, 80)
        self.YH_main_3.setColumnWidth(2, 680)
        self.YH_main.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.YH_main.selectionModel().selectedRows()
        self.YH_main.cellClicked.connect(self.CellValue)
        self.YH_main_2.cellClicked.connect(self.CellValue_return)
        self.YH_rent.clicked.connect(self.Bookrental)
        self.YH_return.clicked.connect(self.Movereturnpage)  # 메인페이지로 기능 이동
        self.YH_rent_2.clicked.connect(self.real_return)
        self.real_return_list = []
        self.member_return_list = []
        self.YH_Back.clicked.connect(self.prestack)
        self.YH_Home.clicked.connect(self.moveMainpage)
        self.YH_Home_2.clicked.connect(self.moveMainpage)


    def moveMainpage(self):
        self.parent().setCurrentIndex(0)
    def prestack(self):
        self.rentstack.setCurrentIndex(0)

    def real_return(self):
        if self.member_return_list == [] :
            return
        if self.row2 == "abc" :
            return
        self.YH_main_2.clearContents()  # 메인 2의 컨텐츠를 지운다
        check_v = 0
        for i in self.bookrental:  # bookrental list 확인
            if self.member_return_list[self.row2] == i:  # 전체대여리스트와 가입자의 대여리스트가 같다면
                del (self.bookrental[check_v])  # 전체 대여리스트에서 그 줄을 빼준다
            check_v += 1
        self.real_return_list.append(self.member_return_list[self.row2])
        del (self.member_return_list[self.row2])
        # 대여 반납 현황판 업데이트

        Row = 0
        self.YH_main_3.setRowCount(len(self.real_return_list))
        for s in self.real_return_list:
            self.YH_main_3.setItem(Row, 0, QTableWidgetItem(s[0]))  # 연번
            self.YH_main_3.setItem(Row, 1, QTableWidgetItem(s[1]))  # 도서관명
            self.YH_main_3.setItem(Row, 2, QTableWidgetItem(s[4]))  # 도서명
            self.YH_main_3.setItem(Row, 3, QTableWidgetItem(s[5]))  # 지은이
            self.YH_main_3.setItem(Row, 4, QTableWidgetItem(s[3]))  # 등록번호
            Row += 1

        self.YH_main_2.setRowCount(len(self.member_return_list))
        Row = 0
        for s in self.member_return_list:
            if self.id == s[12]:
                self.YH_main_2.setItem(Row, 0, QTableWidgetItem(s[0]))  # 연번
                self.YH_main_2.setItem(Row, 1, QTableWidgetItem(s[1]))  # 도서관명
                self.YH_main_2.setItem(Row, 2, QTableWidgetItem(s[4]))  # 도서명
                self.YH_main_2.setItem(Row, 3, QTableWidgetItem(s[5]))  # 지은이
                self.YH_main_2.setItem(Row, 4, QTableWidgetItem(s[3]))  # 등록번호
                self.YH_main_2.setItem(Row, 5, QTableWidgetItem(s[10]))  # 대출일
                self.YH_main_2.setItem(Row, 6, QTableWidgetItem(s[11]))
                self.YH_main_2.setItem(Row, 7, QTableWidgetItem('-'))
                Row += 1

        with open('Rent_list.csv', 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerows(self.bookrental)

    def Movereturnpage(self):
        self.YH_main_2.clearContents()
        self.rentstack.setCurrentIndex(1)
        for s in self.bookrental:
            if s in self.member_return_list:
                continue
            if s[12] == self.id:
                self.member_return_list.append(s)
        self.YH_main_2.setRowCount(len(self.member_return_list))

        Row = 0
        for s in self.member_return_list:
            self.YH_main_2.setItem(Row, 0, QTableWidgetItem(s[0]))  # 연번
            self.YH_main_2.setItem(Row, 1, QTableWidgetItem(s[1]))  # 도서관명
            self.YH_main_2.setItem(Row, 2, QTableWidgetItem(s[4]))  # 도서명
            self.YH_main_2.setItem(Row, 3, QTableWidgetItem(s[5]))  # 지은이
            self.YH_main_2.setItem(Row, 4, QTableWidgetItem(s[3]))  # 등록번호
            self.YH_main_2.setItem(Row, 5, QTableWidgetItem(s[10]))  # 대출일
            self.YH_main_2.setItem(Row, 6, QTableWidgetItem(s[11]))
            self.YH_main_2.setItem(Row, 7, QTableWidgetItem('-'))
            # self.YH_main_2.setItem(Row, 1, QTableWidgetItem(s[4]))  # 반납일
            Row += 1

    def CellValue(self, row, column):
        item = self.YH_main.item(row, column)
        value = item.text()
        label_string = str(value)
        self.YH_label2.setText(label_string)  # 셀의 내용 가져오기
        self.clickedbook = self.search_list[row]
        self.row = row

    def CellValue_return(self, row, column):
        item1 = self.YH_main_2.item(row, column)
        value1 = item1.text()
        label_string1 = str(value1)
        self.YH_returnbook.setText(label_string1)
        self.row2 = row

    def Bookrental(self):  # 도서 대여 csv 추가
        Rental_info = self.YH_main.item(self.row, 5)
        Rental_info_value = Rental_info.text()

        if Rental_info_value == "X":  # 렌탈페이지에 이미 정보가 있으면 대출불가
            QMessageBox.critical(  # 메세지 박스를 통해서 알림창 생성하기  yes와 cancel로 대출 할지 여부 파악하기.
                self, '도서 대여 시스템', '이미 대여된 도서입니다',
                QMessageBox.Cancel)

        else:
            self.clickedbook.append(now.toString(Qt.ISODate))  # 대출일 추가
            self.clickedbook.append(to.toString(Qt.ISODate))  # 반납일 추가
            self.clickedbook.append(f'{self.id}')  # 아이디 추가
            self.YH_main.setItem(self.row, 5, QTableWidgetItem('X'))  # 대출하면 O > X로 바꿔줌
            self.YH_main.setItem(self.row, 6, QTableWidgetItem(self.clickedbook[10]))  # 대출일을 테이블위젯에 추가
            self.YH_main.setItem(self.row, 7, QTableWidgetItem(self.clickedbook[11]))  # 반납 예정일을 테이블위젯에 추가
            self.bookrental.append(self.clickedbook)
            with open('Rent_list.csv', 'w', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerows(self.bookrental)

    def lineeditTextFunction(self):  # 도서명 검색하기위해 사용하는 함수
        self.YH_lineEdit.setText(self.YH_lineEdit.text())  # lineEdit에 입력할수 있도록

    def printTextFunction(self):  # LineEdit에서 Return키(Enter키)가 눌렸을 때 기능 실행.
        print(self.YH_lineEdit.text())

    def clear(self):  # 초기화 버튼과 연결해서 초기화 버튼 눌렀으때 테이블위젯에 나온 자료 전부 제거하는 함수.
        self.YH_main.clearContents()

    def search_Rental(self):
        self.YH_main.clearContents()  # 처음에 테이블 위쳇 초기화 시키고 시작.
        self.search_list = []  # 빈리스트를 생성하기.(검색창에 검색하면 빈리스트에 추가하기위해서)
        text = self.YH_lineEdit.text()  # 검색창에 검색하면 그 검색한게 text안으로 들어가게힘.
        for line in self.csv_list:
            if text in line[4] or text in line[3]: #도서명 or 등록번호
                if '도서명' in line[4]:
                    continue
                self.search_list.append(line)

        self.YH_main.setRowCount(len(self.search_list))
        Row = 0
        for k in self.search_list:
            self.YH_main.setItem(Row, 0, QTableWidgetItem(k[0]))  # 연번
            self.YH_main.setItem(Row, 1, QTableWidgetItem(k[1]))  # 도서관 이름
            self.YH_main.setItem(Row, 2, QTableWidgetItem(k[4]))  # 도서명
            self.YH_main.setItem(Row, 3, QTableWidgetItem(k[5]))  # 지은이
            self.YH_main.setItem(Row, 4, QTableWidgetItem(k[3]))  # 등록번호
            self.YH_main.setItem(Row, 5, QTableWidgetItem('O'))  # 대출가능여부
            self.YH_main.setItem(Row, 6, QTableWidgetItem('-'))  # 대출일
            self.YH_main.setItem(Row, 7, QTableWidgetItem('-'))  # 반납예정일

            for i in range(len(self.bookrental)):
                if self.bookrental[i][4] == k[4]: # 도서명
                    self.YH_main.setItem(Row, 5, QTableWidgetItem('X')) # 대출가능여부
                    self.YH_main.setItem(Row, 6, QTableWidgetItem(self.bookrental[i][10]))  # 대출일
                    self.YH_main.setItem(Row, 7, QTableWidgetItem(self.bookrental[i][11]))  # 반납예정일
                    break
            Row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Rental_page()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()
