# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 02:52:53 2024

@author: Lenovo
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime

"""
you have to go to developers spotify and make a new app from the dashboard. Then copy and paste
the client ID , and Client Secret.
Also, put the redirect_uri

and choose Web API
"""

# Set your Spotify API credentials
client_id = 'Your_Client ID'
client_secret = 'Your_Client Secret'
redirect_uri = 'http://localhost:9090/callback'

# Define the scope for the required access
scope = 'user-top-read'

# Authenticate and create a Spotify object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Function to get the most played song daily
def get_most_played_song():
    # Get the current date
    today = datetime.datetime.today().date()

    # Fetch the top tracks for the current user over the last day
    results = sp.current_user_top_tracks(time_range='short_term', limit=15)
    if results['items']:
        output = ""
        for i in range(min(15, len(results['items']))):
            track = results['items'][i]
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            output += f"#{i+1}: '{track_name}' by {artist_name}\n"
        return f"Your most played songs up today ({today}):\n{output}"
    else:
        return f"No data available for today ({today})."
# Call the function and print the result
print(get_most_played_song())


