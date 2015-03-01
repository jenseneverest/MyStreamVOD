# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/Moduls/nStreamModul_m3u.py
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
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 MyStreamVOD 2.1',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_m3u:

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

    def reset_buttons(self):
        self.kino_title = ''
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
        return

    def get_list(self, url):
        debug(url, 'MODUL URL: ')
        self.reset_buttons()
        parts = url.split('@')
        filename = parts[0]
        name = parts[2].encode('utf-8')
        self.playlistname = name
        ts = None
        if url.find('TS') > -1:
            ts = 'True'
        try:
            video_list_temp = []
            chan_counter = 0
            if filename.find('http') > -1:
                url = filename.replace('http://', '')
                myfile = mod_request(url)
            else:
                myfile = open('/usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/m3uDir/%s' % filename, 'r').read()
            regex = re.findall('#EXTINF.*,(.*\\s)\\s*(.*)', myfile)
            if not len(regex) > 0:
                regex = re.findall('((.*.+)(.*))', myfile)
            for text in regex:
                title = text[0].strip()
                url = text[1].strip()
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 '',
                 'xxx.png',
                 url,
                 None,
                 None,
                 '',
                 '',
                 None,
                 ts)
                video_list_temp.append(chan_tulpe)
                if len(video_list_temp) < 1:
                    print 'ERROR m3u CAT LIST_LEN = %s' % len(video_list_temp)

        except:
            print 'ERROR m3u'

        self.video_list = video_list_temp
        return