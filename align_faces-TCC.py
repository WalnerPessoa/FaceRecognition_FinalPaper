# USAGE
# python align_faces.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/000006.jpg
# python align_faces.py --shape-predictor shape_predictor_68_face_landmarks.dat --dataset dataset  --writing output/file
# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import paths ########### novo
import os ########### novo
import argparse
import imutils
import dlib
import cv2

print("[INFO] inici programa...") ########### novo

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-w", "--writing", required=True, # p/Walner
	help="path to output image") # adicionado p/Walner
args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...") ########### novo
imagePaths = list(paths.list_images(args["dataset"])) ########### novo
knownNames = [] ########### novo
total = 0 ########### novo

for (i, imagePath) in enumerate(imagePaths): ########### novo
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1, ########### novo
		len(imagePaths))) ########### novo
	name = imagePath.split(os.path.sep)[-2] ########### novo

	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor and the face aligner
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(args["shape_predictor"])
	fa = FaceAligner(predictor, desiredFaceWidth=256)

	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=800)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# show the original input image and detect faces in the grayscale
	# image
	cv2.imshow("Input", image)
	rects = detector(gray, 2)


	knownNames.append(name) ########### novo
	total += 1 ########### novo
	print("[INFO] serializing {} encodings...".format(total)) ########### novo
	# loop over the face detections
	for rect in rects:
		# extract the ROI of the *original* face, then align the face
		# using facial landmarks
		(x, y, w, h) = rect_to_bb(rect)
		try:
			faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
		except:
			try:
				faceOrig = imutils.resize(image[y:y + h, x:x + w], width=128)
			except:
				continue
		faceAligned = fa.align(image, gray, rect)

		import uuid
		f = str(uuid.uuid4())
		#cv2.imwrite("output/" + f + ".png", faceAligned)


		# display the output images
		#cv2.imshow("Original", faceOrig)
		#cv2.imshow("Aligned", faceAligned)
		#cv2.waitKey(0)

		#cv2.imwrite(args["writing"]+str(i)+".jpg",faceAligned)# Walner
		cv2.imwrite("output/"+name+str(i)+".jpg",faceAligned)# Walner

		#data_file=faceAligned # Walner
		#f = open(args["writing"], "wb") # Walner
		#f.write(data_file) # Walner
		#f.close() # Walner