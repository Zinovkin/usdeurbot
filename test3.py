import vk
session = vk.Session()
vk_api = vk.API(session)
vk_api.users.get(user_id=190520119)
print(vk_api.users.get(user_id=139946022, fields='online, last_seen'))

import time
print(time.strftime("%D %H:%M", time.localtime(int("1491735287"))))

"--------------"

import vk_api


def main():
    """ Пример получения всех постов со стены """

    login, password = 'testmail100501@yandex.ru', 'sasha13200'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    tools = vk_api.VkTools(vk_session)

    """ VkTools.get_all позволяет получить все объекты со всех страниц.
        Соответственно get_all используется только если метод принимает
        параметры: count и offset.
        Например может использоваться для получения всех постов стены,
        всех диалогов, всех сообщений, etc.
        При использовании get_all сокращается количество запросов к API
        за счет метода execute в 25 раз.
        Например за раз со стены можно получить 100 * 25 = 2500, где
        100 - максимальное количество постов, которое можно получить за один
        запрос (обычно написано на странице с описанием метода)
    """

    wall = tools.get_all('messages.get', 100)


    print('Posts count:', wall['count'])

    if wall['count']:
        print('First post:', wall['items'][0], '\n')

    if wall['count'] > 1:
        print('Last post:', wall['items'][-1])

    x=int(wall['count'])
    messages=''

    for number in range(0, int(wall['count'])):
        print(str(wall['items'][number]))

"""
        f=open('messages.txt','a')
        f.write(wall['items'][number])
        f.close()
"""

if __name__ == '__main__':
    main()
