from pydub import AudioSegment as Audio
from pydub.playback import play

song = Audio.from_mp3('ex021/HEYYEYA.mp3')
play(song)