from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(url=billboard_url)
soup = BeautifulSoup(response.text, "html.parser")

title_data = soup.select(selector="h3.a-no-trucate")
titles = [data.getText().strip() for data in title_data]

song_uris = []
year = date.split("-")[0]
for song in titles:
    song_data = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = song_data["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

new_playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
print(new_playlist)

sp.playlist_add_items(new_playlist["id"], song_uris)

