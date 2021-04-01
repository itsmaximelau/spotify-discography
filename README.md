# spotify-discography

## Description
<b> spotify-discography </b> is a small script to create a Spotify plalylist containing an artist entire discography. It uses spotipy (lightweight Python library for the Spotify Web API) to authenticate user, to find every album an artist has made, to find every song on an album and create an a playlist with every song found.

## Want to use it yourself ?
To use the script, you must create a Spotify app using Spotify for Developers.

<a href= "https://developer.spotify.com/dashboard/applications"> Link to the website </a> 

Once you're logged in with your Spotify account, create an app. App name doesn't matter so you can input whatever you want. Then, click on it an find your Client ID. Also, find the Client Secret (which is hidden under Client ID).

![Client ID and Client Secret example](https://github.com/itsmaximelau/spotify-dicography/blob/main/resources/spotify-dev-image1.png?raw=true)

Then, you have to open credentials.py and paste your Client ID and Client Secret between quotes.

Once this step is complete, go back to your app dashboard and edit settings. You have to set a Redirect URI in there. You have to put the same one that is in the credentials.py file (shoud be http://localhost:8888/callback). 

![Client ID and Client Secret example](https://github.com/itsmaximelau/spotify-dicography/blob/main/resources/spotify-dev-image2.png?raw=true)

Then you're good to go !

- Run spotify_discography.py
- Authenticate youself with your Spotify account credentials.
- Enter the name of an artist
Then, the playlist is created.
