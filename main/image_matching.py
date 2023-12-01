import cv2
import numpy as np
from .models import FoundItem


def image_matcher(image_name):
    img1 = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)

    surf = cv2.SIFT_create()

    result=[]
    arr= FoundItem.objects.all()
    print('namaste')
    for i in arr:
        img2=cv2.imread(i.image.path,cv2.IMREAD_GRAYSCALE)
        kp1, des1 = surf.detectAndCompute(img1, None)
        kp2, des2 = surf.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)


        matches = bf.match(des1, des2)

    
        similarity_threshold = 28
        print(len(matches))


        is_same_object = len(matches) > similarity_threshold
        if is_same_object:
            result.append(i.id)

    return result
     


