from __future__ import unicode_literals
from dotenv import load_dotenv
import os

load_dotenv()

TELE_TOKEN = os.getenv("TELE_TOKEN")
YT_BUILD_TOKEN = os.getenv("YT_BUILD_TOKEN")

def bot_msg_hafidz(text):
    import requests
    url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage"
    payload = {
        "text": '[LOCAL]' + text,
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": "1908911926"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
def get_time_ago_power():
    time_ago_key = []
    
    time_ago_key.append('1 minute ago')
    for i in range(2, 24):
        time_ago_key.append(f'{i} minutes ago')
    time_ago_key.append('1 hour ago')
    for i in range(2, 24):
        time_ago_key.append(f'{i} hours ago')
    time_ago_key.append('1 day ago')
    for i in range(2, 24):
        time_ago_key.append(f'{i} days ago')
    time_ago_key.append('1 week ago')
    for i in range(2, 4):
        time_ago_key.append(f'{i} weeks ago')
    time_ago_key.append('1 month ago')
    for i in range(2, 13):
        time_ago_key.append(f'{i} months ago')
    time_ago_key.append('1 year ago')
    
    for i in range(2, 10):
        time_ago_key.append(f'{i} years ago')
    
    time_ago_value = range(len(time_ago_key))
    power_out = {}
    for key,val in zip(time_ago_key, time_ago_value):
        power_out[key] = val
        
    power_out['Streamed 1 minute ago'] = 0
    
    for i,j in zip(range(2,24),range(1,23)):
        power_out[f'Streamed {i} minutes ago'] = j
        
    power_out['Streamed 1 hour ago'] = 23
    
    for i,j in zip(range(2,24),range(24,23+23)):
        power_out[f'Streamed {i} hours ago'] = j
        
    power_out['Streamed 1 day ago'] = 46

    for i,j in zip(range(2,24),range(47,23+23+34)):
        power_out[f'Streamed {i} days ago'] = j
        
    return power_out

get_time_power = get_time_ago_power()


def tanggal_converter(arg_tanggal):
    ##################
    # Input: Aug 10, 2022           Output: 2022-08-10
    ##################
    arg_tanggal = arg_tanggal.replace(',','')
    bulan_dict = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
    }
    get_bulan = bulan_dict[arg_tanggal.split()[0]]
    if int(arg_tanggal.split()[1]) < 10:
        tanggal_out = f'{arg_tanggal.split()[-1]}-{get_bulan}-0{arg_tanggal.split()[1]}'
    else:
        tanggal_out = f'{arg_tanggal.split()[-1]}-{get_bulan}-{arg_tanggal.split()[1]}'
    return tanggal_out

    
