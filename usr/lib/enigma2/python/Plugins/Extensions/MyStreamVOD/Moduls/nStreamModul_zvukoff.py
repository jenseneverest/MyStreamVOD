# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/Moduls/nStreamModul_zvukoff.py
from xml.etree.cElementTree import fromstring, ElementTree
import urllib2
import urllib as ul
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
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_zvukoff:

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
        debug(url, 'youtube')
        parts = url.split('@')
        video_list_temp = []
        url = parts[0]
        page = parts[1]
        name = parts[2].encode('utf-8')
        self.search_text = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
        self.search_on = 'search'
        chan_counter = 0
        if len(parts) == 3:
            self.playlistname = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb8\xd0\xba \xd0\xbc\xd1\x83\xd0\xb7\xd1\x8b\xd0\xba\xd0\xb8'
            new = (1, '\xd0\x9d\xd0\xb0\xd0\xb6\xd0\xbc\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xbd\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5 \xd0\xba\xd0\xbd\xd0\xbe\xd0\xbf\xd0\xba\xd1\x83 "Stop"', None, None, None, '', None, '', '', None, None)
            video_list_temp.append(new)
        if len(parts) == 4:
            param = parts[3].encode('utf-8')
            param = param.replace(' ', '%20')
            url = 'zvukoff.ru/mp3/search?keywords=' + param
            page = mod_request(url)
            results = re.findall('<a duration="(.*?)" id_song=".*?" href="(.*?)" title_song="(.*?)"  class="song-play btn4 play"><span></span></a>', page)
            self.playlistname = '\xd0\x9f\xd0\xbe \xd0\xb7\xd0\xb0\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd1\x83 %s \xd0\xbd\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe %i \xd1\x80\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82\xd0\xbe\xd0\xb2' % (parts[3], len(results))
            for text in results:
                title = text[2].upper()
                descr = self.playlistname + '\n' + '\xd0\x94\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xb2 \xd1\x81\xd0\xb5\xd0\xba\xd1\x83\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x85 - ' + text[0] + '\n' + '<Created by SashaGamliy>'
                url = text[1]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 descr,
                 'http://cdn2.planetminecraft.com/files/resource_media/screenshot/1241/music-note-t10469_3819011.jpg',
                 url,
                 None,
                 None,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'http://MyStreamVOD.ucoz.ru/vod/start.xml'
        self.prev_page_text = '\xd0\x9f\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0\xd0\xbb'
        self.video_list = video_list_temp
        return