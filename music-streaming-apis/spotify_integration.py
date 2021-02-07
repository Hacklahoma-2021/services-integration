import spotipy

username = input("Enter Spotify username here: ")
client_id=input("Enter client id here: ")
client_secret=input("Enter client secret here: ")

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri='https://open.spotify.com',
    username=username,
    scope="user-read-playback-state"
    )
)

playlists = sp.user_playlists(username)

print("\tYour playlists")

print('\n')
for idx, playlist in enumerate(playlists['items'], start=1):
    print(f"{idx} - {playlist['name']}")
print('\n')

playlist_choice = int(input("Enter your playlist choice: "))

chosen_playlist = playlists['items'][playlist_choice-1]

chosen_playlist_songs = sp.playlist_items(
    chosen_playlist['uri'],
     offset=0,
     fields='items.track.id,total',
     additional_types=['track'])

print('\n')
for idx, track in enumerate(chosen_playlist_songs['items'], start=1):
    print(f"{idx} - {sp.track(track['track']['id'])['name']}")
print('\n')

track_choice = int(input("Enter your track choice: "))

chosen_track = sp.track(chosen_playlist_songs['items'][track_choice-1]['track']['id'])

devices = sp.devices()

print('\n')
for idx, device in enumerate(devices['devices'], start=1):
    print(f"{idx} - {device['name']}")
print('\n')

device_choice = int(input("Enter your device choice: "))

chosen_device = devices['devices'][device_choice-1]

sp.start_playback(device_id=chosen_device['id'], context_uri=chosen_track['uri'])
