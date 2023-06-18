import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()#bunu söylediğimde QtWidgets.QWidget ta bulunan tüm özellikleri miras alır
        self.init_ui()

    def init_ui(self):
        self.username_correct="Ali Demirci"
        self.password_correct="12345"
        self.username=QtWidgets.QLineEdit()# bu input sağlıyor
        self.password=QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)#bu da şifrenin yıldızlarla gösterilmesini sağlar
        self.enter=QtWidgets.QPushButton("Giriş yap")
        self.message=QtWidgets.QLabel("")


        horizontalLayout=QtWidgets.QHBoxLayout()
        horizontalLayout.addStretch()
        horizontalLayout.addWidget(self.username)
        horizontalLayout.addWidget(self.password)
        horizontalLayout.addWidget(self.enter)
        horizontalLayout.addWidget(self.message)
        horizontalLayout.addStretch()

        verticalLayout=QtWidgets.QHBoxLayout()
        verticalLayout.addStretch()
        verticalLayout.addLayout(horizontalLayout)
        verticalLayout.addStretch()

        self.enter.clicked.connect(self.click)


        self.setLayout(verticalLayout)
        self.setWindowTitle("Kullanıcı Girişi")

        self.show()

    def click(self):
        if self.username.text()==self.username_correct and self.password.text()==self.password_correct:#burada ki .text() veriyi düzgün veritipte almamız için önemli. Çünkü QLineEdit veritipindeki veriyi kullanıcıdan alablmemiz için böyle yapmalıyız
            self.message.setText("Hoşgeldiniz "+self.username.text())
        else:
            self.message.setText("kullanıcı adı ya da parola hatalı!")

app=QtWidgets.QApplication(sys.argv)

window=Window()

sys.exit(app.exec_())