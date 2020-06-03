import re
from Settings import Settings


# форматирование текста
class OutTextFormater:
    # форматирует текст в соотвествии с требованиями
    def Format(self, resultArticle):
        listHref = re.findall('<a.*?\/a>+', resultArticle, re.DOTALL)
        insertURL = Settings.GetInstance().showURL
        for x in listHref:
            value = re.search('>.*?<', x).group(0)[1:len(re.search('>.*?<', x).group(0)) - 1]
            href = re.search('f=\".*?\"', x).group(0)[2:]
            replaceString = "[" + href + "] " + value
            if insertURL:
                resultArticle = re.sub(re.compile(x), replaceString, resultArticle)
            else:
                resultArticle = re.sub(re.compile(x), value, resultArticle)

        tempString = resultArticle.replace('&laquo;', '"').replace('&raquo;', '"').replace('&nbsp;&mdash;',
                                                                                           ' —').replace('&nbsp;', ' ')

        tempString = re.sub(re.compile('<p.*?>'), '', tempString)
        tempString = re.sub(re.compile('</p>|</h>|<h>'), '\n', tempString)
        i = 1
        j = 0
        curLen = len(resultArticle)

        wightText = int(Settings.GetInstance().wightText)
        insertTab = Settings.GetInstance().wightText

        buf = ''
        while i < curLen - 1:
            try:
                buf += tempString[i]
                if len(buf) == wightText - 2:
                    k = len(buf) - 1
                    if buf[k] == ' ':
                        index = i - (len(buf) - k - 1)
                        tempString = tempString[:index] + '\n' + tempString[index:]
                    else:
                        while not buf[k] is ' ':
                            if tempString[k] is '\n':
                                break
                            k -= 1
                        index = i - (len(buf) - k - 1)
                        tempString = tempString[:index] + '\n' + tempString[index:]
                    buf = ''
            except:
                pass
            i += 1

        tempString = re.sub(re.compile('<[^>]*>+'), '\n', tempString)
        resultArticle = tempString

        return resultArticle
