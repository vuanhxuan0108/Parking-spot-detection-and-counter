import cv2
import pickle
import numpy as np

def get_parking_spots_bboxes(connected_components):
    (num_labels, labels, stats, centroids) = connected_components
    
    slots = []
    coef = 1

    for i in range (1, num_labels):

        x1 = int(stats[i, cv2.CC_STAT_LEFT] * coef)
        y1 = int(stats[i, cv2.CC_STAT_TOP] * coef)
        w = int(stats[i, cv2.CC_STAT_WIDTH] * coef)
        h = int(stats[i, cv2.CC_STAT_HEIGHT] * coef)

        slots.append([x1, y1, w, h])

    return slots


EMPTY = True
NOT_EMPTY = False

with open('model/model.p', 'rb') as f:
    MODEL = pickle.load(f) # mô hình ML



def empty_or_not(spot_bgr): # Đầu vào là ảnh vùng đỗ xe
    flat_data = []

    img_resized = cv2.resize(spot_bgr, (15, 15))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)

    if y_output == 0:
        return EMPTY
    else:
        return NOT_EMPTY
