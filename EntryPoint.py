import sys

# добавляем пути
sys.path.append("Classes")

from Settings import Settings
from ArticleWorker import ArticleWorker


def main():
    """
    точка входа
    :return:
    """
    Settings().GetInstance()
    Settings().LoadSettings()
    input_article = input('input url article: ')
    ArticleWorker(input_article).work()


main()
