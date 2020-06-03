import os
from Loger import Loger


# сохраняет страницу
class ArticleSaver:

    def write_to_File(self, content, url, encode_article):
        """
        сохранить в файл
        :param content:
        :param url:
        :param encode_article:
        :return:
        """
        path = url.replace('https://', '').replace('http://', '').split('/')
        try:
            if not (path[len(path) - 1] == ''):
                filename = path[len(path) - 1] + '.txt'
            else:
                filename = path[len(path) - 2] + '.txt'
            filename = filename.replace('.shtml', '').replace('.html', '').replace('.htm', '')
            path.pop()

            full_path: str = os.getcwd()
            for x in path:
                full_path += "\\" + x + "\\"
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
            f = open(full_path + filename, "w+", encoding=encode_article)
            f.write(content)
            f.close()
            Loger.GetInstance().WriteLog("Save success")
        except Exception as e:
            Loger.GetInstance().WriteLog("Save error:" + str(e))
            pass
