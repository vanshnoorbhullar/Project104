import cv2

img= cv2.imread('solar-system.jpg')
cv2.imshow('output',img) 
cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (40,600),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Venus",
            (60,900),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (80,1200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mars",
            (100,1500),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Jupiter",
            (120,1800),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (140,2100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Uranus",
            (160,2400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Neptune",
            (180,2700),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.imwrite('Solar_systemwithname.jpg',img)