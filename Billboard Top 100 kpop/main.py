from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

Client_ID = os.environ.get('Client_ID')     #using export
Client_Secret = os.environ.get('Client_Secret')

year = input('Enter year to search[YYYY-MM-DD]: ')
response = requests.get(url=f'https://www.billboard.com/charts/billboard-korea-100/{year}')


soup = BeautifulSoup(response.text, 'html.parser')
#billboard top kpop songs not for free users so i get only 1 song which is hown on top🥲
#cls = """c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"""
cls = 'c-title a-font-primary-bold-l a-font-primary-bold-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-r-150'
song_names_spans = soup.find_all(class_=cls)
song_names = [song.getText() for song in song_names_spans]
formate_song_names = [song.replace('\n','')   for song in song_names]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
#Searching Spotify for songs by title
song_uris = []
year1 = year.split("-")[0]
for song in formate_song_names:
    result = sp.search(q=f"track:{song} year:{year1}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year}top kpop", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)






