from Loger import Loger
import re
import html.parser

#парсит текст
class ArticleBodyParser:
    #очищает полученную страницу от других элементов, кроме текста
    def Parce(self, content):
        listGarbage=["<!--.*?-->|<script[^>]*>([^<]+)</script>|<script(.*)\/script>|<script(.*)\/>|<meta(.*)\/>|<link(.*)\/>|<nav(.*)\/nav>",
                 # "<noscript[^>]*>([^<]+)</noscript>|<noscript(.*)\/noscript>|<noscript(.*)\/>|<footer.*?([\s\S]*)\<\/footer\>|<symbol.*?([\s\S]*)\<\/symbol\>",
                 "<img.*?\/>",
                 "<svg.*?\/svg>",
                #"<script.*?([\s\S]*)?<\/script\>",//косячит
                 "<style[^>]*>([^<]+)</style>|<style(.*)\/style>",
                 "<footer.*?([\s\S]*)\<\/footer\>",
                 "<aside.*?\/aside>",
                 "<time.*?\/time>",
                 "<span.*?\/span>",
                 "<link.*?>",
                 "<blockquote.*?>",
                 "<link.*?\/link>",
                 "<iframe.*?\/iframe>",
                 "<li.*?\/li>",
                 "<style.*?\/style>",
                "<script[\s\S]+?/script>",
                "^\s+|\n|\r|\s+$",
                "<!\[.*?\]>",
                "<!--.*?-->",
                "<noscript[^>]*>([^<]+)</noscript>|<noscript(.*)\/noscript>|<noscript(.*)\/>",
                "<header.*?([\s\S]*)\<\/header\>",
                  ]
        result=content;
        for x in listGarbage:
           cleanr=re.compile(x) 
           temp=re.sub(cleanr,'', result)
           result=temp

        try:
            paragraph=r'<p.*\/p>';
            temp = re.search(paragraph, result)
            result=temp.group(0)
        except Exception as e:
            Loger.GetInstance().WriteLog("ArticleBodyParser:"+str(e));

        result.replace('\n', '').replace('\r', '').replace('\t','')
        result=re.sub(re.compile('<div.*?\/div>'),'', result)
        return result;
