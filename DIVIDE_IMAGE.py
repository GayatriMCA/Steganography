import cv2
def DIVIDE_PARTS(path):
    #img_1="C:/Users/user/PycharmProjects/Stegnography project using RGBSRI method/607.jpg"
    img=cv2.imread(path)
    #print(img.shape)
    height, width, channels = img.shape

    part_1=img[0:height-height//2,0:(width-width//2)-1]
    #print(part_1.shape)
    cv2.imwrite("part_1.jpg", part_1)

    part_2=img[0:height-height//2,(width-width//2)-1:width]
    #print(part_2.shape)
    cv2.imwrite("part_2.jpg", part_2)

    part_3=img[(height-height//2)-1:height,0:(width-width//2)-1]
    #print(part_3.shape)
    cv2.imwrite("part_3.jpg", part_3)

    part_4=img[(height-height//2)-1:height,(width-width//2)-1:width]
    #print(part_4.shape)
    cv2.imwrite("part_4.jpg", part_4)

    #cv2.imshow("part_1",part_1)
    #cv2.imshow("part_2",part_2)
    #cv2.imshow("part_3",part_3)
    #cv2.imshow("part_4",part_4)
    #cv2.waitKey(0)