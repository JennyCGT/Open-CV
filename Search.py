import cv2
import numpy as np

#load images and template
image_p=cv2.imread("original.jpg",0)
template=cv2.imread("4.jpg",0)
original=cv2.imread("original.jpg",1)
original1=cv2.merge((image_p,image_p,image_p))

#image_p= cv2.merge((image_p,image_p,image_p))

#mostrar la image_p
cv2.imshow("imgen",template)
cv2.imshow("original",image_p)

print(template.shape)
print(image_p.shape)
x1= 100
y1= 100

for x in range (0,600,100):
    for y in range (0,400,100):
        roi=image_p[y:y+y1,x:x+x1]
        resta=cv2.absdiff(roi,template)
        t_pixel=np.sum(resta)
        print(t_pixel)
        base=original.copy()
        if t_pixel < 15000:#8000 10000 15000
            original[y:y+y1,x:x+x1]=original1[y:y+y1,x:x+x1]
            cv2.rectangle(original,(x,y),(x+x1,y+y1),(0,0,255),2)        
            original1[y:y+y1,x:x+x1]=(0,0,255)
        cv2.rectangle(base,(x,y),(x+x1,y+y1),(0,255,0),2)        
        cv2.imshow("original",base)
        cv2.imshow("seccion",roi)
        cv2.imshow("resta",resta)
        cv2.waitKey(0)
cv2.imshow("final",original)
cv2.waitKey(0)#indefinida mente queda esperando a q se aplaste una tecla
cv2.destroyAllWindows()
