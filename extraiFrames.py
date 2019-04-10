import cv2

#VIDEO = 'video.mp4'

#cap = cv2.VideoCapture("/videos/V_20181114_094741.mp4")
#x = 0
#while cap.isOpened():
#   res, frame = cap.read()
#   nomeDoFrame = 'frame-%d.jpg' % x
#   cv2.imwrite(nomeDoFrame, frame)
#cap.release()
#print ("Succesful")


#vidcap = cv2.VideoCapture("/videos/V_20181114_094741.mp4")
#success,image = vidcap.read()
#count = 0
#success = True
#while success:
#  success,image = vidcap.read()
#  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
#      break
#  count += 1



vidcap = cv2.VideoCapture("videos/V_20181114_094741.mp4")
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count,image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
