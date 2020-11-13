
print("\nYoutube Channel Archiver\nCreated by Akkoza\n\nhttps://github.com/AkkozaDevelops/Youtube-Channel-Archiver\n\nHave an issue?\nYou can\n\nCreate an issue on the GitHub Repository\nOR\nAdd me on Discord [Akkoza#8767]")
# Don't have to keep this, but I'd prefer if you did <3

import time

try:
    import json
    import urllib.request
    import re
    import os
    import youtube_dl

    from pytube import YouTube
except Exception as error:
    print("Error loading dependancies\n\n" + str(error))

    while True:
        time.sleep(1)

me = os.path.dirname(os.path.abspath(__file__))  
config = None


# Load config.json

try:
    config = json.load(open(me + "/config.json"))
except Exception as error:
    print("config.json failed to load\n\n" + str(error))

    while True:
        time.sleep(1)


api_key = config["youtube_data_api_key"]
channel_id = str(input("Please input the *channel id* here > "))

ydl = None

try:
    if config["directory"] == "default":
        ydl = youtube_dl.YoutubeDL({'outtmpl': me + '/videos/' + config["video_format"]})
    else:
        ydl = youtube_dl.YoutubeDL({'outtmpl': config["directory"] + config["video_format"]})
except Exception as error:
    print("There was an error loading config directory\n\n" + str(error))

    while True:
        time.sleep(1)


# Yoinked from StackOverflow
# https://stackoverflow.com/a/44871104

def get_all_video_in_channel(channel_id):

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
                print("Grabbed video [" + str(len(video_links)) + "]")

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


# Now starts the downloading code
# yaaay!

videos = get_all_video_in_channel(channel_id)

for video in videos:
    print("downloading " + video)

    try:
        with ydl:
            result = ydl.extract_info(
                video,
                download = True
            )
    except Exception as err:
        print("failed to download " + video + "\nError was\n" + str(err) + "\n\n\n")
        
    time.sleep(1)