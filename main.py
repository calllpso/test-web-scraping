import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import requests
from bs4 import BeautifulSoup


class scrap(QtWidgets.QMainWindow):
    def __init__(self):
        super(scrap, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Web-scraper')

        self.ui.lineEdit.setPlaceholderText('url')
        self.ui.pushButton.clicked.connect(self.scrapping)

    def scrapping(self):
        url = self.ui.lineEdit.text()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div')
        with open('test-scrap.doc', 'w', encoding='utf-8') as output_file:
            for quote in quotes:
                print(quote.text)
                output_file.write(quote.text)
    
app = QtWidgets.QApplication([])
application = scrap()
application.show()

sys.exit(app.exec())
