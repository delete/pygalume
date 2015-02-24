import requests as r
from settings import API_URL
from .utils import formating_string_name


class API():

	def getLyrics(self, artist, music):
		artist = formating_string_name(artist)
		music = formating_string_name(music)

		response = r.get(API_URL+'art={0}&mus={1}'.format(artist, music))
		
		if response.json()['type'] == 'song_notfound':
			return 'Song not found!'
			#raise MusicNotFound

		elif response.json()['type'] == 'notfound':
			return 'Artist not found!'
			#raise ArtistNotFound

		else:
			return response.json()['mus'][0]['text']

