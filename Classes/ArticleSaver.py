import os
from Loger import Loger

#сохраняет страницу
class ArticleSaver:
    #сохранить в файл
    def WriteToFile(self,content,URL,encodeArticle):
        path=URL.replace('https://','').replace('http://','') .split('/')
        try:
            if not (path[len(path)-1] == ''):
                filename=path[len(path)-1]+'.txt'
            else:
                filename=path[len(path)-2]+'.txt'
            filename=filename.replace('.shtml','').replace('.html','').replace('.htm','')
            path.pop()

            fullPath= os.getcwd()
            for x in path:
               fullPath+="\\"+x+"\\"
               if not os.path.exists(fullPath):
                    os.makedirs(fullPath)
            f= open(fullPath+filename,"w+",encoding=encodeArticle)
            f.write(content)
            f.close()
            Loger.GetInstance().WriteLog("Save success")
        except Exception as e:
            Loger.GetInstance().WriteLog("Save error:"+str(e))
            pass

              