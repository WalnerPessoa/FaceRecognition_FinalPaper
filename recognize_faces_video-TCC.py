# USO
# python3.5 recognize_faces_video.py --encodings encodings.pickle --detection-method hog
# python recognize_faces_video-TCC.py --encodings encodings.pickle --input 0 --detection-method hog 
# python recognize_faces_video.py --encodings encodings.pickle --output output/jurassic_park_trailer_output.avi --display 0

from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
import requests ######## walner
from datetime import datetime # Walner
import smtplib ######## email Walner
from email.mime.text import MIMEText ######## email walner


ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-o", "--output", type=str,
	help="path to output video")

ap.add_argument("-i", "--input", type=int, default=0, ## Walner
	help="device for diferet camera") ## Walner


ap.add_argument("-y", "--display", type=int, default=1,
	help="whether or not to display output frame to screen")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())


print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()

#################
# device for diferet camera
#
vs = VideoStream(src=0).start() ##### trocar para webcam
#vs = VideoStream(src=1).start() ##### trocar para webcam
#################
#vs = cv2.VideoCapture(0) ## wawlner
#vs = cv2.VideoCapture(args["input"]) ## wawlner


#################
#fps = vs.get(cv2.CAP_PROP_FPS)
#print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
##fps = vs.set(cv2.CAP_PROP_FPS,10.)
#fps = vs.get(cv2.CAP_PROP_FPS)
#print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

#vs.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
#vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

##########################
# Find OpenCV version
#(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#print("VERSAO: ", (cv2.__version__).split('.'))
# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.

#if int(major_ver) < 3 :
#	fps = vs.get(cv2.cv.CV_CAP_PROP_FPS)
#	print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#else :
#	fps = vs.get(cv2.CAP_PROP_FPS)
#	print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

##########################

#vs = cv2.VideoCapture(args["input"]) ## wawlner

writer = None
time.sleep(2.0)
lista_convidado=[]	#### Walner	

# TCC print("Digite numero whats App: ") #===== whatsAPP
# TCC num_whats_app= input("Digite numero whats App com DDD: ") #===== whatsAPP
# TCC print("Numero: ", num_whats_app)#===== whatsAPP
now = datetime.now()

lista_presenca=[] #walner

