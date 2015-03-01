# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/Moduls/nStreamModul_youtubesearch.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2
import urllib as ul
import sys
sys.path.append('/usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD')
import os, re
from datetime import datetime
from time import time

def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    url = 'http://' + url
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 MyStreamVOD 0.1',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_youtubesearch:

    def __init__(self):
        self.video_list = []
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = ''
        self.active_site_url = ''
        self.playlistname = ''
        self.playlist_cat_name = ''
        self.kino_title = ''
        self.category_back_url = ''
        self.error = ''

    def get_list(self, url):
        global nexturl
        global prevurl
        global prevad
        prevad = ''
        nexturl = ''
        prevurl = ''
        debug(url, 'youtube')
        parts = url.split('@')
        video_list_temp = []
        url = parts[0]
        page = parts[3]
        name = parts[4].encode('utf-8')
        self.search_text = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
        self.search_on = 'search'
        chan_counter = 0
        if len(parts) == 6:
            self.playlistname = 'youtube.com'
            new = (1, '\xd0\x9d\xd0\xb0\xd0\xb6\xd0\xbc\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xba\xd0\xbd\xd0\xbe\xd0\xbf\xd0\xba\xd1\x83 "Stop"', None, None, None, '', None, '', '', None, None)
            video_list_temp.append(new)
        if len(parts) == 7:
            next = parts[1]
            remainpages = parts[2]
            next = int(next)
            remainpages = int(remainpages)
            param = parts[6].encode('utf-8')
            param = param.replace(' ', '%20')
            url = 'gdata.youtube.com/feeds/api/videos?max-results=50&start-index=' + str(next) + '&q=' + param + '&orderby=viewCount'
            page = mod_request(url)
            results = re.findall("<media:player url='(.*?)&amp;feature=youtube_gdata_player'/><.*?media:thumbnail url='(.*?)' height='360' width='480'.*?\\/><media:thumbnail url.*?\\/><media:thumbnail url=.*?\\/><media:thumbnail url=.*?\\/><media:title type='plain'>(.*?)<\\/media:title><yt:duration seconds='(.*?)'/></media:group><gd:rating average='.*?' max='.*?' min='.*?' numRaters='.*?' rel='.*?'/><yt:statistics favoriteCount='.*?' viewCount='(.*?)'/>", page)
            if remainpages == 0:
                totalresults = re.findall('<openSearch:totalResults>(.*?)<', page)
                totalresult = int(totalresults[0])
                totalpages = int(totalresults[0]) / 50 + 1
                remainpages = totalpages - 1
            else:
                totalresult = int(parts[5])
                next2 = next - 50
                remainpages2 = 0
                prevurl = 'nStreamModul@youtubesearch@' + str(next2) + '@' + str(remainpages2) + '@start@youtube@' + str(totalresult) + '@' + param
                prevad = '\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd1\x8b\xd0\xb4\xd1\x83\xd1\x89\xd0\xb0\xd1\x8f'
            if next == 51:
                prevurl = 'nStreamModul@youtubesearch@1@0@start@0@youtube@' + param
                prevad = '\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd1\x8b\xd0\xb4\xd1\x83\xd1\x89\xd0\xb0\xd1\x8f'
            next1 = next + 50
            nexturl = 'nStreamModul@youtubesearch@' + str(next1) + '@' + str(remainpages) + '@start@youtube@' + str(totalresult) + '@' + param
            self.playlistname = str(totalresult) + ' \xd0\xbd\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe'
            for text in results:
                img = text[1]
                title = text[2]
                descr = '\xd0\x94\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x81\xd0\xb5\xd0\xba\xd1\x83\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x85 - ' + text[3] + '\n' + '\xd0\x9f\xd1\x80\xd0\xbe\xd1\x81\xd0\xbc\xd0\xbe\xd1\x82\xd1\x80\xd0\xbe\xd0\xb2 - ' + text[4] + '\n' + 'Created by Faltlines' + '\n' + '<Mod by SashaGamliy>'
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 descr,
                 img,
                 url,
                 None,
                 None,
                 img,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = prevurl
        self.prev_page_text = prevad
        self.next_page_url = nexturl
        self.next_page_text = '\xd0\xa1\xd0\xbb\xd0\xb5\xd0\xb4\xd1\x83\xd1\x8e\xd1\x89\xd0\xb0\xd1\x8f'
        self.video_list = video_list_temp
        return