def crawling_harian():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import pandas as pd
    import requests
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    import pandas as pd
    ser = Service("C:\Program Files (x86)\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    
    bot_msg_hafidz('Youtube Crawling Started!')
    from datetime import datetime

    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y").replace('/','-')
    
    print('Starting to get all link...=================================================================\n')
    bot_msg_hafidz('Starting to get all link...')
    links = []
    channel_name = []
    days_list = ['21 hours ago','22 hours ago','23 hours ago','1 day ago']
    from bs4 import BeautifulSoup as bs
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time
    from selenium.webdriver.support.ui import WebDriverWait
    from tqdm import tqdm
    
def clean_view(texts):
    result = re.sub(',','', texts)
    result = re.sub(' views','', result)

    try:
        return int(result)
    except:
        return 0
    
def clean_like(texts):
    if 'K' in texts:
        if '.' in texts:
            texts = texts.replace('.', '').replace('K', '')
            try:
                texts = texts + '00'
                return int(texts)
            except:
                return 0
        else:
            try:
                texts = texts.replace('K', '')
                return int(texts + '000')
            except:
                return 0
    else:
        try:
            return int(texts)
        except:
            return 0

#     channels = """CNNindonesiaOfficial
# kompastv
# tribunnews
# tvOneNews
# MetrotvnewsOfficial
# BeritaSatuChannel
# VIVAcoid
# CNBCIndonesia_ID
# OfficialiNews
# HarianKompasCetak
# mykompascom
# UCQA6NejSxQguRkD3L8eXHzA
# OfficialNETNews
# TribunMedanTV
# detikcom
# TribunJogjaOfficial
# PikiranRakyatDigital
# suaradotcom"""

#     channels_decode = """CNNindonesiaOfficial
# kompastv
# tribunnews
# tvOneNews
# MetrotvnewsOfficial
# BeritaSatuChannel
# VIVAcoid
# CNBCIndonesia_ID
# OfficialiNews
# HarianKompasCetak
# kompas.com
# iNews_id
# OfficialNETNews
# TribunMedanTV
# detikcom
# TribunJogjaOfficial
# PikiranRakyatDigital
# suaradotcom"""
    
    channels = """CNNindonesiaOfficial
kompastv"""

    channels_decode = """CNNindonesiaOfficial
kompastv"""


    channels = channels.split('\n')
    channels_decode = channels_decode.split('\n')

    until_when = '1 day ago'

    for channel,decode in zip(tqdm(channels), channels_decode):
        start_time = time.time()
        if channel in ['UCQA6NejSxQguRkD3L8eXHzA','UCH_ElasO_yPy0WI3rAOUkQQ','UCpFqnctVbdqj1UketjDVz4Q']:
            driver.get(f'https://www.youtube.com/channel/{channel}/videos')
        elif channel in ['suaradotcom']:
            driver.get(f'https://www.youtube.com/user/{channel}/videos')
        else:
            driver.get(f'https://www.youtube.com/c/{channel}/videos')
        sc = 0
        while True:
            time.sleep(2)
            sc += 1080
            driver.execute_script("window.scrollTo(0, {})".format(sc))
            date_check = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#metadata-line span+span')))[-1].text
            time.sleep(1)
            print(date_check)

            if get_time_power.get(date_check,0) >= get_time_power.get(until_when,0):
                time_passed = round(time.time() - start_time)
                print(f"{time_passed} seconds passed after crawling title in channel {decode}")
                break

        soup = bs(driver.page_source, 'lxml')
        links_html = soup.select('#video-title')
        overlapping_time_check = soup.select('#metadata-line span+span')

        for i,j in zip(links_html,overlapping_time_check):
            if get_time_power.get(j.text, 0) <= get_time_power.get(until_when,0):  
                links.append(i.get('href'))
                channel_name.append(decode)
            
            
    
    print(f'\nStarting to get all data, total: {len(links)}...=================================================================\n')        
    bot_msg_hafidz(f'Starting to get all data, total: {len(links)}')
    
    all_data = []
    
    
    from youtube_transcript_api import YouTubeTranscriptApi # API for caption
    from googleapiclient.discovery import build # API for comment

    import youtube_dl # API for downloading mp3
    import re

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from pytube import YouTube # API for description

    import urllib.request
    import json
    import urllib

    driver_wait = 5


    youtube = build('youtube','v3', developerKey=YT_BUILD_TOKEN)

    for link, ch in zip(tqdm(links),channel_name):
        try:
            driver.get(f"https://www.youtube.com/{link}")
        except:
            print('driver problem')
        time.sleep(2)

        each_data = {}
        each_data.update({"video_link": f"https://www.youtube.com{link}"})
        try:
            params = {"format": "json", "url": link}
            url = "https://www.youtube.com/oembed"
            query_string = urllib.parse.urlencode(params)
            url = url + "?" + query_string
            with urllib.request.urlopen(url) as response:
                response_text = response.read()
                data = json.loads(response_text.decode())
                video_title = (data['title'])
            each_data.update({"video_title": video_title})
        except Exception as e:
            print(e)
            each_data.update({"video_title": '-'})
        try: 
            video_date = WebDriverWait(driver, driver_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#info-strings'))).text
            each_data.update({"video_date": video_date})
            print(video_date)
        except Exception as e:
            print(e)
            each_data.update({"video_date": '-'})
            
        # Cleaned date
        splitted_date_time = date_time.split('-')
        date_time_normalized = f'{splitted_date_time[-1]}-{splitted_date_time[0]}-{splitted_date_time[1]}'

        try:
            re_get_tanggal = re.findall('\w+\s\d{1,2}\,\s\d{4}',video_date)[0]
        except:
            re_get_tanggal = video_date
        try:
            cleaned_date = tanggal_converter(re_get_tanggal)
        except:
            cleaned_date = date_time_normalized

        each_data.update({"tanggal": cleaned_date})
        
        try:
            view_count = WebDriverWait(driver, driver_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.view-count'))).text
            each_data.update({"view_count": view_count})
            print(view_count)
        except Exception as e:
            print(e)
            each_data.update({"view_count": '-'})
        try:
            like_count = WebDriverWait(driver, driver_wait).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.yt-simple-endpoint>yt-formatted-string'))).text
            each_data.update({"like_count": like_count})
            print(like_count)
        except Exception as e:
            print(e)
            each_data.update({"like_count": '-'})
        try:
            video_desc = YouTube(link).description
            #video_desc = WebDriverWait(driver, driver_wait).until(EC.presence_of_element_located((By.XPATH,'/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[9]/div[2]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div/yt-formatted-string'))).text
            each_data.update({"video_desc": video_desc})
        except Exception as e:
            print(e)
            each_data.update({"video_desc": '-'})



        try:
            transcriptList = YouTubeTranscriptApi.list_transcripts(re.findall(r'(?<=watch\?v\=).+', link)[0])
            dataCaption = []
            for transcript in transcriptList:
                for text in transcript.translate('id').fetch():
                    dataCaption.append(text.get('text'))
            data_caption_str = ''
            for i in dataCaption:
                data_caption_str += i + " "
            each_data.update({"caption": data_caption_str})
        except Exception as e:
            print(e)
            each_data.update({"caption": '-'})

        try:
            def get_video_comments(**kwargs):
                comments = []
                results = youtube.commentThreads().list(**kwargs).execute()
                comment_dict = {
                    "authorDisplayName": '',
                    "authorChannelUrl": '',
                    "authorProfileImageUrl": '',
                    "textOriginal": '',
                    "likeCount": '',
                    "replies" : ''
                }
                while results:
                    for item in results['items']:
                        ds = item['snippet']['topLevelComment']['snippet']
                        for com_key in comment_dict.keys():
                            if com_key != 'replies':
                                comment_dict[com_key] = ds[com_key]
                            else:
                                try:
                                    comment_dict['replies'] = item['replies']['comments']
                                except:
                                    comment_dict['replies'] = []
                        comments.append(comment_dict.copy())
                    # Check if another page exists
                    if 'nextPageToken' in results:
                        kwargs['pageToken'] = results['nextPageToken']
                        results = youtube.commentThreads().list(**kwargs).execute()
                    else:
                        break
                return comments
            
            get_all_comment = get_video_comments(part='snippet,replies',videoId=re.findall(r'(?<=watch\?v\=).+', link)[0])
            each_data.update({"video_comment": get_all_comment})      
            
        except Exception as e:
            print(e)
            dict_comment_kosong = {'authorDisplayName': '',
            'authorChannelUrl': '',
            'authorProfileImageUrl': '',
            'textOriginal': '',
            'likeCount': 0,
            'replies': []}
            each_data.update({"video_comment": [dict_comment_kosong]})

        each_data.update({"channel_name": ch})

        all_data.append(each_data)
        
    all_data_table = pd.DataFrame(all_data)
    no_caption_df = all_data_table[all_data_table['caption'] == '-']
    
    bot_msg_hafidz(f'There is {len(all_data_table) - len(no_caption_df)}/{len(all_data_table)} data!')



    no_stt = f'data_yt_harian_{date_time}_raw.json'

    with open(no_stt,'w') as f:
        all_data = json.dump(all_data_table.to_dict('records'),f)
    no_caption_df = all_data_table[all_data_table['caption'] == '-']
    
    print('\nStarting to download the remaining mp3 caption...============================================\n')
    bot_msg_hafidz('Starting to download the remaining mp3 caption...')
    
    import youtube_dl

    for each_link in tqdm(no_caption_df['video_link'].to_list()):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'data01/' + each_link.split('/www.youtube.com/')[1] + '.mp3'
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                dictMeta = ydl.extract_info(each_link,download=False)
                if dictMeta['duration'] < 1800:
                    ydl.download([each_link])
        except Exception as e:
            pass
    
    print('Starting speech to text...=================================================================')
    bot_msg_hafidz('Starting speech to text...')

    from os import listdir
    from os.path import isfile, join

    mypath = 'C:/Users/hafid/main/projects/data_science/youtube_scraping/data01'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    onlyfiles = ['data01/'+i for i in onlyfiles]
    onlyfiles = [i for i in onlyfiles if '.mp3' in i]
    import os
    import speech_to_text
    stt = []
    for each_file in tqdm(onlyfiles):
        try:
            stt_out = speech_to_text.parse_transcription(each_file)
            print(stt_out)
            stt.append(stt_out)
        except Exception as e:
            print(e)
            
    df = all_data_table
    import re
    for i in stt:
        if i['transcription']:
            locate_link = df['video_link'] == 'https://www.youtube.com/' + i['file'].split('.mp3')[0].replace('#','?')
            df.loc[locate_link,['caption']] = i['transcription']
    df.drop(df[df['caption'] == '-' ].index, inplace=True)
    
    bot_msg_hafidz(f'There is {len(df)}/{len(all_data_table)} data after speech to text!')
    df['like'] = df['like_count'].apply(clean_like)
    df['view'] = df['view_count'].apply(clean_like)
    save = f'data_yt_harian_{date_time}.json'

    with open(save,'w') as f:
        json.dump(df.to_dict('records'),f)
        
    bot_msg_hafidz(save)
    
    import os
    dir = 'C:/Users/hafid/main/projects/data_science/youtube_scraping/data01'
    for f in os.listdir(dir):
        try:
            os.remove(os.path.join(dir, f))
        except:
            pass
    print('Done=================================================================')

import schedule
import time


get_input = input('Want to start now?(y/n): ')
schedule_time = "14:42"
if get_input == 'y':
    crawling_harian()
else:
    print(f'Will start at {schedule_time}')
    schedule.every().day.at(schedule_time).do(crawling_harian)
    print('======Local youtube scraping Started!======')

while True:
    schedule.run_pending()
    time.sleep(1)