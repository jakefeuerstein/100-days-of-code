import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

URL_START = "https://www.billboard.com/charts/hot-100/"

SP_ID = ""
SP_SECRET = ""

date = ""
# date = input("Which date would you like your Billboard chart to come from? Enter YYYY-MM-DD format.")
url = f"{URL_START}{date}/"

# -----------------------REQUEST------------------------

response = requests.get(url=url)
response.raise_for_status()
data = response.text

# -----------------------SOUP------------------------

soup = BeautifulSoup(data, "html.parser")
songs_raw = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
songs = [song.getText().strip() for song in songs_raw]
songs = songs[0:10]

# print(songs)


# -----------------------SPOTIPY------------------------

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com/"
    )
)

user_id = sp.current_user()['id']
# playlist = sp.user_playlist_create(user_id, "Billboard Top 100", public=False, collaborative=False, description='')


sp_songs = [sp.search(q=f"track:{song} year:{1992}", type='track', limit=1)['tracks']['items'][0]['id'] for song in songs]

PLAYLIST_ID = "4l49LDqbXnlZYDZL1eYBdi"
sp.playlist_add_items(PLAYLIST_ID, sp_songs, position=None)

# pprint.pprint(sp_songs)

