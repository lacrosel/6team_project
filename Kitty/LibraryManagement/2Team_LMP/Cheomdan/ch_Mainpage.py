import sys
import random

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, QObject, QEvent

from bookrentalqt import Rental_page
from login import Login
from bookqt import BooksearchClass
# from selenium import webdriver
import webbrowser

form_class = uic.loadUiType('./Mainpage.ui')[0]  # 페이지 UI불러옴

# 이벤트 핸들러 생성 #사용자 정의 시그널 사용
# connect(instance) Q~클래스로 만들어진 객체를 가지고 옴.
def connect(widget):
    # Filter라는 클래스를 생성하고 Qobject모듈을 상속한다
    class Filter(QObject):
        clicked = pyqtSignal()  # clicked는 pyqtSinal()클래스로 생성 # 반드시 클래스 변수로 선언해야함.

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.MouseButtonPress:
                self.clicked.emit()
                return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class Main(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        loginpage.loginStatus = False
        Notice_image = QPixmap("Notice.png")  # Qpixmap으로 Notice_image 객체 생성
        self.notice.setPixmap(Notice_image)  # Notice_image를 notice 라벨 객체에 넣어줌
        event_image = QPixmap("event2.png")
        self.even_cal2.setPixmap(event_image)
        Facil1 = QPixmap("Fac1.PNG")  # 위와 같음.
        Facil2 = QPixmap("Fac2.PNG")
        Facil3 = QPixmap("Fac3.PNG")
        book1 = QPixmap("rec_Book1.PNG")
        book2 = QPixmap("rec_Book2.PNG")
        book3 = QPixmap("rec_Book3.PNG")
        book4 = QPixmap("rec_Book4.PNG")
        book5 = QPixmap("rec_Book5.PNG")
        Calendar = QPixmap("calendar.PNG")
        connect(self.notice).connect(self.openURL)  # 공지사항 누를시 웹페이지로 연결
        self.FacilityINFO.setCurrentIndex(0)  # 시설정보의 스택 페이지를 0으로 설정
        self.rv = random.randint(0, 4)  # 추천도서의 스택위젯을 랜덤으로 설정하기 위하여 random으로 줌
        self.bookPage.setCurrentIndex(self.rv)  # 상동
        self.Fac_1.setPixmap(Facil1)
        self.Fac_2.setPixmap(Facil2)
        self.Fac_3.setPixmap(Facil3)
        self.bookpic1.setPixmap(book1)
        self.bookpic2.setPixmap(book2)
        self.bookpic3.setPixmap(book3)
        self.bookpic4.setPixmap(book4)
        self.bookpic5.setPixmap(book5)
        connect(self.bookpic1).connect(self.recommendBook1) #추천도서 검색해줌
        connect(self.bookpic2).connect(self.recommendBook2)
        connect(self.bookpic3).connect(self.recommendBook3)
        connect(self.bookpic4).connect(self.recommendBook4)
        connect(self.bookpic5).connect(self.recommendBook5)
        self.even_cal.setPixmap(Calendar)
        self.Loginstack.setCurrentIndex(0) #기본적으로 로그인 / 회원가입이 보이게 해줌
        loginpage.login_Button.pressed.connect(self.changelog_Stat)  # 만약 로그인 페이지의 로그인 버튼을 누르면 change_Stat을 불러옴!!
        self.btn_Next_f3.clicked.connect(self.MoveFirstPage)  # 시설정보 바꿔주는 버튼
        self.btn_Next_f1.clicked.connect(self.MoveSecondPage)
        self.btn_Next_f2.clicked.connect(self.MoveThirdPage)
        self.btn_Login1234.clicked.connect(self.Moveloginpage)  # 로그인/회원가입 누르면 로그인페이지로 이동
        self.rentReturn.clicked.connect(self.MoveRentalpage)  # 대여 페이지로 이동
        self.searchBook.clicked.connect(self.Movesearchpage)  # 조회 페이지로 이동

    def recommendBook1(self):
        Booksearchpage.bookname.setText("누가 내 치즈를 옮겼을까")
        Booksearchpage.searchlist()
        widget.setCurrentIndex(3)
        Booksearchpage.stackedWidget.setCurrentIndex(1)
    def recommendBook2(self):
        Booksearchpage.bookname.setText("트렌드 코리아")
        Booksearchpage.searchlist()
        widget.setCurrentIndex(3)
        Booksearchpage.stackedWidget.setCurrentIndex(1)
    def recommendBook3(self):
        Booksearchpage.bookname.setText("불편한 편의점")
        Booksearchpage.searchlist()
        widget.setCurrentIndex(3)
        Booksearchpage.stackedWidget.setCurrentIndex(1)
    def recommendBook4(self):
        Booksearchpage.bookname.setText("세븐 테크")
        Booksearchpage.searchlist()
        widget.setCurrentIndex(3)
        Booksearchpage.stackedWidget.setCurrentIndex(1)
    def recommendBook5(self):
        Booksearchpage.bookname.setText("시선으로부터")
        Booksearchpage.searchlist()
        widget.setCurrentIndex(3)
        Booksearchpage.stackedWidget.setCurrentIndex(1)

    def changelog_Stat(self):
        login_check = loginpage.Login_Check()  # 12.21 추가함
        if login_check == True:
            loginpage.loginStatus = True  # 로그인이 완료된다면 로그인페이지에서 넘어올떄 로그인 스테이터스를 바꿔줌.
            self.label_logined.setText(f"{loginpage.id}님 환영합니다")
            self.parent().setCurrentIndex(0)  # 메인페이지로 이동
            self.Loginstack.setCurrentIndex(1)  # 로그인스택 ㅇㅇㅇ 안녕하세요 뜨게함
            Rentalpage.id = loginpage.id
            print(Rentalpage.id)
    def Messagebox(self):
        QMessageBox.information(self, "반납페이지", "로그인해야 이동가능합니다")  # 이거 떠야되는데안뜸 #메세지박스생성

    def openURL(self):
        webbrowser.open_new("https://lib.gwangsan.go.kr/CD/board/3")  # 공지사항으로 이동

    def MoveFirstPage(self):
        self.FacilityINFO.setCurrentIndex(0)  # 시설정보 이동

    def MoveSecondPage(self):
        self.FacilityINFO.setCurrentIndex(1)  # 시설정보 이동

    def MoveThirdPage(self):
        self.FacilityINFO.setCurrentIndex(2)  # 시설정보 이동

    def Moveloginpage(self):
        widget.setCurrentIndex(1)  # 로그인페이지로 이동

    def MoveRentalpage(self):  # 대여 페이지로 이동

        if loginpage.loginStatus == True:  # 로그인페이지의 로그인스테이터스가 참이면 이동
            widget.setCurrentIndex(2)
        else:  # 아니면 메세지박스 나옴
            self.Messagebox()

    def Movesearchpage(self):  # 검색페이지로 이동
        widget.setCurrentIndex(3)
        Booksearchpage.bookname.setText("")
        Booksearchpage.stackedWidget.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()  # StackedWidget 생성

    loginpage = Login()  # 로그인페이지의 로그인 클래스를 불러와서 객체 생성
    Rentalpage = Rental_page()  # 상동
    Booksearchpage = BooksearchClass()  # 상동
    mainWindow = Main()  # 상동

    widget.addWidget(mainWindow)  # stackedwidget에 객체 페이지를 넣어줌.
    widget.addWidget(loginpage)
    widget.addWidget(Rentalpage)
    widget.addWidget(Booksearchpage)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    sys.exit(app.exec_())
