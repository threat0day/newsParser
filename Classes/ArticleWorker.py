from ArticleDownloader import ArticalDownloader
from ArticleSaver import ArticleSaver
from ArticleBodyParser import ArticleBodyParser
from OutTextFormater import OutTextFormater

#главный класс
class  ArticleWorker:
    def Work(self,URL):
       dowloader=ArticalDownloader();
       content=dowloader.DownloadPage(URL);
       sourceText=ArticleBodyParser().Parce(content)

       result=OutTextFormater().Format(sourceText)

       ArticleSaver().WriteToFile(result,URL,dowloader.encodeArticle);

 