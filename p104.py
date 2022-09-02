import cv2
img = cv2.imread("solar-system.jpg")

sun = img[120:360,400:500]

text_to_show1 = "Sun"
text_to_show2 = "Mercury"
text_to_show3 = "Venus"
text_to_show4 = "Earth"
text_to_show5 = "Mars"
text_to_show6 = "Jupiter"
text_to_show7 = "Saturn"
text_to_show8 = "Uranus"
text_to_show9 = "Neptune"


cv2.putText(img,  
           text_to_show1,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           text_to_show2,
           (120, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,0,255)
           )  
cv2.putText(img,  
           text_to_show3,
           (190, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,255,255)
           )                      
cv2.putText(img,  
           text_to_show4,
           (295, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,0)
           )  
cv2.putText(img,  
           text_to_show5,
           (410, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,200,255)
           )  
cv2.putText(img,  
           text_to_show6,
           (550, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(70,255,255)
           )  
cv2.putText(img,  
           text_to_show7,
           (610, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,100,255)
           )  
cv2.putText(img,  
           text_to_show8,
           (690, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,250)
           )  
cv2.putText(img,  
           text_to_show9,
           (730, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(112,255,255)
           )             
cv2.imshow("output",img)

cv2.waitKey(0)