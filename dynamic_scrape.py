import sys 
from PyQt4.QtGui import QApplication 
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage  
from bs4 import BeautifulSoup 
import urllib.request 
import lxml 


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()


url = "https://pythonprogramming.net/parsememcparseface/"

# url = "https://www.artsy.net/015-gallery/artists"
# url = "https://www.artsy.net/015-gallery/contact"
# url = "https://newyork.craigslist.org/search/bbb?query=python%20tutor&sort=rel"
client_response = Client(url) 
source = client_response.mainFrame().toHtml()

soup = BeautifulSoup(source, "lxml")
Email = soup.find('div', class_="partner2-content")
js_test = soup.find('p', class_="jstest").text 
print(js_test)
# print(Email)
# print(soup)
# print(source)
