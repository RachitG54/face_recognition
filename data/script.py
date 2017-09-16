# -*- coding: utf-8 -*-
import urllib
#urllib.urlretrieve("https://firebasestorage.googleapis.com/v0/b/lynkhacksmock.appspot.com/o/10.jpg?alt=media&token=538dec79-1f84-4c47-8185-bfcc3ce4aa3a", "local-filename.jpg")

file = open('dataset.json', 'rb') 
arr = file.readlines()
arr2 =  [x.strip() for x in arr[0].split('\"')]
imgnme = ""
url = []
for i in xrange(len(arr2)):
	if(arr2[i]=='imageuid'):
		i+=2
		imgnme = 'lynk/' + arr2[i]+'.jpg'
	elif(arr2[i]=='url'):
		i+=2
		imgurl = arr2[i]
		url.append(imgurl)
		print imgnme+"\n"+imgurl
		urllib.urlretrieve(imgurl,imgnme)
print len(url)