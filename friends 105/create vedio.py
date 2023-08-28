import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images.append(file_name)
        
#print(len(images))
count = len(images)

frame = cv2.imread(images[0])
h,w,c = frame.shape
size = (w,h)
#print(size)

out = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.releas()
print("Done")

