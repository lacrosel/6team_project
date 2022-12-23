import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

form_class = uic.loadUiType('./login.ui')[0]


class Login(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.checkStatus = False        # 회원가입페이지-중복확인 시 필요
        self.setupUi(self)
        self.id_lineEdit.setText("")
        self.login_SW.setCurrentIndex(1)        # 스택위젯
        self.login_Button.clicked.connect(self.Login_Check)        # 로그인페이지-로그인버튼
        self.signup_Button.clicked.connect(self.MoveSignupPage)     # 로그인페이지-회원가입버튼
        self.Home1_Button.clicked.connect(self.MoveMainPage)        # 로그인페이지-홈버튼
        self.Home2_Button.clicked.connect(self.MoveMainPage)        # 회원가입페이지-홈버튼
        self.join_Button.clicked.connect(self.Sign_Up)              # 회원가입페이지-가입하기버튼
        self.duplication_Button.clicked.connect(self.Double_Check)  # 회원가입페이지-중복확인버튼
        self.agree1_checkBox.toggled.connect(self.Check_Box)        # 회원가입페이지-전체동의
        # 숫자만 입력 받게하기 위해 추가
        self.onlyInt = QIntValidator()
        self.phone_lineEdit.setValidator(self.onlyInt)      # self. 다음에 적용할 lineEdit 객체명으로 변경

    def MoveMainPage(self):     # 메인페이지로 이동하는 함수
        self.login_SW.setCurrentIndex(1)
        self.parent().setCurrentIndex(0)

    def MoveSignupPage(self):       # 회원가입 페이지로 이동하는 함수
        self.login_SW.setCurrentIndex(2)

    def MoveLoginPage(self):        # 로그인 페이지로 이동하는 함수
        self.login_SW.setCurrentIndex(1)


    # 회원가입 함수
    def Double_Check(self):         # 회원가입 페이지-중복 확인하는 함수
        user = self.id_lineEdit.text()  # id_lineEdit에 입력되는 텍스트
        dc = 0  # 임의로 지정한 변수
        lines = open('Userinfo.txt', 'r').read().split('\n')      # txt 파일에 저장된 정보를 \n로 구분된 리스트로 만듦
        for i in range(len(lines)):
            data = lines[i].split('\n')         # lisnes[i] 값을 ','로 구분된 리스트로 만듦
            # data가 lines의 요소라서(Userinfo.txt의 한 줄) 정보를 다 읽은 후에 알림을 띄우려면 변수로 리턴값을 주고 조건문으로 알림창이 나오게 해야됨
            if (user + '\n') in lines:
                dc = 1      # 변수에 임의의 값 저장
                break
            elif (user + '\n') not in lines:
                dc = 2
                self.checkStatus = True
                break
            else:
                pass
        if dc == 1:
            QMessageBox.critical(self, "알림", "아이디 중복")
        elif dc == 2:
            QMessageBox.information(self, "알림", "사용 가능한 아이디")


    def Sign_Up(self):
        id = self.id_lineEdit.text()        # lineEdit에 입력받은 데이터
        pw1 = self.pw_lineEdit.text()
        pw2 = self.pw2_lineEdit.text()
        name = self.name_lineEdit.text()
        phone = self.phone_lineEdit.text()
        address = self.address_lineEdit.text()

        user = [id, pw1, name, phone, address]      # 정보 저장 순서

        with open('Userinfo.txt', 'a') as f:
            # 회원가입 시 필요한 조건
            if pw1 != pw2:
                QMessageBox.critical(self, "알림", "비밀번호가 일치하지 않습니다. 다시 확인해주세요")

            elif self.checkStatus == False:
                QMessageBox.critical(self, "알림", "아이디 중복 확인이 안 되어있습니다")

            elif id == '' or pw1 == '' or name == '' or phone == '' or address == '':
                QMessageBox.critical(self, "알림", "정보를 입력하세요")

            else:

                QMessageBox.information(self, "알림", "회원가입 됐습니다")
                f.writelines(f"\n{id},{pw1},{name},{phone},{address}")     # 사용자 정보 저장
                self.login_SW.setCurrentIndex(1)
                #Line_edit에 입력 받은 값 지워주기
                self.id_lineEdit.clear()
                self.pw_lineEdit.clear()
                self.pw2_lineEdit.clear()
                self.name_lineEdit.clear()
                self.phone_lineEdit.clear()
                self.address_lineEdit.clear()
                self.agree1_checkBox.setChecked(False)
                self.agree2_checkBox.setChecked(False)
                self.agree3_checkBox.setChecked(False)
                self.agree4_checkBox.setChecked(False)


    def Check_Box(self):
        if self.agree1_checkBox.isChecked() == True:
            self.agree2_checkBox.toggle()
            self.agree3_checkBox.toggle()
            self.agree4_checkBox.toggle()


    # 로그인
    def Login_Check (self):

        if self.login_id_lineEdit.text() == "":
            return
        self.id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()
        logined = 0
        lines = open('Userinfo.txt', 'r').read().split('\n')        # txt 파일에 저장된 정보를 \n로 구분된 리스트로 만듦
        for i in range(len(lines)):
            list = lines[i].split(',')          # lisnes[i] 값을 ','로 구분된 리스트로 만듦
            if self.id not in list[0]:       # list[0] = id
                logined = 1

            elif pw not in list[1]:     # list[1] = pw
                logined = 2
            else:
                logined = 3
                break       # 안해주면 마지막에 가입한 사람만 로그인 됨
            print(list)

        if logined == 1:
            QMessageBox.critical(self, "로그인 오류", "ID 정보가 없습니다. 회원가입 해주세요")
        elif logined == 2:
            QMessageBox.critical(self, "로그인 오류", "비밀번호를 다시 입력하세요")
        else:
            return True    # 로그인 성공



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Login()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()