# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/MyStreamVOD/Moduls/nStreamModul_kinomaxpro.py
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
        req = urllib2.Request(url, param, {'User-agent': 'Mozilla/5.0 MyStreamVOD 1.2',
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html


class html_parser_kinomaxpro:

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
        url = parts[0]
        page = parts[1]
        name = parts[2].encode('utf-8')
        self.active_site_url = 'kinomaxpro.com'
        if page == 'start':
            self.playlistname = name
            self.video_list = self.get_kinomaxpro_categories(url)
        if page == 'category':
            self.playlist_cat_name = name
            self.playlistname = 'Kinomaxpro CAT: ' + self.playlist_cat_name
            self.video_list = self.get_kinomaxpro_category_films(url)
            self.category_back_url = url
            self.category_title = name
        if page == 'category_page':
            page_nr = ''
            page = url.split('/')
            if len(page) == 6 and page[3] == 'page':
                page_nr = ' PAGE ' + page[4]
            if len(page) == 4 and page[1] == 'page':
                page_nr = ' PAGE ' + page[2]
            self.playlistname = self.playlist_cat_name + page_nr
            self.video_list = self.get_kinomaxpro_category_films(url)
            self.category_back_url = url
        if page == 'film':
            self.kino_title = name
            self.playlistname = self.playlist_cat_name + ' ' + name
            self.video_list = self.get_kinomaxpro_film(url)

    def get_kinomaxpro_categories(self, url):
        try:
            page = mod_request(url).decode('cp1251').encode('utf-8')
            video_list_temp = []
            chan_counter = 1
            new = (chan_counter,
             'NEW',
             None,
             None,
             None,
             'nStreamModul@' + self.active_site_url + '/@category@NEW',
             None,
             '',
             '',
             None,
             None)
            video_list_temp.append(new)
            regex = re.findall('<a href="/(.*)/">(.*)</a>', page)
            for text in regex:
                title = text[1]
                url = text[0]
                chan_counter += 1
                chan_tulpe = (chan_counter,
                 title,
                 None,
                 None,
                 None,
                 'nStreamModul@' + self.active_site_url + '/' + url + '/@category@' + title,
                 None,
                 '',
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

            if len(video_list_temp) < 1:
                print 'ERROR CAT LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_kinomaxpro_category'

        self.prev_page_url = 'http://nstream.ucoz.ru/portal/portal.xml'
        self.prev_page_text = 'Back'
        return video_list_temp

    def get_kinomaxpro_category_films(self, url):
        try:
            page = mod_request(url).decode('cp1251').encode('utf-8')
            video_list_temp = []
            chan_counter = 0
            regex_films = re.findall('<div class="poster">\\s.*<img.*src="(.*jpg)".*\\s.*\\s.*\\s.*\\s.*<a href="(http.*html)".*>(.*)<\\/a', page)
            regex_descr = re.findall('<div id="news.*">(.*)<\\/div>', page)
            for text in regex_films:
                chan_counter += 1
                url = text[1].replace('http://', '')
                img_url = text[0]
                title = text[2]
                descr = regex_descr[chan_counter - 1]
                chan_tulpe = (chan_counter,
                 title,
                 descr,
                 'http://' + self.active_site_url + img_url,
                 None,
                 'nStreamModul@' + url + '@film@' + title,
                 None,
                 'http://' + self.active_site_url + img_url,
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)
                navi = re.findall('<div class="navigation">\\s*.*<a\\s+href=".*">.*<\\/a>.*\\s*<\\/div>', page)

            if len(navi) > 0:
                pages = re.findall('ref=\\"([^\\"]*)\\">([^\\d][^<"]*)', navi[0])
                if len(pages) == 1:
                    if pages[0][1].find('8592') == -1:
                        self.next_page_url = pages[0][0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                        text = pages[0][1].replace(' &#8594;', '')
                        self.next_page_text = text
                        self.prev_page_url = 'nStreamModul@kinomaxpro.com@start@KINOMAXPRO ALL CATEGORIES'
                        self.prev_page_text = 'Categories'
                    else:
                        self.prev_page_url = pages[0][0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                        text = pages[0][1].replace('&#8592; ', '')
                        self.prev_page_text = text
                if len(pages) == 2:
                    self.next_page_url = pages[1][0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                    self.next_page_text = pages[1][1].replace(' &#8594;', '')
                    self.prev_page_url = pages[0][0].replace('http://', 'nStreamModul@') + '@category_page@' + self.playlist_cat_name
                    self.prev_page_text = pages[0][1].replace('&#8592; ', '')
            if len(video_list_temp) < 1:
                print 'ERROR CAT_FIL LIST_LEN = %s' % len(video_list_temp)
        except:
            print 'ERROR get_kinomaxpro_category'

        return video_list_temp

    def get_kinomaxpro_film(self, url):
        page = mod_request(url)
        ref_url_vimeo = url
        chan_counter = 0
        video_list_temp = []
        trailer = re.findall('param.*&videoUrl=(http:\\/\\/.*)&videoHDUrl=', page)
        img = re.findall('<div class="poster">\\s.*<img.*src="(.*jpg)"', page)
        if len(trailer) > 0:
            chan_counter = chan_counter + 1
            url = trailer[0]
            chan_tulpe = (chan_counter,
             self.kino_title + '(trailer)',
             '',
             'http://' + self.active_site_url + img[0],
             url,
             None,
             None,
             'http://' + self.active_site_url + img[0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        vk = re.findall('<iframe src="(http:\\/\\/vk.*)" width', page)
        if len(vk) > 0:
            url = vk[0].replace('&amp;', '&')
            chan_counter = chan_counter + 1
            chan_tulpe = (chan_counter,
             self.kino_title + ' (vkontakte)',
             '',
             'http://' + self.active_site_url + img[0],
             url,
             None,
             None,
             'http://' + self.active_site_url + img[0],
             '',
             None,
             None)
            video_list_temp.append(chan_tulpe)
        vkontakte2 = re.findall('value=.(http:\\/\\/vkontakte.ru\\/[^<"]*).>([^<]*)', page)
        if len(vkontakte2) > 0:
            for film in vkontakte2:
                title = film[1].decode('cp1251').encode('utf-8')
                url = film[0].replace('&amp;', '&')
                chan_counter = chan_counter + 1
                chan_tulpe = (chan_counter,
                 self.kino_title + '/' + title + ' (vkontakte)',
                 '',
                 'http://' + self.active_site_url + img[0],
                 url,
                 None,
                 None,
                 'http://' + self.active_site_url + img[0],
                 '',
                 None,
                 None)
                video_list_temp.append(chan_tulpe)

        vimeo = re.findall('iframe.*src="(http:\\/\\/player.vimeo.com\\/[^<"]*)', page)
        if len(vimeo) > 0:
            url_vimeo = vimeo[0]
            url_ref = 'http://' + ref_url_vimeo
            request = urllib2.Request(url_vimeo, None, {'User-agent': 'Mozilla/5.0 MyStreamVOD 0.1',
             'Connection': 'Close'})
            request.add_header('Referer', url_ref)
            page = urllib2.urlopen(request)
            page = page.read()
            params = re.findall('"signature":"([0-9a-f]{32})","timestamp":([0-9]+),.*"video":\\{"id":(\\d+).*', page)
            qualitys = re.findall('{"h264":[^\\}]*', page)
            if qualitys:
                qualitys = re.findall('"(hd|sd|mobile)"', qualitys[0])
                for quality in qualitys:
                    url = 'http://player.vimeo.com/play_redirect?clip_id=video/' + params[0][2] + '&sig=' + params[0][0] + '&time=' + params[0][1] + '&quality=' + quality + '&codecs=H264,VP8,VP6&type=moogaloop&embed_location=' + url_ref
                    chan_counter = chan_counter + 1
                    chan_tulpe = (chan_counter,
                     self.kino_title + ' (vimeo ' + quality + ')',
                     '',
                     'http://' + self.active_site_url + img[0],
                     url,
                     None,
                     None,
                     'http://' + self.active_site_url + img[0],
                     '',
                     None,
                     None)
                    video_list_temp.append(chan_tulpe)

        self.prev_page_url = 'nStreamModul@kinomaxpro.com@start@KINOMAXPRO ALL CATEGORIES'
        self.prev_page_text = 'Back'
        return video_list_temp