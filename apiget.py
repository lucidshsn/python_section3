import sys
import io
import requests, json
# import soundcloud

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# # create a client object with your app credentials
# client = soundcloud.Client(client_id='wrtipo@gmail.com')
# print(client)
# # fetch track to stream
# track_url = 'http://soundcloud.com/forss/voca-nomen-tuum'
#
# # get the tracks streaming URL
# track = client.get('/resolve', url=track_url)
#
# # print the tracks stream URL
# for track in client.get('/tracks/%d/comments' % track.id):
#     print 'Someone said: %s at %d' % (comment.body, comment.timestamp)

r = requests.get('http://developers.soundcloud.com/')
r.raise_for_status()
print(r.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set('name', 'kim', domain='httpbin.org', path='/cookies')

# r= requests.get('http://httpbin.org/cookies', cookies=jar)
# r.raise_for_status()
# print(r.text)

# r= requests.get('https://github.com', timeout=3)
# print(r.text)
