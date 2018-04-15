
"""
tochka = data3.find('.')
zapyataya = data3.find(',')


if tochka == -1 and zapyataya == -1:
            if data3.isdigit()==True:
                chislo=int(data3)
            else: chislo =0

if tochka >= 0 and zapyataya == -1:
            if tochka == 0:
               data4 = data3[1:len(data3)]
               if data4.isdigit() == True:
                   koef = len(data4)
                   chislo = int(data4)*10**(-koef)
               else:
                   chislo =0
            if tochka >0:
                data4=data3[0:tochka]
                data5 = data3[tochka+1:len(data3)]
                if data4.isdigit()==True and data5.isdigit()==True:
                    koef = len(data5)
                    chislo = int(data4)+(int(data5)*10**(-koef))
                else:
                    chislo=0

if zapyataya >=0 and tochka==-1:
            if zapyataya == 0:
                data4 = data3[1:len(data3)]
                if data4.isdigit()==True:
                    koef = len(data4)
                    chislo=int(data4)*10**(-koef)
                else:
                    chislo=0
            if zapyataya>0:
                data4 = data3[0:zapyataya]
                data5 = data3[zapyataya + 1:len(data3)]
                if data4.isdigit()==True and data5.isdigit()==True:
                    koef = len(data5)
                    chislo=int(data4)+(int(data5)*10**(-koef))
                else:
                    chislo=0"""
def hardwork1():
    import datetime
    import urllib.request
    from bs4 import BeautifulSoup
    """Работа с датой для сайта"""
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    year = now.year
    month = now.month
    day = now.day
    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)
    dates = (str(day) +'/'+ str(month) +'/'+ str(year))
    dates1 = (str(day)  + str(month) + str(year))
    print('\n', '------------------------------------------------------')

    read = open('usdeur.txt', 'r')
    readdata = read.read()
    readdata1 = readdata.find('mydate="')
    dataeurusd=readdata[readdata1+8:readdata1+16]

    read.close()

    if dataeurusd!=dates1:
        print('Получаем курсы с сайта')
        """Работа с сайтом, получение курса USD и EUR"""
        site = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + dates
        print('Проверь, работет ли', site)
        f = open('usdeur.txt', 'w')

        def get_html(url):
            response = urllib.request.urlopen(url)
            return response.read()

        def parse(html):
            soup = BeautifulSoup(html, "lxml")
            table = soup.find_all('body')
            # print(soup.contents[1].contents[0].name)
            f.write(str(table))

        def main():
            parse(get_html(site))

        if __name__ == '__main__':
            main()

        f.close()

        f=open('usdeur.txt', 'a')
        f.write(' mydate="'+str(dates1)+'"')
        f.close()

        fname = "usdeur.txt"
        infile = open(fname, 'r')
        data = infile.read()

        data = data.replace('<', '')
        data = data.replace('>', '')
        data = data.replace('value', '')
        data = data.replace('/', '')
        data = data.replace('charcode', '')
        data = data.replace('nominal', '')
        data = data.replace('name', '')
        data = data.replace('numcode', '')
        data = data.replace('valute', '')
        data = data.replace('\n', ' ')
        data = data.replace('[bodyvalcurs', '')
        f = open('usdeur.txt', 'w')
        f.write(data)
        f.close()
        course1 = '1 Доллар США '
        course1 = data.find(course1)
        course2 = '1 Евро '
        course2 = data.find(course2)

        usd = data[course1 + 13:course1 + 20]
        usd1 = usd[0:2]
        usd1 = int(usd1)
        usd2 = usd[3:7]
        usd2 = int(usd2) * 0.0001
        usd = usd1 + usd2
        usd = round(usd, 4)

        eur = data[course2 + 7:course2 + 14]

        eur1 = eur[0:2]
        eur1 = int(eur1)
        eur2 = eur[3:7]
        eur2 = int(eur2) * 0.0001
        eur = eur1 + eur2
        eur = round(eur, 4)

        print('1 USD =', usd, '₽')
        print('1 EUR =', eur, '₽')
    else:
        print('Получаем курсы из usdeur.txt')
        f = open('usdeur.txt', 'r')
        data=f.read()
        f.close()
        course1 = '1 Доллар США '
        course1 = data.find(course1)
        course2 = '1 Евро '
        course2 = data.find(course2)

        usd = data[course1 + 13:course1 + 20]
        usd1 = usd[0:2]
        usd1 = int(usd1)
        usd2 = usd[3:7]
        usd2 = int(usd2) * 0.0001
        usd = usd1 + usd2
        usd = round(usd, 4)

        eur = data[course2 + 7:course2 + 14]
        eur1 = eur[0:2]
        eur1 = int(eur1)
        eur2 = eur[3:7]
        eur2 = int(eur2) * 0.0001
        eur = eur1 + eur2
        eur = round(eur, 4)

        print('1 USD =', usd, '₽')
        print('1 EUR =', eur, '₽')

    return usd, eur

x=hardwork1()
