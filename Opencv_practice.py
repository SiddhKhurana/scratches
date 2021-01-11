
import cv2  
import matplotlib.pyplot as plt
# path to input images are specified and   
# images are loaded with imread command  
image1 = cv2.imread('C:\\Users\\sony\\Pictures\\Screenshots\\Screenshot (50).png',cv2.IMREAD_COLOR)  
image2 = cv2.imread('C:\\Users\\sony\\Pictures\\Screenshots\\Screenshot (48).png',cv2.IMREAD_COLOR) 
  
# cv2.addWeighted is applied over the 
# image inputs with applied parameters 
image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0) 
  
half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5) 
bigger = cv2.resize(image, (1050, 1610)) 
  
stretch_near = cv2.resize(image, (780, 540),  
               interpolation = cv2.INTER_NEAREST) 
  
  
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
images =[image, half, bigger, stretch_near] 
count = 4
  
for i in range(count): 
    plt.subplot(2, 2, i + 1) 
    plt.title(Titles[i]) 
    plt.imshow(images[i]) 
  
#plt.show() 
n_image=cv2.subtract(image,image2)
cv2.imshow('Original',n_image)
cv2.imshow('added',image)
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  