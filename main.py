# Name: Eshan Oberoi
# Start Date: August 16 2022
# Project: Clone Hero Twitter Bot
# Design: Scrape the main song download repository website for the video game Clone Hero (chorus.fightthe.pw)
# and create a Twitter bot that tracks each new song release

import requests
import tweepy
from dateutil import parser
import datetime

keys = open('twitterkeys.txt', 'r').read().splitlines()
consumer_key = keys[0]
consumer_key_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]
bearer_token = keys[4]
# Twitter ID for @CHSongBot: 1579698267700559872

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_key_secret,
                       access_token=access_token, access_token_secret=access_token_secret)
client.get_me()


# client.create_tweet(text="Hello World!") -- first tweet
# client.follow_user('1666587121') -- follow personal account
# client.follow_user('918556551408947200') -- follow @CloneHero


# retrieves the JSON of the "latest" song section from the site
song_dict = requests.get('https://chorus.fightthe.pw/api/latest').json()

# print(type(song_dict))
name_list = []

last_24_hours = datetime.datetime.now() - datetime.timedelta(days=1)
for song in song_dict['songs']:
    # name_list.append(song['name'])
    # ORIGINAL TWEET SHOULD INCLUDE:
    # NEW CHART: name [length]
    # artist: ###
    # album: ### (year)
    # genre: ###
    # charter: ###

    # REPLY TWEET SHOULD INCLUDE (only include instruments if applicable)
    # Difficulties:
    # Guitar: N/A / difficulties (easy, medium, hard, expert)
    # Bass: N/A / difficulties (easy, medium, hard, expert)
    # Drums: N/A / difficulties (easy, medium, hard, expert)
    # Rhythm Guitar: N/A / difficulties (easy, medium, hard, expert)
    # Keys: N/A / difficulties (easy, medium, hard, expert)

    if parser.isoparse(song['uploadedAt']).timestamp() >= last_24_hours.timestamp():
        m, s = divmod(song['length'], 60)
        guitar_diff_list = []
        guitar_diff_str = ''
        bass_diff_list = []
        bass_diff_str = ''
        drums_diff_list = []
        drums_diff_str = ''
        rhythm_diff_list = []
        rhythm_diff_str = ''
        keys_diff_list = []
        keys_diff_str = ''
        song_length = '{:02d}:{:02d}'.format(m, s)
        for item in song:
            if song[item] is None and item == 'album':
                song[item] = 'Unknown Album'
            elif song[item] is None:
                song[item] = 'N/A'
            for instrument in song['noteCounts']:
                if instrument == 'guitar':
                    guitar_diff_list = list(song['noteCounts'][instrument].keys())
                    guitar_diff_str = "\nGuitar: " + ",".join(guitar_diff_list).upper()
                elif instrument == 'bass':
                    bass_diff_list = list(song['noteCounts'][instrument].keys())
                    bass_diff_str = "\nBass: " + ",".join(bass_diff_list).upper()
                elif instrument == 'drums':
                    drums_diff_list = list(song['noteCounts'][instrument].keys())
                    drums_diff_str = "\nDrums: " + ",".join(drums_diff_list).upper()
                elif instrument == 'rhythm':
                    rhythm_diff_list = list(song['noteCounts'][instrument].keys())
                    rhythm_diff_str = "\nRhythm: " + ",".join(rhythm_diff_list).upper()
                elif instrument == 'keys':
                    keys_diff_list = list(song['noteCounts'][instrument].keys())
                    keys_diff_str = "\nKeys: " + ",".join(keys_diff_list).upper()

        original_tweet = client.create_tweet(text=song['name'] + ' [' + song_length + ']\n' + 'ARTIST: '
              + song['artist'] + '\n\n' + 'ALBUM: ' + song['album'] + ' (' + str(song['year']) + ')\n'
              + 'GENRE: ' + song['genre'] + '\nCHARTER: ' + song['charter'])
        thread_tweet_one = client.create_tweet(text='DIFFICULTIES:' + guitar_diff_str + bass_diff_str
                                                    + drums_diff_str + rhythm_diff_str + keys_diff_str,
                                               in_reply_to_tweet_id=original_tweet.data['id'])


