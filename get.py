import configparser
import StringIO
import mutagen


import requests

r = requests.get('http://www2.kuow.org/stream/swingyears.pls')

buf = StringIO.StringIO(r.content)
config = configparser.ConfigParser()
config.readfp(buf)
mp3 = config.get('playlist', 'File1')

filename = mp3.split('/')[-1]
r = requests.get(mp3, stream=True)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
#
# mutagen.File("kuow-tsy.mp3")
#
# from mutagen.id3 import ID3
#
# audio = ID3("kuow-tsy.mp3")
#
#
# from mutagen.easyid3 import EasyID3
# filename = "foo.mp3"
#
# try:
#     meta = EasyID3(filename)
# except mutagen.id3.ID3NoHeaderError:
#     meta = mutagen.File(filePath, easy=True)
#     meta.add_tags()
#     meta
#
# meta['title'] = "This is a title"
# meta['artist'] = "Artist Name"
# meta['genre'] = "Space Funk"meta.save()
# changed = EasyID3(filename)
# changed
# {'genre': [u'Space Funk'], 'title': [u'This is a title'], 'artist': [u'Artist Name']}
