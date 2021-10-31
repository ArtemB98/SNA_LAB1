import vk_api
import json
import tweepy

from MyStreamListener import MyStreamListener

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
group_id = -43938013


def auth_handler():
    """ При двухфакторной аутентификации вызывается
    эта функция.
    """
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True
    return key, remember_device


def stop_f(items):
    print(items)


def task1():
    login, password = '<ВАШ ЛОГИН>', '<ВАШ ПАРОЛЬ>'
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler  # функция
        # для
        # обработки
        # двухфакторной
        # аутентификации
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)

    tools = vk_api.VkTools(vk_session)
    vk_app = vk_session.get_api()
    print(vk_app.wall.post(message='Hello world!'))


def task2():
    """ Пример получения всех постов со стены """
    login, password = '<ВАШ ЛОГИН>', '<ВАШ ПАРОЛЬ>'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    tools = vk_api.VkTools(vk_session)
    wall = tools.get_all('wall.get', 100,
                         {'owner_id': group_id})
    print('Posts count:', wall['count'])
    f = open(r" wall_asp.txt", 'a')
    f.write(json.dumps(wall))
    f.close()


def task3_part1():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    user = api.get_user('twitter')
    print(user.screen_name, user.followers_count)


def task3_part2():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status('Просто так твит ни о чём!')


if __name__ == '__main__':
    task1()
    task2()
    task3_part1()
    task3_part2()
    MyStreamListener().task3_part3()