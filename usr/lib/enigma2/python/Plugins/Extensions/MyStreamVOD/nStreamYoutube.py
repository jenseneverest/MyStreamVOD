import urllib2, re
import nVars
from urlparse import parse_qs
from urllib import quote, unquote_plus, unquote
from Tools import Notifications
from Screens.MessageBox import MessageBox
import hashlib
VIDEO_FMT_PRIORITY_MAP = nVars.VIDEO_FMT_PRIORITY_MAP
VIDEO_FMT_NAME = {'38': 'MP4 Original (HD) ',
 '37': 'MP4 1080p (HD) ',
 '22': 'MP4 720p (HD) ',
 '18': 'MP4 360p ',
 '35': 'FLV 480p ',
 '34': 'FLV 360p '}

class youtube_url:

    def __init__(self):
        self.quality = ''

    def get_youtube_link2(self, url):
        video_url = url
        error = None
        try:
            self.quality = ''
            if url.find('youtube') > -1:
                found = False
                finder = url.find('=')
                video_id = url[finder + 1:]
                for el in ['&el=embedded',
                 '&el=detailpage',
                 '&el=vevo',
                 '']:
                    info_url = 'http://www.youtube.com/get_video_info?&video_id=%s%s&ps=default&eurl=&gl=US&hl=en' % (video_id, el)
                    request = urllib2.Request(info_url, None, {'User-agent': 'Mozilla/5.0 nStreamVOD 0.1',
                     'Connection': 'Close'})
                    try:
                        infopage = urllib2.urlopen(request).read()
                        videoinfo = parse_qs(infopage)
                        if ('url_encoded_fmt_stream_map' or 'fmt_url_map') in videoinfo:
                            found = True
                            break
                    except Exception as ex:
                        print ex + 'YT ERROR 1'

                if found:
                    video_fmt_map = {}
                    fmt_infomap = {}
                    if videoinfo.has_key('url_encoded_fmt_stream_map'):
                        tmp_fmtUrlDATA = videoinfo['url_encoded_fmt_stream_map'][0].split(',')
                    else:
                        tmp_fmtUrlDATA = videoinfo['fmt_url_map'][0].split(',')
                    for fmtstring in tmp_fmtUrlDATA:
                        fmturl = fmtid = ""
                        if videoinfo.has_key('url_encoded_fmt_stream_map'):
                            try:
                                for arg in fmtstring.split('&'):
                                    if arg.find('=') >= 0:
                                        key, value = arg.split('=')
                                        if key == 'itag':
                                            if len(value) > 3:
                                                value = value[:2]
                                            fmtid = value
                                        elif key == 'url':
                                            fmturl = value
                                        elif key == 'sig':
                                            fmtsig = value

                                if fmtid != "" and fmturl != "" and VIDEO_FMT_PRIORITY_MAP.has_key(fmtid):
                                    video_fmt_map[VIDEO_FMT_PRIORITY_MAP[fmtid]] = {'fmtid': fmtid,
                                     'fmturl': unquote_plus(fmturl),
                                     'fmtsig': fmtsig}
                                    fmt_infomap[int(fmtid)] = "%s" %(unquote_plus(fmturl))
                                fmturl = fmtid = ""
                            except:
                                print 'error YT2:'

                        else:
                            fmtid, fmturl = fmtstring.split('|')
                        if VIDEO_FMT_PRIORITY_MAP.has_key(fmtid) and fmtid != '':
                            video_fmt_map[VIDEO_FMT_PRIORITY_MAP[fmtid]] = {'fmtid': fmtid,
                             'fmturl': unquote_plus(fmturl)}
                            fmt_infomap[int(fmtid)] = unquote_plus(fmturl)

                    if video_fmt_map and len(video_fmt_map):
                        best_video = video_fmt_map[sorted(video_fmt_map.iterkeys())[0]]
                        video_url = "%s" %(best_video['fmturl'].split(';')[0])
                        self.quality = VIDEO_FMT_NAME[video_fmt_map[sorted(video_fmt_map.iterkeys())[0]]['fmtid']]
                elif videoinfo.has_key('errorcode') and videoinfo.has_key('reason'):
                    reason = videoinfo['reason']
                    print 'ERROR REASON'
                    error = reason[0]
        except Exception as ex:
            print ex

        if video_url != url:
            print 'YOUTUBE VIDEO URL' + video_url
        return (error, video_url)