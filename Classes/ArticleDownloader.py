import urllib.request
import re
from Loger import Loger


# работа с загрузкой страниц
class ArticalDownloader:

    # кодировка страницы
    @property
    def encodeArticle(self):
        return self._encodeArticle

    @encodeArticle.setter
    def encodeArticle(self, value):
        self._encodeArticle = value

    # загрузить страницу
    def DownloadPage(self, URL):
        try:
            Loger.GetInstance().WriteLog("Start download page")
            htmlPage = urllib.request.urlopen(URL).read()

            self.encodeArticle = self.GetEncode(htmlPage);
            Loger.GetInstance().WriteLog("Page Encode:" + self.encodeArticle)

            resultSource = str(htmlPage.decode(self.encodeArticle))
            return resultSource
        except Exception as e:
            Loger.GetInstance().WriteLog("Page not downlaod:" + str(e))
            return ""

    # получить кодировку
    def GetEncode(self, HTMLpage):

        listRegex = ["meta.*charset=(\"|.).*?\"",
                     "charset=(\"|.).*?\"",
                     "(\"|=)\S*\w"]
        encodeArticle = str(HTMLpage)
        for x in listRegex:
            temp = re.search(x, encodeArticle)
            encodeArticle = temp.group(0)
        return encodeArticle[1:]
