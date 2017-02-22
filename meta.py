import mutagen
from mutagen.easyid3 import EasyID3
import datetime
filename = "foo.mp3"

try:
    meta = EasyID3(filename)
except mutagen.id3._util.ID3NoHeaderError:
    meta = mutagen.File(filename, easy=True)
    meta.add_tags()
    meta

today = datetime.date.today()

meta['title'] = "Swingyears: %s" % today
meta['artist'] = "KUOW"
meta['genre'] = "swing"
meta.save()
changed = EasyID3(filename)
print changed
