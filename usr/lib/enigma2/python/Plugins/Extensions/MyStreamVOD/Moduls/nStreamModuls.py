class html_parser_moduls:
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
		from nStreamModul_m3u import html_parser_m3u
		if(url.find('m3u')>-1):
			m3u = html_parser_m3u()
			m3u.get_list(url)
			self.video_list = m3u.video_list
			self.next_page_url = m3u.next_page_url
			self.next_page_text = m3u.next_page_text
			self.prev_page_url = m3u.prev_page_url
			self.prev_page_text = m3u.prev_page_text
			self.search_text = m3u.search_text
			self.search_on = m3u.search_on
			self.active_site_url = m3u.active_site_url
			self.playlistname = m3u.playlistname
			self.playlist_cat_name = m3u.playlist_cat_name
			self.kino_title = m3u.kino_title
			self.category_back_url = m3u.category_back_url
			self.error = m3u.error
		from nStreamModul_youtubesearch import html_parser_youtubesearch
		if(url.find('youtubesearch')>-1):
			youtubesearch = html_parser_youtubesearch()
			youtubesearch.get_list(url)
			self.video_list = youtubesearch.video_list
			self.next_page_url = youtubesearch.next_page_url
			self.next_page_text = youtubesearch.next_page_text
			self.prev_page_url = youtubesearch.prev_page_url
			self.prev_page_text = youtubesearch.prev_page_text
			self.search_text = youtubesearch.search_text
			self.search_on = youtubesearch.search_on
			self.active_site_url = youtubesearch.active_site_url
			self.playlistname = youtubesearch.playlistname
			self.playlist_cat_name = youtubesearch.playlist_cat_name
			self.kino_title = youtubesearch.kino_title
			self.category_back_url = youtubesearch.category_back_url
			self.error = youtubesearch.error
		from nStreamModul_vkontaktesearch import html_parser_vkontaktesearch
		if(url.find('vkontaktesearch')>-1):
			vkontaktesearch = html_parser_vkontaktesearch()
			vkontaktesearch.get_list(url)
			self.video_list = vkontaktesearch.video_list
			self.next_page_url = vkontaktesearch.next_page_url
			self.next_page_text = vkontaktesearch.next_page_text
			self.prev_page_url = vkontaktesearch.prev_page_url
			self.prev_page_text = vkontaktesearch.prev_page_text
			self.search_text = vkontaktesearch.search_text
			self.search_on = vkontaktesearch.search_on
			self.active_site_url = vkontaktesearch.active_site_url
			self.playlistname = vkontaktesearch.playlistname
			self.playlist_cat_name = vkontaktesearch.playlist_cat_name
			self.kino_title = vkontaktesearch.kino_title
			self.category_back_url = vkontaktesearch.category_back_url
			self.error = vkontaktesearch.error
		from nStreamModul_m3u import html_parser_m3u
		if(url.find('m3u')>-1):
			m3u = html_parser_m3u()
			m3u.get_list(url)
			self.video_list = m3u.video_list
			self.next_page_url = m3u.next_page_url
			self.next_page_text = m3u.next_page_text
			self.prev_page_url = m3u.prev_page_url
			self.prev_page_text = m3u.prev_page_text
			self.search_text = m3u.search_text
			self.search_on = m3u.search_on
			self.active_site_url = m3u.active_site_url
			self.playlistname = m3u.playlistname
			self.playlist_cat_name = m3u.playlist_cat_name
			self.kino_title = m3u.kino_title
			self.category_back_url = m3u.category_back_url
			self.error = m3u.error
		from nStreamModul_zvukoff import html_parser_zvukoff
		if(url.find('zvukoff')>-1):
			zvukoff = html_parser_zvukoff()
			zvukoff.get_list(url)
			self.video_list = zvukoff.video_list
			self.next_page_url = zvukoff.next_page_url
			self.next_page_text = zvukoff.next_page_text
			self.prev_page_url = zvukoff.prev_page_url
			self.prev_page_text = zvukoff.prev_page_text
			self.search_text = zvukoff.search_text
			self.search_on = zvukoff.search_on
			self.active_site_url = zvukoff.active_site_url
			self.playlistname = zvukoff.playlistname
			self.playlist_cat_name = zvukoff.playlist_cat_name
			self.kino_title = zvukoff.kino_title
			self.category_back_url = zvukoff.category_back_url
			self.error = zvukoff.error
		from nStreamModul_youtubesearch import html_parser_youtubesearch
		if(url.find('youtubesearch')>-1):
			youtubesearch = html_parser_youtubesearch()
			youtubesearch.get_list(url)
			self.video_list = youtubesearch.video_list
			self.next_page_url = youtubesearch.next_page_url
			self.next_page_text = youtubesearch.next_page_text
			self.prev_page_url = youtubesearch.prev_page_url
			self.prev_page_text = youtubesearch.prev_page_text
			self.search_text = youtubesearch.search_text
			self.search_on = youtubesearch.search_on
			self.active_site_url = youtubesearch.active_site_url
			self.playlistname = youtubesearch.playlistname
			self.playlist_cat_name = youtubesearch.playlist_cat_name
			self.kino_title = youtubesearch.kino_title
			self.category_back_url = youtubesearch.category_back_url
			self.error = youtubesearch.error
		from nStreamModul_vkontaktesearch import html_parser_vkontaktesearch
		if(url.find('vkontaktesearch')>-1):
			vkontaktesearch = html_parser_vkontaktesearch()
			vkontaktesearch.get_list(url)
			self.video_list = vkontaktesearch.video_list
			self.next_page_url = vkontaktesearch.next_page_url
			self.next_page_text = vkontaktesearch.next_page_text
			self.prev_page_url = vkontaktesearch.prev_page_url
			self.prev_page_text = vkontaktesearch.prev_page_text
			self.search_text = vkontaktesearch.search_text
			self.search_on = vkontaktesearch.search_on
			self.active_site_url = vkontaktesearch.active_site_url
			self.playlistname = vkontaktesearch.playlistname
			self.playlist_cat_name = vkontaktesearch.playlist_cat_name
			self.kino_title = vkontaktesearch.kino_title
			self.category_back_url = vkontaktesearch.category_back_url
			self.error = vkontaktesearch.error
		from nStreamModul_kinomaxpro import html_parser_kinomaxpro
		if(url.find('kinomaxpro')>-1):
			kinomaxpro = html_parser_kinomaxpro()
			kinomaxpro.get_list(url)
			self.video_list = kinomaxpro.video_list
			self.next_page_url = kinomaxpro.next_page_url
			self.next_page_text = kinomaxpro.next_page_text
			self.prev_page_url = kinomaxpro.prev_page_url
			self.prev_page_text = kinomaxpro.prev_page_text
			self.search_text = kinomaxpro.search_text
			self.search_on = kinomaxpro.search_on
			self.active_site_url = kinomaxpro.active_site_url
			self.playlistname = kinomaxpro.playlistname
			self.playlist_cat_name = kinomaxpro.playlist_cat_name
			self.kino_title = kinomaxpro.kino_title
			self.category_back_url = kinomaxpro.category_back_url
			self.error = kinomaxpro.error
		from nStreamModul_kinomaxpro import html_parser_kinomaxpro
		if(url.find('kinomaxpro')>-1):
			kinomaxpro = html_parser_kinomaxpro()
			kinomaxpro.get_list(url)
			self.video_list = kinomaxpro.video_list
			self.next_page_url = kinomaxpro.next_page_url
			self.next_page_text = kinomaxpro.next_page_text
			self.prev_page_url = kinomaxpro.prev_page_url
			self.prev_page_text = kinomaxpro.prev_page_text
			self.search_text = kinomaxpro.search_text
			self.search_on = kinomaxpro.search_on
			self.active_site_url = kinomaxpro.active_site_url
			self.playlistname = kinomaxpro.playlistname
			self.playlist_cat_name = kinomaxpro.playlist_cat_name
			self.kino_title = kinomaxpro.kino_title
			self.category_back_url = kinomaxpro.category_back_url
			self.error = kinomaxpro.error
		from nStreamModul_zvukoff import html_parser_zvukoff
		if(url.find('zvukoff')>-1):
			zvukoff = html_parser_zvukoff()
			zvukoff.get_list(url)
			self.video_list = zvukoff.video_list
			self.next_page_url = zvukoff.next_page_url
			self.next_page_text = zvukoff.next_page_text
			self.prev_page_url = zvukoff.prev_page_url
			self.prev_page_text = zvukoff.prev_page_text
			self.search_text = zvukoff.search_text
			self.search_on = zvukoff.search_on
			self.active_site_url = zvukoff.active_site_url
			self.playlistname = zvukoff.playlistname
			self.playlist_cat_name = zvukoff.playlist_cat_name
			self.kino_title = zvukoff.kino_title
			self.category_back_url = zvukoff.category_back_url
			self.error = zvukoff.error
		return self.video_list
