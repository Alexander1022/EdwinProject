import pafy
import vlc

def play():
	url = "https://www.youtube.com/watch?v=a8-Pz-6K3Uc&list=PLRmO0NQFpcOKi5uqQoPqPK0fVjK3SuMh-"
	video = pafy.new(url)
	best = video.getbestaudio()
	playurl = best.url
	Instance = vlc.Instance()
	player = Instance.media_player_new()
	Media = Instance.media_new(playurl)
	Media.get_mrl()
	player.set_media(Media)
	player.play()
