

import cv2
import numpy as np

image = cv2.imread("Bild1.jpeg", 1)

edge = cv2.Canny(image, 100,250)

contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

Konturen = cv2.drawContours(edge, contours, -1, 255)

color_img = image.copy()


for cnt in contours:
    
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    
    if radius > 5:
        cv2.circle(color_img, center, radius, (255, 0, 0), 1)

    if cv2.contourArea(cnt) <= 100:
        continue
    
    status_ok = True 

    (xc, yc), radius = cv2.minEnclosingCircle(cnt)

    for point in cnt:
        px, py = point[0]

        distanz = np.sqrt((px - xc)**2 + (py - yc)**2)

        if (radius - distanz) > 4.0:
            status_ok = False
            break  
            
    if status_ok == True:
        color = (0, 120, 0)
    else:
        color = (0, 0, 255)
        
    text = "OK" if status_ok else "FEHLER"

    center_point = (int(xc), int(yc))
    text_position = (int(xc) - 20, int(yc) - 10)
    
    cv2.circle(color_img, center_point, int(radius), color, 2)
    cv2.putText(color_img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                    
                    
    color = (0, 255, 0) if status_ok else (0, 0, 255)
    text = "OK" if status_ok else "FEHLER"
    
    (x,y), radius = cv2.minEnclosingCircle(cnt)
    center_point = (int(x), int(y))
    text_position = (int(x)-20, int(y)-10)
    
    cv2.circle(color_img, center_point, int(radius), color, 2)
    
    cv2.putText(color_img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 29)
    
    
cv2.imshow("Qualitätskontrolle", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









