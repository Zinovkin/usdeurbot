#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Команды бота
start - Старт
help - Помощь
getcourses - Получить курс $, € и нефти
devlog - Лог разработки
usdtorub - Доллары в рубли
rubtousd - Рубли в доллары
eurtorub - Евро в рубли
rubtoeur - Рубли в евро
В разработке:
"""

import constants
import telebot
from flask import Flask, request
import logging
bot = telebot.TeleBot(constants.token)
import os

ids =[]
commands1 =[]
commands2 = []
commands3 =[]
commands4 = []

print(bot.get_me())

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

def log(message):
    print("\n")
    from datetime import datetime
    logfile = open('logfile.txt', 'a')
    logs2 = "Сообщение от {0} {1}; (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id),message.text)
    logs = '\n'+'\n'+' '+str(datetime.now())+' '+logs2

    logfile.write(logs)
    print('------------------------------------------------------')
    print(datetime.now())
    print("Сообщение от {0} {1}; (id = {2}) \n Текст = {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id),message.text))
    logfile.close()
    print('------------------------------------------------------')

#Клавиатура
user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
user_markup.row('/start', 'Hide the keyboard', '/help')
user_markup.row('/getcourses','/devlog')
user_markup.row('/usdtorub', '/rubtousd')
user_markup.row('/eurtorub', '/rubtoeur')

@bot.message_handler(commands=['start']) # Старт
def handle_text(message):
    answer = "Вас приветствует HunkyBot v1.8"
    log(message)
    bot.send_message(message.from_user.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['help']) # Помощь
def handle_text(message):
    answer = "HunkyBot умеет многое. Чтобы знать всё о нём, посмотри devlog, ткнув сюда /devlog"
    log(message)
    bot.send_message(message.chat.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['getcourses']) # Курсы валют и нефти
def handle_text(message):
    peremen = hardworkz()
    usd = peremen[0]
    eur = peremen[1]
    uznak=peremen[2]
    eznak=peremen[3]
    answer = '1 USD = ' + str(usd) +'₽'+' ' +str(uznak)+'\n' '1 EUR = '+ str(eur)+'₽'+' '+str(eznak)
    log(message)
    bot.send_message(message.chat.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['devlog']) # Лог разработки
def handle_text(message):
    f2name = "devlog.txt"
    infile = open(f2name, 'r')
    devlog = infile.read()
    answer = devlog
    log(message)
    bot.send_message(message.chat.id, answer, reply_markup=user_markup)

@bot.message_handler(commands=['usdtorub'])
def handle_text(message):
    answer = "Введи количество $, которое хочешь перевести в ₽"
    ids.append(message.chat.id)
    commands1.append('usdtorub')
    log(message)
    bot.send_message(message.chat.id,answer)

@bot.message_handler(commands=['rubtousd'])
def handle_text(message):
    answer = "Введи количество ₽, которое хочешь перевести в $"
    ids.append(message.chat.id)
    commands2.append('rubtousd')
    log(message)
    bot.send_message(message.chat.id,answer)

@bot.message_handler(commands=['eurtorub'])
def handle_text(message):
    answer = "Введи количество €, которое хочешь перевести в ₽"
    ids.append(message.chat.id)
    commands3.append('eurtorub')
    log(message)
    bot.send_message(message.chat.id,answer)

@bot.message_handler(commands=['rubtoeur'])
def handle_text(message):
    answer = "Введи количество ₽, которое хочешь перевести в €"
    ids.append(message.chat.id)
    commands4.append('rubtoeur')
    log(message)
    bot.send_message(message.chat.id,answer)

@bot.message_handler(content_types=['text']) # Если текст

def handle_text(message):

    if message.text == "Hide the keyboard" and message.chat.id not in ids:
        answer = "Keyboard is hidden"
        hide_markup = telebot.types.ReplyKeyboardRemove()
        log(message)
        bot.send_message(message.from_user.id, answer, reply_markup=hide_markup)

    elif message.chat.id not in ids:
        answer = 'Не понял тебя'
        log(message)
        bot.send_message(message.chat.id, answer)

    elif  message.chat.id in ids:

        peremen = hardworkz()
        usd = peremen[0]
        eur = peremen[1]

        #Считывание присланной строки
        f3 = open('insert.txt', 'w')
        f3.write(message.text)
        f3.close()

        f3 = "insert.txt"
        infile = open(f3, 'r')
        data3 = infile.read()

        messagee=data3

        plus = messagee.find('+')
        minus = messagee.find('-')
        umnozh = messagee.find('*')
        divide = messagee.find('/')

        chislo = 0
        if plus >= 0 and minus == -1 and umnozh == -1 and divide == -1:
            messagee = messagee.split("+")
            for i in range(len(messagee)):
                tochka = messagee[i].find('.')
                zapyataya = messagee[i].find(',')
                if tochka == -1 and zapyataya == -1:
                    if messagee[i].isdigit() == True:
                        messagee[i] = int(messagee[i])
                    else:
                        messagee[i] = 0

                if tochka >= 0 and zapyataya == -1:
                    if tochka == 0:
                        data4 = messagee[i][1:len(data3)]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            chislo = 0
                    if tochka > 0:
                        data4 = messagee[i][0:tochka]
                        data5 = messagee[i][tochka + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0

                if zapyataya >= 0 and tochka == -1:
                    if zapyataya == 0:
                        data4 = messagee[i][1:len(messagee[i])]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            messagee[i] = 0
                    if zapyataya > 0:
                        data4 = messagee[i][0:zapyataya]
                        data5 = messagee[i][zapyataya + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0
                data3 = 0
            for i in range(len(messagee)):
                data3 = messagee[i] + data3
            chislo = data3

        if plus == -1 and minus >= 0 and umnozh == -1 and divide == -1:
            messagee = messagee.split("-")
            for i in range(len(messagee)):
                tochka = messagee[i].find('.')
                zapyataya = messagee[i].find(',')
                if tochka == -1 and zapyataya == -1:
                    if messagee[i].isdigit() == True:
                        messagee[i] = int(messagee[i])
                    else:
                        messagee[i] = 0

                if tochka >= 0 and zapyataya == -1:
                    if tochka == 0:
                        data4 = messagee[i][1:len(data3)]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            chislo = 0
                    if tochka > 0:
                        data4 = messagee[i][0:tochka]
                        data5 = messagee[i][tochka + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0

                if zapyataya >= 0 and tochka == -1:
                    if zapyataya == 0:
                        data4 = messagee[i][1:len(messagee[i])]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            messagee[i] = 0
                    if zapyataya > 0:
                        data4 = messagee[i][0:zapyataya]
                        data5 = messagee[i][zapyataya + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0
                data3 = 0
            for i in range(len(messagee)):
                if i == 0:
                    continue
                data3 = messagee[i] + data3
            data3 = messagee[0] - data3
            chislo = data3

        if plus == -1 and minus == -1 and umnozh >= 0 and divide == -1:
            messagee = messagee.split("*")
            for i in range(len(messagee)):
                tochka = messagee[i].find('.')
                zapyataya = messagee[i].find(',')
                if tochka == -1 and zapyataya == -1:
                    if messagee[i].isdigit() == True:
                        messagee[i] = int(messagee[i])
                    else:
                        messagee[i] = 0

                if tochka >= 0 and zapyataya == -1:
                    if tochka == 0:
                        data4 = messagee[i][1:len(data3)]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            chislo = 0
                    if tochka > 0:
                        data4 = messagee[i][0:tochka]
                        data5 = messagee[i][tochka + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0

                if zapyataya >= 0 and tochka == -1:
                    if zapyataya == 0:
                        data4 = messagee[i][1:len(messagee[i])]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            messagee[i] = 0
                    if zapyataya > 0:
                        data4 = messagee[i][0:zapyataya]
                        data5 = messagee[i][zapyataya + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0
                data3 = messagee[0]
            for i in range(len(messagee)):
                if i == 0:
                    continue
                data3 = messagee[i] * data3
            chislo = data3

        if plus == -1 and minus == -1 and umnozh == -1 and divide >= 0:
            messagee = messagee.split("/")
            for i in range(len(messagee)):
                tochka = messagee[i].find('.')
                zapyataya = messagee[i].find(',')
                if tochka == -1 and zapyataya == -1:
                    if messagee[i].isdigit() == True:
                        messagee[i] = int(messagee[i])
                    else:
                        messagee[i] = 0

                if tochka >= 0 and zapyataya == -1:
                    if tochka == 0:
                        data4 = messagee[i][1:len(data3)]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            chislo = 0
                    if tochka > 0:
                        data4 = messagee[i][0:tochka]
                        data5 = messagee[i][tochka + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0

                if zapyataya >= 0 and tochka == -1:
                    if zapyataya == 0:
                        data4 = messagee[i][1:len(messagee[i])]
                        if data4.isdigit() == True:
                            koef = len(data4)
                            messagee[i] = int(data4) * 10 ** (-koef)
                        else:
                            messagee[i] = 0
                    if zapyataya > 0:
                        data4 = messagee[i][0:zapyataya]
                        data5 = messagee[i][zapyataya + 1:len(messagee[i])]
                        if data4.isdigit() == True and data5.isdigit() == True:
                            koef = len(data5)
                            messagee[i] = int(data4) + (int(data5) * 10 ** (-koef))
                        else:
                            messagee[i] = 0
                data3 = messagee[0]
            for i in range(len(messagee)):
                if i == 0:
                    continue
                data3 = data3 / messagee[i]

            chislo = data3

        if plus == -1 and minus == -1 and umnozh == -1 and divide == -1:
            data3 = messagee
            tochka = data3.find('.')
            zapyataya = data3.find(',')

            if tochka == -1 and zapyataya == -1:
                if data3.isdigit() == True:
                    chislo = int(data3)
                else:
                    chislo = 0

            if tochka >= 0 and zapyataya == -1:
                if tochka == 0:
                    data4 = data3[1:len(data3)]
                    if data4.isdigit() == True:
                        koef = len(data4)
                        chislo = int(data4) * 10 ** (-koef)
                    else:
                        chislo = 0
                if tochka > 0:
                    data4 = data3[0:tochka]
                    data5 = data3[tochka + 1:len(data3)]
                    if data4.isdigit() == True and data5.isdigit() == True:
                        koef = len(data5)
                        chislo = int(data4) + (int(data5) * 10 ** (-koef))
                    else:
                        chislo = 0

            if zapyataya >= 0 and tochka == -1:
                if zapyataya == 0:
                    data4 = data3[1:len(data3)]
                    if data4.isdigit() == True:
                        koef = len(data4)
                        chislo = int(data4) * 10 ** (-koef)
                    else:
                        chislo = 0
                if zapyataya > 0:
                    data4 = data3[0:zapyataya]
                    data5 = data3[zapyataya + 1:len(data3)]
                    if data4.isdigit() == True and data5.isdigit() == True:
                        koef = len(data5)
                        chislo = int(data4) + (int(data5) * 10 ** (-koef))
                    else:
                        chislo = 0
            print(chislo)

        if 'usdtorub' in commands1:
            chislo = chislo + 0
            if chislo > 0:
                moneys = chislo * usd
                moneys = round(moneys, 2)
                answer = str(moneys) + ' ₽'
            if chislo == 0:
                answer = 'Введи нормальное число'
            log(message)
            bot.send_message(message.chat.id, answer)
            ids.remove(message.chat.id)
            commands1.remove('usdtorub')

        if 'rubtousd' in commands2:
            chislo = chislo + 0
            if chislo > 0:
                moneys = chislo / usd
                moneys = round(moneys, 2)
                answer = str(moneys) + ' $'
            if chislo == 0:
                answer = 'Введи нормальное число'
            log(message)
            bot.send_message(message.chat.id, answer)
            ids.remove(message.chat.id)
            commands2.remove('rubtousd')

        if 'eurtorub' in commands3:
            chislo = chislo + 0
            if chislo > 0:
                moneys = chislo *eur
                moneys = round(moneys, 2)
                answer = str(moneys) + ' ₽'
            if chislo == 0:
                answer = 'Введи нормальное число'
            log(message)
            bot.send_message(message.chat.id, answer)
            ids.remove(message.chat.id)
            commands3.remove('eurtorub')

        if 'rubtoeur' in commands4:
                chislo = chislo + 0
                if chislo > 0:
                    moneys = chislo / eur
                    moneys = round(moneys, 2)
                    answer = str(moneys) + ' €'
                if chislo == 0:
                    answer = 'Введи нормальное число'
                log(message)
                bot.send_message(message.chat.id, answer)
                ids.remove(message.chat.id)
                commands4.remove('rubtoeur')







        #------------

"""if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://usdeurbot.herokuapp.com") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()"""
bot.polling(none_stop=True)
