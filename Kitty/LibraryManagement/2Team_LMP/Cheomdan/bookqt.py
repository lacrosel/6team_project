import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("booksearch.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class BooksearchClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        # ui 불러오기, 객체 생성
        self.setupUi(self)
        f = open('cheomdan.csv', 'rt', encoding='UTF8')  # 장덕.csv 파일 읽어옴
        self.rdr = csv.reader(f)
        self.csv_list = []  # 리스트 생성
        for line in self.rdr:
            self.csv_list.append(line)  # 리스트에 추가
        f.close()
        f = open('jangdeok.csv', 'rt', encoding='UTF8')   # 첨단.csv 파일 읽어옴
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)  # 리스트에 추가
        f.close()
        f = open('singa.csv', 'rt', encoding='cp949')  # 신가.csv 파일 읽어옴
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)  # 리스트에 추가
        f.close()
        f = open('taleflower.csv', 'rt', encoding='cp949')  #이야기꽃.csv 파일 읽어옴.
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)  # 리스트에 추가
        f.close()

        # stack의 페이지를 첫번째 페이지로 고정한다
        self.stackedWidget.setCurrentIndex(0)
        # 버튼의 클릭이벤트와 함수를 연결해준다
        self.btn_search.clicked.connect(self.MoveBooklistpage)  # 검색한 도서 리스트 페이지로 이동
        self.btn_back_search.clicked.connect(self.MoveSearchpage)   # 도서 조회 페이지로 이동
        self.btn_main.clicked.connect(self.MoveMainPage)    # 메인 페이지로 이동
        self.btn_main2.clicked.connect(self.MoveMainPage)   # 메인 페이지로 이동
        self.btn_search.clicked.connect(self.searchlist)    # 도서 조회 리스트 나타남
        self.bookname.textChanged.connect(self.booknameTextFunction)    # LineEdit 글자가 바뀔 때 기능 실행
        self.bookname.returnPressed.connect(self.printTextFunction) # LineEdit에서 Return키(Enter키)가 눌렸을 때 기능 실행
        self.bookpublisher.textChanged.connect(self.bookpublisherTextFunction)
        self.bookpublisher.returnPressed.connect(self.printTextFunction)
        self.bookwriter.textChanged.connect(self.bookwriterTextFunction)
        self.bookwriter.returnPressed.connect(self.printTextFunction)


    def MoveBooklistpage(self): # 검색 후 도서 리스트 나오는 페이지
        self.stackedWidget.setCurrentIndex(1)

    def MoveSearchpage(self):   # 도서 조회 페이지
        self.stackedWidget.setCurrentIndex(0)

    def MoveMainPage(self): # 메인페이지와 연결
        self.parent().setCurrentIndex(0)

    def booknameTextFunction(self): # 책 제목으로 검색 실행
        self.bookname.setText(self.bookname.text())

    def bookpublisherTextFunction(self):    # 출판사로 검색 실행
        self.bookpublisher.setText(self.bookpublisher.text())

    def bookwriterTextFunction(self):   # 작가로 검색 실행
        self.bookwriter.setText(self.bookwriter.text())

    def printTextFunction(self):    # 검색 후 출력 실행
        print(self.bookname.text())
        print(self.bookpublisher.text())
        print(self.bookwriter.text())

    def searchlist(self):   # 검색 리스트
        f = open('Rent_list.csv', 'rt', encoding='UTF8')  # 대여리스트.csv 파일 읽어옴
        self.rdr = csv.reader(f)
        self.bookrental = []    # 리스트 생성
        for line in self.rdr:
            self.bookrental.append(line)    # 대여 리스트에 추가
        f.close()
        book = []   # 리스트 생성
        bookname = self.bookname.text()
        bookpublisher = self.bookpublisher.text()
        bookwriter = self.bookwriter.text()

        for line in self.csv_list:
            if '도서명' == line[4]:    # 4번째 라인에 '도서명'이 있으면 재실행
                continue
            elif bookname in line[4] and bookpublisher in line[6] and bookwriter in line[5]:    # 제목이 4번째, 출판사가 6번째, 작가가 5번째에 있으면 검색 결과 리스트에 추가
                book.append(line)

        self.booksearchlist.setRowCount(len(book))
        Row = 0
        # Row = Row - 1
        for x in book:
            self.booksearchlist.setItem(Row, 0, QTableWidgetItem(x[0]))    # 연번
            self.booksearchlist.setItem(Row, 1, QTableWidgetItem(x[4]))    # 제목
            self.booksearchlist.setItem(Row, 2, QTableWidgetItem(x[5]))    # 저자
            self.booksearchlist.setItem(Row, 3, QTableWidgetItem(x[6]))    # 출판사
            self.booksearchlist.setItem(Row, 4, QTableWidgetItem(x[1]))    # 소장도서관
            self.booksearchlist.setItem(Row, 5, QTableWidgetItem(x[3]))    # 등록번호
            self.booksearchlist.setItem(Row, 6, QTableWidgetItem(x[8]))    # 청구기호
            self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출가능'))    # 자료상태
            self.booksearchlist.setItem(Row, 8, QTableWidgetItem('-'))  # 반납예정일자(없으면 '-'로 표시)
            if "첨단도서관" != x[1] :   # 도서관별로 수정 필요 ? ? ..
                self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출불가능(타도서관)'))

            for i in range(len(self.bookrental)):
                if self.bookrental[i][4] in x[4]:   # 대여 리스트 i줄 4번째에 제목이 있으면
                    self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출불가능'))  # 대출 불가능 출력
                    self.booksearchlist.setItem(Row, 8, QTableWidgetItem(self.bookrental[i][11]))   # bookrental 11번째에 있는 반납예정일자가 Row 8번째에 표시됨
                    break
                # elif "장덕도서관" != x[1]: #도서관이  다르면
                #     self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출불가능(타도서관)'))
                # elif self.bookrental[i][4] not in x[4]: # 대여 리스트 i줄 4번째에 제목이 없으면
                #     self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출가능'))   # 대출 가능 출력
                #     continue

            Row = Row + 1

if __name__ == "__main__" :
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = BooksearchClass()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()









