CHANNEL_NUMBER = [7,10,40,33,0]
CHANNEL_NAME = [55,7,670,22,1]
FONT_0 = ('RegularIPTV', 20)
FONT_1 = ('RegularIPTV', 24)
BLOCK_H = 37
NTIMEOUT = 50

VIDEO_FMT_PRIORITY_MAP = {
	'38' : 1, #MP4 Original (HD)
	'37' : 2, #MP4 1080p (HD)
	'22' : 3, #MP4 720p (HD)
	'18' : 4, #MP4 360p
	'35' : 5, #FLV 480p
	'34' : 6, #FLV 360p
}