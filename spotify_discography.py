import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from credentials import CLIENT_ID,CLIENT_SECRET,REDIRECT_URI

### REMEMBER TO CHANGE VARIABLES IN CREDENTIALS.PY, SEE GITHUB FOR DETAILS ###

# This is the scope for Spotfy Auth, change for the following values if you want the generated playlist to be public
#scope = "playlist-modify-public"
#public_playlist = True

scope = "playlist-modify-private"
public_playlist = False

# Spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=scope))

# Current user id
spotify_user_id = sp.me()['id']

# Creates a playlist for authentified user and returns playlist ID, 
def create_playlist(name):
    playlist = sp.user_playlist_create(spotify_user_id, name=name, public=public_playlist)
    playlist_id = playlist["id"]
    return playlist_id

# Adds a song list to a playlist
def add_to_playlist(song_id,playlist_id):
    sp.user_playlist_add_tracks(spotify_user_id,playlist_id,song_id)

# Return a list of albums ID for a selected artist
def search_artist_albums(artist):
    albums = []
    albums_id = []
    album = sp.artist_albums(search_artist(artist)["id"])
    albums.extend(album['items'])
    while album['next']:
        album = sp.next(album)
        albums.extend(album['items'])
    unique = set()
    
    for album in albums:
        if album["album_group"] in ("single", "album"):
            name = album['name'].lower()
            if name not in unique:
                unique.add(name)
                albums_id.append(album["id"])
    return albums_id

# Return a list of songs ID for a selected album
def search_album_songs(album_id):
    songs = []
    song = sp.album_tracks(album_id)
    songs.extend(song['items'])
    while song['next']:
        song = sp.next(song)
        songs.extend(song['items'])
    return songs

# Return an artist ID using Spotify search function
def search_artist(artist):
    artist_search = sp.search(q='artist:' + artist, type='artist')
    return artist_search["artists"]["items"][0]

# Main script - creates a playlist for selected artist
def create_artist_discography(artist):
    playlist_id = create_playlist(artist + " - Discography")
    albums = search_artist_albums(artist)
    print("Found every albums from the artist (" + str(len(albums)) + ").")
    
    # Search for albums
    unique_song_id = []
    for album in albums:
        songs = search_album_songs(album)
        for song in songs:
            song_id = song["id"]
            if song_id not in unique_song_id:
                unique_song_id.append(song_id)
    print("Found every songs from the artist (" + str(len(unique_song_id)) + ").")
    time.sleep(5)
    
    # Split requests in 100 songs per request
    amount_of_songs = len(unique_song_id)
    amount_of_last_request = amount_of_songs % 100
    amount_of_full_requests = int((amount_of_songs - amount_of_last_request)/100)
    
    #100 song requests
    for x in range(amount_of_full_requests):
        song_list = unique_song_id[(x*100):(x*100 + 100)]
        add_to_playlist(song_list,playlist_id)
        print("Adding " + str(len(song_list)) + " songs to the playlist.")
        time.sleep(5)
    
    #Leftover request
    if amount_of_last_request != 0:
        song_list = unique_song_id[-amount_of_last_request:]
        add_to_playlist(song_list,playlist_id)
        print("Adding " + str(len(song_list)) + " songs to the playlist.")
    print("Playlist for " + artist + " is done.")

def main():
    create_artist_discography(input("Enter an artist : "))

main()