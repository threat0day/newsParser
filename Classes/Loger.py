from Settings import Settings
class Loger:

    __instance = None
    #получить инстанс Loger
    @staticmethod
    def GetInstance():

        if Loger.__instance == None:
           Loger()
        return Loger.__instance 

    def __init__(self):
        if Loger.__instance == None:
           Loger.__instance = self

    #пишем логи в консоль
    def WriteLog(self,mess):
       if  bool(Settings.GetInstance().writeLogs):
           print (mess)
