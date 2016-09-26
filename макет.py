import os
import urllib.request as ur
import time

def gethtml(adress):
    address = ''
    try:
        page = ur.urlopen(address)
        text = page.read().decode('ISO-8859-1')
        print('PAGE EXISTS')
    except:
        print('None')

def writefile(text):

def get_text(page):
    # функция которая используется много раз, чтобы достать что-то из текста.
    # например имя автора или даты написания статьи

def cleantext(text):
    k = []
    for line in s:
        words = line.split(' ')
        for word in words:
            word = word.lower()
            word = word.strip(',.<>?/\'":;#№!~\n\t[]{}*+-_()1234567890=')
            if word != '':
                k.append(word)
    print(' '.join(k))

def mystemm():
    #аргумент - это путь
    # в такую-то папку пиши html, а втакую-то папку пиши тексты

def main():
#вставить в цикле time.sleep()
#здесь будет лежать цикл, перебирающий страницы

if __name__ == '__main__':
    main() 
