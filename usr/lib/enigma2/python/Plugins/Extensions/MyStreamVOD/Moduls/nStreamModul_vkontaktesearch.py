# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/Moduls/nStreamModul_vkontaktesearch.py
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
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_vkontaktesearch:

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
        debug(url, 'MODUL URL: ')
        parts = url.split('@')
        next = 0
        video_list_temp = []
        url = parts[0]
        page = parts[1]
        name = parts[2].encode('utf-8')
        self.search_text = '\xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba'
        self.search_on = 'search'
        chan_counter = 0
        if len(parts) == 3:
            self.playlistname = 'VK \xd0\x9f\xd0\xbe\xd0\xb8\xd1\x81\xd0\xba.Mod by SG'
            new = (1, '\xd0\x9d\xd0\xb0\xd0\xb6\xd0\xbc\xd0\xb8\xd1\x82\xd0\xb5 \xd0\xba\xd0\xbd\xd0\xbe\xd0\xbf\xd0\xba\xd1\x83 "Stop"', None, None, None, '', None, '', '', None, None)
            video_list_temp.append(new)
        if len(parts) == 4:
            url = 'watchcinema.ru/search/'
            param = ul.quote(parts[3].encode('windows-1251'))
            debug(param, 'param')
            param = 'q=%s&quality=1&poisk=add' % param
            page = mod_request(url, param)
            results = re.findall('<a href="(.+?)" class="video_row_relative">\\W+.+?".+?"><.+?">(.+?)<\\/div><.+?">(.+?)</div></div>\\W+.+?\\W+.+?\\W<.+?url..(.+?)\'', page)
            self.playlistname = '"%s" - %i %s' % (parts[3], len(results), '\xd0\xbd\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe')
            for url, baslik, sure, res in results:
                baslik = baslik.decode('windows-1251').encode('utf-8').upper()
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 baslik,
                 None,
                 res,
                 'http://watchcinema.ru' + url,
                 None,
                 None,
                 res,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        self.prev_page_text = 'Prev'
        self.video_list = video_list_temp
        if len(parts) == 5:
            url1 = 'watchcinema.ru/video/'
            url = url1 + str(parts[4]) + '/'
            chan_counter = 0
            next = int(parts[4]) + 1
            page = mod_request(url)
            results = re.findall('<a href="(.+?)" class="video_row_relative">\\W+.+?\\W+.+?".+?"><.+?">(.+?)<\\/div><.+?">(.+?)</div></div>\\W+.+?\\W+.+?\\W<.+?url..(.+?)\'', page)
            self.playlistname = 'VK EROTICA'
            for url, baslik, sure, res in results:
                baslik = baslik.decode('cp1254').encode('cp1254').upper()
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 baslik,
                 None,
                 res,
                 'http://watchcinema.ru' + url,
                 None,
                 None,
                 res,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        if next != 2:
            self.prev_page_url = 'searchs.xml'
            self.prev_page_text = '\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd1\x8b\xd0\xb4\xd1\x83\xd1\x89\xd0\xb0\xd1\x8f'
        self.video_list = video_list_temp
        if len(parts) == 6:
            url1 = 'watchcinema.ru/category/6/'
            url = url1 + str(parts[5]) + '/'
            chan_counter = 0
            next = int(parts[5]) + 1
            page = mod_request(url)
            results = re.findall('<a href="(.+?)" class="video_row_relative">\\W+.+?\\W+.+?".+?"><.+?">(.+?)<\\/div><.+?">(.+?)</div></div>\\W+.+?\\W+.+?\\W<.+?url..(.+?)\'', page)
            self.playlistname = 'VK EROTICA'
            for url, baslik, sure, res in results:
                baslik = baslik.decode('cp1254').encode('cp1254').upper()
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 baslik,
                 None,
                 res,
                 'http://watchcinema.ru' + url,
                 None,
                 None,
                 res,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        if next != 2:
            self.prev_page_url = 'searchs.xml'
            self.prev_page_text = '\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd1\x8b\xd0\xb4\xd1\x83\xd1\x89\xd0\xb0\xd1\x8f'
        self.video_list = video_list_temp
        return