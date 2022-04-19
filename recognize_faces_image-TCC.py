# USO
# python recognize_faces_image.py --encodings encodings.pickle --image examples/foto15.jpg
# python3.5 recognize_faces_image.py --encodings encodings.pickle --image exemplos/parla_04.jpeg

import face_recognition
import argparse
import pickle
import cv2
import requests ######## walner
import time

start = time.time()
#print("hello")


ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
	model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)

names = []
lista_presenca=[] #walner
lista_convidado=[]	#### Walner	

for encoding in encodings:
	
	matches = face_recognition.compare_faces(data["encodings"],
		encoding, 0.4)
	name = "Unknown"

	if True in matches:

		matchedIdxs = [i for (i, b) in enumerate(matches) if b]
		counts = {}

		#name_recognisized = data["names"][0] #### ENVIAR NOME RECONHECIDO
		name_recognisized = data["names"][matchedIdxs[0]] #### ENVIAR NOME RECONHECIDO

		key_in=1 #### walner
		for i in matchedIdxs:
			name = data["names"][i]
			#### ENVIAR NOME RECONHECIDO #  walner
			#print(i)
			#print(name)
			#print(name_recognisized)
			#print(matchedIdxs)
			if name_recognisized==name and key_in==1 and not(name in lista_convidado): #### walner
				#response = requests.get(f'https://2expressos.localhoost.com/scriptcase9/app/Email_Marketing_CNI/teste_walner/index.php?convidado={name_recognisized}')
				#print(f'https://2expressos.localhoost.com/scriptcase9/app/Email_Marketing_CNI/teste_walner/index.php?convidado={name_recognisized}')
				lista_presenca.append(name_recognisized)
				#print(name)#### walner
				key_in=0
			else: #### walner
				name_recognisized = data["names"][i]#### walner

			counts[name] = counts.get(name, 0) + 1

		name = max(counts, key=counts.get)
	
	names.append(name)

for ((top, right, bottom, left), name) in zip(boxes, names):
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	y = top - 15 if top - 15 > 15 else top + 15
	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.imwrite("saida_imagem.jpg",image)
print(lista_presenca)

end = time.time()
print(end - start)
cv2.waitKey(0) # mostra a foto
cv2.destroyAllWindows()
