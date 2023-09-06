from src.channel import Channel

#класс `Video`c инициализацией реальными данными следующих атрибутов экземпляров класса `Video`:
  # - id видео: video_id
  # - название видео: name
  # - ссылка на видео: link
  # - количество просмотров: view_count
  # - количество лайков: like_count

class Video(Channel):

    def __init__(self, video_id):
        self.video_id = video_id
        self.dict_channel = self.get_service().videos().list(part='snippet,'
                                                                    'statistics,'
                                                                    'contentDetails,'
                                                                    'topicDetails',
                                                               id=video_id).execute()

        self.title = self.dict_channel['items'][0]['snippet']['title']
        self.url = self.dict_channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = self.dict_channel['items'][0]['statistics']['viewCount']
        self.like_count = self.dict_channel['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.video_id}, {self.title}, {self.url}, {self.view_count}, {self.like_count}'

# второй класс для видео `PLVideo`, в котором инициализируется  'id видео' и 'id плейлиста'
# Видео может находиться в множестве плейлистов, поэтому непосредственно из видео через API информацию о плейлисте не получить.
# Реализуйте инициализацию реальными данными следующих атрибутов экземпляра класса `PLVideo`:
#   - id видео: video_id
#   - название видео: name
#   - ссылка на видео: link
#   - количество просмотров: view_count
#   - количество лайков: like_count
#   - id плейлиста: playlist_id

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f'{self.video_id}, {self.playlist_id}'
