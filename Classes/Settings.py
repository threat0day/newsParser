import configparser
import os
import distutils.util

#настройки приложения
class Settings:

    __instance = None
    #получить инстанс Settings
    @staticmethod
    def GetInstance():

        if Settings.__instance == None:
           Settings()
        return Settings.__instance 

    def __init__(self):
        writeLogs = True

        if Settings.__instance == None:
           Settings.__instance = self
  
    #если False, то логи не выводятся  
    @property
    def writeLogs(self):                       
        return self._writeLogs
    @writeLogs.setter
    def writeLogs(self, value):             
        self._writeLogs = value
    _writeLogs = True

    #ширина текста
    @property
    def wightText(self):                       
        return self._wightText
    @wightText.setter
    def wightText(self, value):             
        self._wightText = value
    _wightText = 80

    #Включать табуляцию в начале абзаца
    @property
    def beginTab(self):                       
        return self._beginTab
    @beginTab.setter
    def beginTab(self, value):             
        self._beginTab = value
    _beginTab = True

    #Показывать ссылки в тексте
    @property
    def showURL(self):                       
        return self._showURL
    @showURL.setter
    def showURL(self, value):             
        self._showURL = value
    _showURL = None

    #Загружает настройки из ini файла
    def LoadSettings(self):
        try:
            if os.path.isfile(os.getcwd() + "\\" + 'Settings.ini'):
                config = configparser.ConfigParser()
                config.read(os.getcwd() + "\\" + 'Settings.ini')
                    
                self.GetInstance().writeLogs = bool(distutils.util.strtobool(config['Common']['writeLogs']))
                self.GetInstance().showURL = bool(distutils.util.strtobool(config['Text']['showURL']))
                self.GetInstance().beginTab = bool(distutils.util.strtobool(config['Text']['beginTab']))
                self.GetInstance().wightText = int(config['Text']['wightText'])
                print("Settings load")
            else:
                self.InitIniFile()
        except Exception as e:
               print("Settings not load:" + str(e))

    #Сохраняет настройки в ini файл
    def SaveSettings(self):
        config = configparser.ConfigParser()
        config['Common']['writeLogs'] = str(self.writeLogs)
        config['Text']['showURL'] = str(self.showURL)
        config['Text']['beginTab'] = str(self.beginTab)
        config['Text']['wightText'] = self.wightText
        with open(os.getcwd() + "\\" + 'Settings.ini', 'w') as configfile:  
            config.write(configfile)

    #Значения настроек поумолчанию
    def InitIniFile(self):
        config = configparser.ConfigParser()
        config.add_section('Common')
        config['Common']['writeLogs'] = 'True'

        config.add_section('Text')
        config['Text']['showURL'] = 'True'
        config['Text']['beginTab'] = 'True'
        config['Text']['wightText'] = '80'

        with open(os.getcwd() + "\\" + 'Settings.ini', 'w') as configFile:  
            config.write(configFile)


