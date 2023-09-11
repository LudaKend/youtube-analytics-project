# класс PlayList, который инициализируется id плейлиста и имеет следующие публичные атрибуты:
# название плейлиста: title
# ссылку на плейлист: url
# Реализуйте следующие методы:
# total_duration возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
# (обращение как к свойству, использовать @property)
# show_best_video() возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)

from src.channel import Channel
import datetime
import isodate

class PlayList(Channel):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        #print(self.get_service())
        self.dict_playlist = self.get_service().playlists().list(id=self.playlist_id, part='contentDetails, snippet', maxResults=50).execute()
        # self.dict_channel = self.get_service().channels().list(id=self.video_id, part='snippet,statistics').execute()
        #print(self.dict_playlist)
        self.title = self.dict_playlist['items'][0]['snippet']['title']
        #print(self.title)
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        #print(self.url)

        self.playlist_videos = self.get_service().playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50).execute()
        #print(playlist_videos)
        self.list_id_playlist = []
        for playlist in self.playlist_videos['items']:
            # print(playlist)
            # print()
            self.list_id_playlist.append(playlist['contentDetails']['videoId'])
        #print(self.list_id_playlist)


    @property
    def total_duration(self):
        '''возвращает объект класса datetime.timedelta с суммарной длительность плейлиста'''
        time_playlist = datetime.timedelta()
        #print(f'time_playlist {time_playlist}')
        for item in self.list_id_playlist:
            self.video_response = self.get_service().videos().list(part='statistics,contentDetails,topicDetails',
                                               id=item).execute()
            #print(f'self.video_response   {self.video_response}')
            self.duration = self.video_response['items'][0]['contentDetails']['duration']
            #print(f'self.duration  {self.duration}')


            # метод parse_duration() преобразует строку длительности ISO 8601 в объект timedelta или Duration
            str_duration = isodate.parse_duration(self.duration)
            #print(f'str_duration {str_duration}')
            # print(type(str_duration))
            time_playlist += str_duration
            #print(f'time_playlist {time_playlist}')

        return time_playlist



    def show_best_video(self):
        '''возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)'''
        self.max_like_count = 0
        for item in self.list_id_playlist:
            self.video_response = self.get_service().videos().list(part='statistics,contentDetails,topicDetails',
                                                                   id=item).execute()
            self.like_count = int(self.video_response['items'][0]['statistics']['likeCount'])
            #print(f'self.like_count  {self.like_count}')
            if self.like_count > self.max_like_count:
                self.max_like_count = self.like_count
                self.best_id_playlist = item
        return f'https://youtu.be/{self.best_id_playlist}'
