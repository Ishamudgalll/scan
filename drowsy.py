import numpy as np
import os.path
import cv2
import json
from flask import Flask,request, Response
import uuid

def faceDetect(img):
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
	#save file
	path_file=('https://github.com/Ishamudgalll/scan/tree/master/static/%s.jpg' %uuid.uuid4().hex)
	cv2.imwrite(path_file,img)
	return json.dumps(path_file)

#API
app=Flask(__name__)
@app.route('/api/upload',methods=['POST'])
def upload():
#retrieve image from client
	img=cv2.imdecode(np.fromstring(request.files['image'].read(),np.uint8),cv2.IMREAD_UNCHANGED)
#process image
	img_processed=faceDetect(img)
	#response
	return Response(response=img_processed,status=200,mimetype="application/json") # return json 

#start server
#app.run(host="0.0.0.0",port=5000)
if __name__ == "__main__":
    app.run(debug=True)
