# ch-twitter-bot
A Twitter Bot that automates tweets based on the release of new Clone Hero charts from the Chorus Repository.
https://twitter.com/CHsongbot

OVERVIEW:
Clone Hero is a free popular fan-made clone of the Guitar Hero video game franchise. The clone allows players to download charts (maps of notes to play) and play along to songs on their PC with guitar, drum, and key controllers that they may own. These charts are designed to be freely and widely available, with a few major repositories and spreadsheets where thousands of song charts can be downloaded. Perhaps the biggest (single) source of charts is the Chorus repository (https://chorus.fightthe.pw/), where users, with permission from admins, can upload their custom-made charts for other users to install and add to their Clone Hero songs folder.

PURPOSE:
This project is mainly one of personal convenience. As a regular player of Clone Hero, I enjoy downloading new charts and playing along. However, there is no convenient way to know when charts of songs I may want to play will be released, besides just checking the Recent section of Chorus, or looking up songs I know on a whim in the search bar. The latter method limits my exposure to new charts to just my imagination, versus seeing charts that I am intriuged by but did not think of searching. This is where the Twitter bot comes in. By having an automated system of tweeting out new chart releases and details, I can scroll through my personal Twitter timeline and if I come across tweets from the bot of charts I am interested in, I can then choose to download them off of Chorus. By making this a public bot, however, I am hoping other Clone Hero players can find this a useful (but onifficial) tool.

METHODOLOGY:
I needed to authenticate my project with the Twitter developer account I created, which requires personal keys in a document that is not available in this Git repository, so that others cannot access my account. IF YOU WISH TO DUPLICATE THIS, you will have to undergo your own Twitter developer application and receive your own keys. 

I used the API of the Recent section on the Chorus website (can be seen on the homepage) as a dictionary to draw my data from.

ORIGINAL TWEET INCLUDES:
    NEW CHART: name [length]
    artist: ###
    album: ### (year)
    genre: ###
    rcharter: ###

REPLY TWEET INCLUDES (only include difficulties of each instrument if the instrument and/or its difficulties exists in the chart)
    Difficulties (E = Easy, M = Medium, H = Hard, X = expert):
    Guitar: N/A or E, H, M, X
    Bass: N/A or E, H, M, X
    Drums: N/A or E, H, M, X
    Rhythm Guitar: N/A or E, H, M, X
    Keys: N/A or E, H, M, X
    
UPDATE: As of December 5, 2022, the bot is in its Beta phase. The script runs at 1:06 AM EST daily.
