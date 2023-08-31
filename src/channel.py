import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""
# глобальный атрибут класса api_key, ему присваиваем значение ключа, указав путь нахождения
    api_key: str = os.getenv('API_KEY')
# с помощью специального конструктора build,формируем необходимый для доступа к каналу,интерфейс
 #   youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.dict_channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.dict_channel['items'][0]['snippet']['title']
        self.description = self.dict_channel['items'][0]['snippet']['description']
        self.url = self.dict_channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = self.dict_channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.dict_channel['items'][0]['statistics']['videoCount']
        self.view_count = self.dict_channel['items'][0]['statistics']['viewCount']


    def print_info(self):
        """Выводит в консоль информацию о канале."""
#получаем список с ютюба, записываем в  dict_channel
      #  dict_channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()

#выводим, полученный список, преобразовав из формата json
        print(json.dumps(self.dict_channel, indent=2, ensure_ascii=False))

        # print(dict_channel['items'])   для отладки


    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube


    def to_json(self, name_channel):
        '''Запись данных в файл в формате JSON'''

        data = [self.channel_id, self.title, self.description, self.url, self.subscriber_count, self.video_count,
                self.view_count]
        with open(name_channel, 'w') as f:
            json.dump(data, f)

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        '''Метод срабатывает, когда используется оператор сложения.
	В параметре other хранится то, что справа от знака +'''
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        '''Метод вычитания'''
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        '''метод для операции сравнения «меньше» (self < other)'''
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        '''метод для операции сравнения «меньше или равно» (self <= other)'''
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        '''метод для операции сравнения «равно» (self > other)'''
        return int(self.subscriber_count) == int(other.subscriber_count)


