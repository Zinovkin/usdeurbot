#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


"""
def hardworkz():
    import datetime
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    dates = (str(day) + '.' + str(month) + '.' + str(year))
    print(dates)

    read = open('usdeurz.txt', 'r')
    readdata = read.read()
    datez = readdata.find('date_req=')
    date0=readdata[datez+10:]
    datez = date0.find('date_req=')
    datez = date0[datez + 9:datez + 19]
    print(datez)
    read.close()
    print('\n')

    if datez!=dates:
        print('Получаем курсы с сайта')
        import urllib.request
        from bs4 import BeautifulSoup


        site1 = "http://www.cbr.ru/"
        print('Проверь, работет ли', site1)
        f = open('usdeurz.txt', 'w')

        def get_html(url):
            response = urllib.request.urlopen(url)
            return response.read()

        def parse(html):
            soup = BeautifulSoup(html, "lxml")
            table = soup.find_all('body')
            # print(soup.contents[1].contents[0].name)
            f.write(str(table))

        def main():
            parse(get_html(site1))

        if __name__ == '__main__':
            main()  # Конец парсинга

        fname0 = "usdeurz.txt"
        infile0 = open(fname0, 'r')
        data0 = infile0.read()

        usdpos = 'Доллар США'
        usdpos = data0.find(usdpos)

        europos = 'Евро'
        europos = data0.find(europos)

        udata0 = data0[usdpos:europos]

        edata0 = data0[europos:europos + 255]

        znak = '</i>'

        uznak = udata0.find(znak)
        ukurs = udata0[uznak+4:uznak+11]
        uznak = udata0[uznak - 1]

        usd1 = ukurs[0:2]
        usd1 = int(usd1)
        usd2 = ukurs[3:7]
        usd2 = int(usd2) * 0.0001
        usd = usd1 + usd2
        usd = round(usd, 4)


        eznak = edata0.find(znak)
        ekurs = edata0[eznak+4:eznak+11]
        eznak = edata0[eznak - 1]

        eur1 = ekurs[0:2]
        eur1 = int(eur1)
        eur2 = ekurs[3:7]
        eur2 = int(eur2) * 0.0001
        eur = eur1 + eur2
        eur = round(eur, 4)

        print('1 USD =', usd, '₽', uznak)
        print('1 EUR =', eur, '₽', eznak)

    else:
        print('Получаем курсы из usdeurz.txt')
        fname0 = "usdeurz.txt"
        infile0 = open(fname0, 'r')
        data0 = infile0.read()

        usdpos = 'Доллар США'
        usdpos = data0.find(usdpos)

        europos = 'Евро'
        europos = data0.find(europos)

        udata0 = data0[usdpos:europos]

        edata0 = data0[europos:europos + 255]

        znak = '</i>'

        uznak = udata0.find(znak)
        ukurs = udata0[uznak + 4:uznak + 11]
        uznak = udata0[uznak - 1]

        usd1 = ukurs[0:2]
        usd1 = int(usd1)
        usd2 = ukurs[3:7]
        usd2 = int(usd2) * 0.0001
        usd = usd1 + usd2
        usd = round(usd, 4)

        eznak = edata0.find(znak)
        ekurs = edata0[eznak + 4:eznak + 11]
        eznak = edata0[eznak - 1]

        eur1 = ekurs[0:2]
        eur1 = int(eur1)
        eur2 = ekurs[3:7]
        eur2 = int(eur2) * 0.0001
        eur = eur1 + eur2
        eur = round(eur, 4)

        print('1 USD =', usd, '₽')
        print('1 EUR =', eur, '₽')

    return usd,eur,uznak,eznak
hardworkz()


