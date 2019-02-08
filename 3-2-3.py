import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with requests.Session() as s:
    r=s.get('http://httpbin.org/stream/20', stream=True)
    #print(r.text)
    #print(r.encoding)
    if r.encoding is None:
        r.encoding ='utf-8'

    for line in r.iter_lines(decode_unicode=True):
        #print(line)
        b = json.loads(line)
        #print(type(b)) #class 'dict'
        for e in b.keys():
            print("key:", e, "values:", b[e])
