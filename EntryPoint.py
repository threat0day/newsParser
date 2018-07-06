import sys

#добавляем пути
sys.path.append("Classes")

from Loger import Loger
from Settings import Settings
from ArticleWorker import ArticleWorker

#точка входа
def main():
    Settings().GetInstance();
    Settings().LoadSettings()
    Loger.GetInstance();
    inputArticle = input('input url article: ')
    if (inputArticle!=''):
        ArticleWorker().Work(inputArticle)
    else:
        Loger.GetInstance().WriteLog('url not must be empty');
    return 0;

main();
