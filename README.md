# Youtube Channel Archiver
*[originally made to archive Unus Annus' channel]*

## Anchor Points
[Managing config.json](#managing-config.json)

[Getting a channel's ID](#getting-a-channels-id)

[Getting a Youtube V3 Data API Key](#getting-a-youtube-v3-data-api-key)


##  Managing config.json

The config file was made to be as simple as possible.

To add your **YouTube API Key** you simply remove ***"enter youtube v3 data api key"*** and **replace** the **string** with your own **API key**.

![gif of me replacing the api key](https://i.imgur.com/50Mqd3m.gif)

To change the **directory** where the **downloaded videos** go, you simply change **default** to a **system path** to where you want it to do

*ex: **D:/Videos/awesome archive***

![gif of me replacing default with the example above](https://i.imgur.com/9rBcsmr.gif)

*Note: you don't have to touch **video_format** as that is used by the **youtube-dl** package, read their documentation on it for help there.*



## Getting a Channel's ID

This is probably the simplist step, to get a channel's id, you simply **go to the channel on YouTube** and copy the **random string** that comes after *youtube.com/channel/*

![picture of me selecting the "random string"](https://i.imgur.com/hESZ8RW.png)

## Getting a Youtube V3 Data API Key
To get a YouTube Data key is pretty simple.
Simply click [here](https://console.developers.google.com/apis/library/youtube.googleapis.com?q=YouTube&id=125bab65-cfb6-4f25-9826-4dcc309bc508&project=tester-api-key) to go to the API page, and press **Enable**

Once you press **Enable** it should ask you what project you'd like to use, just use any of them *[should be one called **My First Project**]*

![image of me hovering over "my first project"](https://i.imgur.com/B8PONSZ.png)

Once you get redirected, at the top of the page it should ask you to **Create Credentials**, you'll want to **click** on the button

![image of the create credentials banner](https://i.imgur.com/ZTHkMt0.png)

When **creating** the **API credentials** it'll ask for what API you are using, click **Choose** and pick **YouTube Data API v3**

![image of me picking the right api](https://i.imgur.com/BimK7hN.png)

Once you pick this, another option should pop up asking, "**Where will you be calling the API from?**"; Here, you'll pick **Web server**

![image of picking the right api to call from](https://i.imgur.com/SeMu0mY.png)

For "**What data will you be accessing?**"; You'll simply want to pick **Public data**

![image dotting in public data](https://i.imgur.com/G40FY9k.png)

Once you do this, you can go ahead and click the **blue** "**What credentials do I need?**" button; once you click it, you'll finally get your **API key**.