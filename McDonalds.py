from sys import *
from PyQt5. QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QLabel, QVBoxLayout,QHBoxLayout,  QLineEdit,QRadioButton,QButtonGroup
from PyQt5 import QtGui

price1 = 61
price2 = 95
price3 = 32
price4 = 39
price5 = 53
price6 = 71
price7 = 44
price8 = 53
price9 = 28
price10 = 41
price11 = 48
price12 = 65
class Start(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("МакДональдс")
        self.resize(1920,1080)
        self.v = QVBoxLayout()
        self.text1 = QLabel(self)
        self.text1.setText("Вас вітає онлайн магазин МакДональдс,\n бажаємо вам приємних покупок!")
        self.text1.show()
        self.v.addWidget(self.text1,alignment = Qt.AlignCenter)
        self.picture = QtGui.QPixmap("fon.png")
        self.pict = QLabel()
        self.pict.setPixmap(self.picture)
        self.v.addWidget(self.pict,alignment=Qt.AlignCenter)
        self.text1.setFont(QtGui.QFont("Comic Sans",25))
        self.but = QPushButton(self)
        self.but.setText("Далі")
        self.but.show()
        self.v.addWidget(self.but,alignment = Qt.AlignCenter) 
        self.but.setFont(QtGui.QFont("Comic Sans",25))
        self.setLayout(self.v)

class McDonalds(QWidget):
    def __init__(self):
        super(McDonalds,self).__init__()
        self.setWindowTitle("McDonalds")
        self.resize(1920,1080)

        self.h1 = QHBoxLayout(self)

        self.v1 = QVBoxLayout(self)
        self.v2 = QVBoxLayout(self)
        self.v3 = QVBoxLayout(self)    
        self.v4 = QVBoxLayout(self) 
        self.v5 = QVBoxLayout(self) 

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.picture1 = QtGui.QPixmap("BigMac.jpg")
        self.picture2 = QtGui.QPixmap("bigtasty.jpg")
        self.picture3 = QtGui.QPixmap("cheeseburger.jpg")
        self.picture4 = QtGui.QPixmap("cheeseburgerbecon.jpg")

        self.pic1 = QLabel()
        self.pic2 = QLabel()
        self.pic3 = QLabel()
        self.pic4 = QLabel()

        self.pic1.setPixmap(self.picture1)
        self.pic2.setPixmap(self.picture2)
        self.pic3.setPixmap(self.picture3)
        self.pic4.setPixmap(self.picture4)

        self.v1.addWidget(self.pic1,alignment=Qt.AlignCenter)
        self.v2.addWidget(self.pic2,alignment=Qt.AlignCenter)
        self.v3.addWidget(self.pic3,alignment=Qt.AlignCenter)
        self.v4.addWidget(self.pic4,alignment=Qt.AlignCenter)
        self.but1 = QPushButton(str(price1)+"₴")
        self.v1.addWidget(self.but1,alignment = Qt.AlignCenter)
        self.but2 = QPushButton(str(price2)+"₴")
        self.v2.addWidget(self.but2,alignment = Qt.AlignCenter)
        self.but3 = QPushButton(str(price3)+"₴")
        self.v3.addWidget(self.but3,alignment = Qt.AlignCenter)
        self.but4 = QPushButton(str(price4)+"₴")
        self.v4.addWidget(self.but4,alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.picture5 = QtGui.QPixmap("doublecheeseburger.jpg")
        self.picture6 = QtGui.QPixmap("doubleroyalcheeseburger.jpg")
        self.picture7 = QtGui.QPixmap("fheshmcmaffin.jpg")
        self.picture8 = QtGui.QPixmap("fileofish.jpg")

        self.pic5 = QLabel()
        self.pic6 = QLabel()
        self.pic7 = QLabel()
        self.pic8 = QLabel()

        self.pic5.setPixmap(self.picture5)
        self.pic6.setPixmap(self.picture6)
        self.pic7.setPixmap(self.picture7)
        self.pic8.setPixmap(self.picture8)

        self.v1.addWidget(self.pic5,alignment=Qt.AlignCenter)
        self.v2.addWidget(self.pic6,alignment=Qt.AlignCenter)
        self.v3.addWidget(self.pic7,alignment=Qt.AlignCenter)
        self.v4.addWidget(self.pic8,alignment=Qt.AlignCenter)

        self.but5 = QPushButton(str(price5)+"₴")
        self.v1.addWidget(self.but5,alignment = Qt.AlignCenter)
        self.but6 = QPushButton(str(price6)+"₴")
        self.v2.addWidget(self.but6,alignment = Qt.AlignCenter)
        self.but7 = QPushButton(str(price7)+"₴")
        self.v3.addWidget(self.but7,alignment = Qt.AlignCenter)
        self.but8 = QPushButton(str(price8)+"₴")
        self.v4.addWidget(self.but8,alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)


        self.picture9 = QtGui.QPixmap("gamburger.jpg")
        self.picture10 = QtGui.QPixmap("mcchicken.jpg")
        self.picture11 = QtGui.QPixmap("mcchickenbecon.jpg")
        self.picture12 = QtGui.QPixmap("royalcheeseburger.jpg")

        self.pic9 = QLabel()
        self.pic10 = QLabel()
        self.pic11 = QLabel()
        self.pic12 = QLabel()

        self.pic9.setPixmap(self.picture9)
        self.pic10.setPixmap(self.picture10)
        self.pic11.setPixmap(self.picture11)
        self.pic12.setPixmap(self.picture12)

        self.v1.addWidget(self.pic9,alignment=Qt.AlignCenter)
        self.v2.addWidget(self.pic10,alignment=Qt.AlignCenter)
        self.v3.addWidget(self.pic11,alignment=Qt.AlignCenter)
        self.v4.addWidget(self.pic12,alignment=Qt.AlignCenter)

        self.but9 = QPushButton(str(price9)+"₴")
        self.v1.addWidget(self.but9,alignment = Qt.AlignCenter)
        self.but10 = QPushButton(str(price10)+"₴")
        self.v2.addWidget(self.but10,alignment = Qt.AlignCenter)
        self.but11 = QPushButton(str(price11)+"₴")
        self.v3.addWidget(self.but11,alignment = Qt.AlignCenter)
        self.but12 = QPushButton(str(price12)+"₴")
        self.v4.addWidget(self.but12,alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.b1 = QLabel()
        self.v1.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v2.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v3.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)

    
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel("Ціна вашого кошика")
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1.setFont(QtGui.QFont("Courier New",15))

        self.pokupka = 0
        self.price = QLabel(str(self.pokupka))
        self.v5.addWidget(self.price, alignment = Qt.AlignCenter)
        self.price.setFont(QtGui.QFont("Courier New",15))
        

        self.but13 = QPushButton("Buy")
        self.v5.addWidget(self.but13,alignment = Qt.AlignCenter)
        self.but13.setFont(QtGui.QFont("Courier New",15))
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v5.addWidget(self.b1, alignment = Qt.AlignCenter)

        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)
        self.h1.addLayout(self.v3)
        self.h1.addLayout(self.v4)
        self.h1.addLayout(self.v5)
        self.setLayout(self.h1)

class zamovlenya(QWidget):
    def __init__(self):
        super(zamovlenya,self).__init__()
        self.setWindowTitle("Оплата")
        self.resize(1920,1080)
        self.h1 = QHBoxLayout(self)
        self.v0 = QVBoxLayout(self)
        self.v1 = QVBoxLayout(self)
        self.v2 = QVBoxLayout(self)
        self.v3 = QVBoxLayout(self)
        self.v4 = QVBoxLayout(self)

        self.b1 = QLabel()
        self.v0.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v0.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.b1 = QLabel()
        self.v4.addWidget(self.b1, alignment = Qt.AlignCenter)
        self.ed1 = QLineEdit("Номер телефону")
        self.v1.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(400)
        self.ed1 = QLineEdit("Ім'я та фамілія")
        self.v3.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(400)
        self.ed1 = QLineEdit("Місто")
        self.v1.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(300)
        self.ed1 = QLineEdit("Адреса")
        self.v3.addWidget(self.ed1,alignment = Qt.AlignCenter)
        self.ed1.setMaximumWidth(300)
        self.but0 = QPushButton("Готово")
        self.v2.addWidget(self.but0,alignment = Qt.AlignCenter)

        self.h1.addLayout(self.v0)
        self.h1.addLayout(self.v1)
        self.h1.addLayout(self.v2)
        self.h1.addLayout(self.v3)
        self.h1.addLayout(self.v4)
        self.setLayout(self.h1)

class End(QWidget):
    def __init__(self):
        super(End,self).__init__()
        self.setWindowTitle("Успішно")
        self.resize(1920,1080)
        self.h1 = QVBoxLayout(self)

        self.rr = QLabel("Ваше замовлення прийнято\n через кілька хвилин вам подзвонить кур'єр\n дякуємо, що користуєтесь МакДональдсом")
        self.h1.addWidget(self.rr,alignment = Qt.AlignCenter)
        self.rr.setFont(QtGui.QFont("Courier New",15))
        self.but = QPushButton("Готово")
        self.h1.addWidget(self.but,alignment = Qt.AlignCenter)
        self.setLayout(self.h1)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')    
        self.v1 = QVBoxLayout(self)
        self.setLayout(self.v1)
    def win1(self):
        self.w1 = Start()
        self.w1.but.clicked.connect(self.win2)
        self.w1.but.clicked.connect(self.w1.close)
        self.w1.show()
    def click1(self):
        self.w2.pokupka += 61
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but1.setVisible(False)
    def click2(self):
        self.w2.pokupka += 95
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but2.setVisible(False)
    def click3(self):
        self.w2.pokupka += 32
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but3.setVisible(False)
    def click4(self):
        self.w2.pokupka += 39
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but4.setVisible(False)
    def click5(self):
        self.w2.pokupka += 53
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but5.setVisible(False)
    def click6(self):
        self.w2.pokupka += 71
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but6.setVisible(False)
    def click7(self):
        self.w2.pokupka += 44
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but7.setVisible(False)
    def click8(self):
        self.w2.pokupka += 53
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but8.setVisible(False)
    def click9(self):
        self.w2.pokupka += 28
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but9.setVisible(False)
    def click10(self):
        self.w2.pokupka += 41
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but10.setVisible(False)
    def click11(self):
        self.w2.pokupka += 48
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but11.setVisible(False)
    def click12(self):
        self.w2.pokupka += 65
        self.w2.price.setText(str(self.w2.pokupka)+"₴")
        self.w2.but12.setVisible(False)

    def win2(self):
        self.w2 = McDonalds()
        self.w2.show()
        self.w2.but1.clicked.connect(self.click1)
        self.w2.but2.clicked.connect(self.click2)
        self.w2.but3.clicked.connect(self.click3)
        self.w2.but4.clicked.connect(self.click4)
        self.w2.but5.clicked.connect(self.click5)
        self.w2.but6.clicked.connect(self.click6)
        self.w2.but7.clicked.connect(self.click7)
        self.w2.but8.clicked.connect(self.click8)
        self.w2.but9.clicked.connect(self.click9)
        self.w2.but10.clicked.connect(self.click10)
        self.w2.but11.clicked.connect(self.click11)
        self.w2.but12.clicked.connect(self.click12)
        self.w2.but13.clicked.connect(self.win3)
        self.w2.but13.clicked.connect(self.w2.close)

    def win3(self):
        self.w2 = zamovlenya()
        self.w2.show()
        self.w2.but0.clicked.connect(self.win4)
        self.w2.but0.clicked.connect(self.w2.close)
    def win4(self):
        self.w4 = End()
        self.w4.show()
        self.w4.but.clicked.connect(self.w4.close)
        
app = QApplication(argv)
w = MainWindow()
w.win1()
exit(app.exec_())