import json
import time
import urllib.request
import re
import os
import youtube_dl

from pytube import YouTube

api_key = "AIzaSyAvtSfXka8Qf_i2BlbORNfTWKRPiJbXMJ8"
channel_id = "UCIcgBZ9hEJxHv6r_jDYOMqg"

ydl = youtube_dl.YoutubeDL({'outtmpl': './videos/%(title)s.%(ext)s'})


# Yoinked from StackOverflow, with slight modifications
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

#YouTube('https://youtube.com/watch?v=2lAe1cqCOXo').streams.first().download("./videos")