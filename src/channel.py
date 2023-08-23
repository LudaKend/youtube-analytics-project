import os
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""
# глобальный атрибут класса api_key, ему присваиваем значение ключа, указав путь нахождения
    api_key: str = os.getenv('API_KEY')
# с помощью специального конструктора build,формируем необходимый для доступа к каналу,интерфейс
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
#получаем список с ютюба, записываем в  dict_channel
        dict_channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
#выводим, полученный список, преобразовав из формата json
        print(json.dumps(dict_channel, indent=2, ensure_ascii=False))
