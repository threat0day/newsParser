from ArticleDownloader import ArticalDownloader
from ArticleSaver import ArticleSaver
from ArticleBodyParser import ArticleBodyParser
from OutTextFormater import OutTextFormater
from Loger import Loger


class ArticleWorker:

    def __init__(self, url):
        """

       :param url:
       """
        self.url = url

        if not self.url:
            Loger.GetInstance().WriteLog('url not must be empty')
            raise Exception('url not must be empty')

    def work(self):
        dowloader = ArticalDownloader()
        content = dowloader.DownloadPage(self.url)
        sourceText = ArticleBodyParser().Parce(content)

        result = OutTextFormater().Format(sourceText)

        ArticleSaver().write_to_File(result, self.url, dowloader.encodeArticle)
