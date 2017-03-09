import urllib2
ret = urllib2.urlopen('http://hostname/directory/file.jpg')
if ret.code == 200:
    print("Exists!")
else:
	print("oo")
# via http://stackoverflow.com/questions/7347888/how-do-i-check-if-a-file-on-http-exists-using-python-django