while True:
	frame = vs.read()
	# convert the input frame from BGR to RGB then resize it to have
	#rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #--------------------------

	##########################
	W = 480.
	#W = 720.
	#W = 1080.
	#W = 1920.


	#frame = imutils.resize(frame, width=W)### Walner teste
	height, width, depth = frame.shape ##### ---- linha com erros
	#(height, width) = frame.shape[:2]

	#(height, width) = frame.shape ### Walner teste

	imgScale = W/width
	newX,newY = frame.shape[1]*imgScale, frame.shape[0]*imgScale
	frame = cv2.resize(frame,(int(newX),int(newY)))
	##########################


	# COM 750px (PARA ACELERARA O PROCESSO)
	#rgb = cv2.resize(frame,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC) ### WALNER REDUZIR IMG
	#rgb = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) ### nasser REDUZIR IMG
	#rgb = cv2.resize(frame,(200,300),interpolation=cv2.INTER_AREA)
	#rgb = cv2.resize(frame,(200,300))
	

	##########################
	# convert the input frame from BGR to RGB then resize it to have
	# a width of 750px (to speedup processing)
	##### trocar para webcam
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#--------------------------
	#rgb = imutils.resize(frame, width=750) # width=250 #--------------------------
	frame = imutils.resize(frame, width=750) #Walner
	r = frame.shape[1] / float(rgb.shape[1]) #--------------------------
	##########################

	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []
	key_in=1 #### walner	
	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding, 0.4)
		name = "Unknown"
		

		

		if True in matches:
			
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}


			name_recognisized = data["names"][0] #### ENVIAR NOME RECONHECIDO
			for i in matchedIdxs:
				name = data["names"][i]
				#### ENVIAR NOME RECONHECIDO #  walner
				#print("1 - ", lista_convidado)
				#if not(name in lista_convidado): ##### Walner
				#if lista_convidado.index(name) == False: ##### Walner
					#lista_convidado.append(name) #### Walner
				#print("2 - ", lista_convidado)
					#index =  lista_convidado.index(name)
				if name_recognisized==name and key_in==1 and not(name in lista_convidado): #### walner
					now = datetime.now()
					name_hora=name_recognisized+' '+str(now.hour)+'h'+str(now.minute)
					lista_presenca.append(name_hora)


					########################################### emal 
					# https://humberto.io/pt-br/blog/enviando-e-recebendo-emails-com-python/
					# https://myaccount.google.com/lesssecureapps?pli=1
					# https://support.google.com/accounts/answer/185833
					# conexão com os servidores do google
					# TCC smtp_ssl_host = 'smtp.gmail.com'
					# TCC smtp_ssl_port = 465
					# username ou email para logar no servidor
					# TCC username = 'walner@sempreceub.com'
					#password = 'gzevdbavxkfpupah'
					# TCC password = 'jelwvktadvknzqvs'
					# TCC from_addr = 'walner@sempreceub.com'
					# TCC to_addrs = ['walleu@gmail.com']
					###########   to_addrs.append('walner@sempreceub.com')
					# a biblioteca email possuí vários templates
					# para diferentes formatos de mensagem
					# neste caso usaremos MIMEText para enviar
					# somente texto
					# TCC message = MIMEText(f'Sistema Reconhecimento Facial\n{name_recognisized} chegou no evento às {now.hour}h{now.minute}.\n\n\n Estão presentes: \n{lista_presenca} ' )
					# TCC message['subject'] = f'{name_recognisized} chegou.'
					# TCC message['from'] = from_addr
					# TCC message['to'] = ', '.join(to_addrs)
					# conectaremos de forma segura usando SSL
					#server = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
					# TCC server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
					#
					# para interagir com um servidor externo precisaremos
					# fazer login nele
					# TCC server.login(username, password)
					# TCC server.sendmail(from_addr, to_addrs, message.as_string())
					# TCC server.quit()
					########################################### emal 

						
					### AVISO PARA WAHTS APP++++++++++++++++++++++++++++++++
					#####url = 'https://eu61.chat-api.com/instance57820/sendMessage?token=02v6iwd57hmt4qlu'
					#---url = "https://eu61.chat-api.com/instance57820/sendMessage?token=02v6iwd57hmt4qlu"
					#---num_whats_app=str(num_whats_app)
					#---data_whats = {"phone": "55"+num_whats_app, "body": "Presidente "+name_recognisized+ " chegou no evento."}
					#---data_whats2 = {"phone": "55"+num_whats_app, "body": "Estão presentes: "+str(lista_presenca)}

					##data = {"phone": "5561983415277", "body": "Presidente "+name_recognisized+ " chegou."}
					#print(type(num_whats_app))
					#print(num_whats_app)
					#---res = requests.post(url, json=data_whats)
					#---res = requests.post(url, json=data_whats2)
					#print ('teste :',res.text)
					### AVISO PARA WAHTS APP++++++++++++++++++++++++++++++++

					### AVISO PARA EMAIL
					# ###### response = requests.get(f'https://2expressos.localhoost.com/scriptcase9/app/Email_Marketing_CNI/teste_walner/index.php?convidado={name_recognisized}')
				

					#print(f'https://2expressos.localhoost.com/scriptcase9/app/Email_Marketing_CNI/teste_walner/index.php?convidado={name_recognisized}')
					print("Face Identificada: ", name_recognisized)
					lista_convidado.append(name) #### Walner
					index =  lista_convidado.index(name)
					#print(lista_convidado[index])#### walner
					key_in=0
				else: #### walner
					name_recognisized = data["names"][i]#### walner

				counts[name] = counts.get(name, 0) + 1

			
			name = max(counts, key=counts.get)
		
		names.append(name)

	for ((top, right, bottom, left), name) in zip(boxes, names):
		top = int(top * r)
		right = int(right * r)
		bottom = int(bottom * r)
		left = int(left * r)

		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)

	
	if writer is None and args["output"] is not None:
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args["output"], fourcc, 20,
			(frame.shape[1], frame.shape[0]), True)

	
	if writer is not None:
		writer.write(frame)

	
	if args["display"] > 0:
		cv2.imshow("Frame", frame) #################################
		key = cv2.waitKey(1) & 0xFF

		# CLICAR "q" PARA SAIR
		if key == ord("q"):
			break

cv2.destroyAllWindows()
vs.stop()

if writer is not None:
	writer.release()