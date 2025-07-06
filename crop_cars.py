import os
import cv2

output_empty = 'clf-data/empty'
output_not_empty = 'clf-data/not_empty'
os.makedirs(output_empty, exist_ok=True)
os.makedirs(output_not_empty, exist_ok=True)
mask_path = r'mask_1920_1080.png'
mask = cv2.imread(mask_path, 0)

analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)

(num_labels, labels, stats, centroids) = analysis

slots = []

for i in range(1, num_labels):
    area = stats[i, cv2. CC_STAT_AREA]

    x1 = stats[i, cv2.CC_STAT_LEFT]
    y1 = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]

    pt1 = (x1, y1)
    pt2 = (x1 + w, y1 + h)
    (X, Y) = centroids[i]
    slots.append([x1, y1, w, h])

video_path = r'data/parking_1920_1080.mp4'

cap = cv2.VideoCapture(video_path)

frame_nmr = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
ret, frame = cap.read()

while ret:

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_nmr)
    ret, frame = cap.read()

    if ret:

        for slot_nmr, slot in enumerate(slots): # slot: [x, y, w, h]
            slot = frame[slot[1]: slot[1] + slot[3], slot[0]: slot[0] + slot[2], :]

            if slot_nmr in [132, 147, 164, 180, 344, 360, 377, 385, 341, 360, 179, 131, 106, 91, 61, 4, 89, 129, 161, 185, 201, 224, 271, 303, 319, 335, 351, 389, 29, 12, 32, 72, 281, 280, 157, 223, 26]:
                cv2.imwrite(os.path.join(output_empty, '{}_{}.jpg'.format(str(frame_nmr).zfill(8), str(slot_nmr).zfill(8))), slot)

            if slot_nmr in [3, 5, 7, 13, 14, 16, 17, 18, 28, 31, 41, 46, 55, 56, 65, 67, 76, 85, 105, 115, 116, 119, 120, 125, 127, 128, 142, 144, 145, 146, 148, 159, 160, 163, 175, 176, 178, 184, 187, 188, 199, 200, 221, 229, 232, 243, 253, 258, 270, 277, 278, 295, 312, 320, 327, 356, 358, 370, 378, 384, 391, 392]:
                cv2.imwrite(os.path.join(output_not_empty, '{}_{}.jpg'.format(str(frame_nmr).zfill(8), str(slot_nmr).zfill(8))), slot)

        frame_nmr += 10

cap.release()

