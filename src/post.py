from detect import *
from FaceRecognizer import *
import glob
import pickle
import requests

data_dir = '../data/lynk/'

verify_url = 'https://us-central1-lynkhacksmock.cloudfunctions.net/verifyface'
team_name = 'NADS'

with open('FRmod_v1.obj', 'r') as filehandler :
 fr = pickle.load(filehandler) 

log_response = open('response.log', 'w')

for file_name in glob.glob(data_dir+'*') :
	print 'Predicting -- ',file_name
	image_uid = file_name.split('/')[-1].split('.')[0]
	# person_name = label_map[image_uid]

	img, score = face_detect(file_name)
	guess = fr.predict(img)

	data = {"teamname":team_name, "imageuid": image_uid, "name":guess}

	r = requests.post(url, json)
	log_response.write(r.text + '\n')

log_response.close()
