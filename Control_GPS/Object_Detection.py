import cv2

thres = 0.45  # Threshold to detect object

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)
# cap.set(4, 720)
# cap.set(10, 70)
classFile = 'coco.names'
classNames = open(classFile, 'rt').read().rsplit('\n')
# print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def detectar(img):
    imagen_final = img
    classIds, confs, bbox = net.detect(imagen_final, confThreshold=thres)
    #print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            name = classNames[classId - 1]
            print(name)
            if name == "potted plant":
                cv2.rectangle(imagen_final, box, color=(0, 255, 0), thickness=2)
                cv2.putText(imagen_final, classNames[classId - 1].upper(),
                            (box[0] + 10, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(imagen_final, str(round(confidence * 100, 2)),
                            (box[0] + 200, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return imagen_final
    return None
                #cv2.rectangle(imagen_final, box, color=(0, 255, 0), thickness=2)
                #cv2.putText(imagen_final, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                 #           cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                #cv2.putText(imagen_final, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                  #          cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                # cv2.imshow("Output", imagen_final)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()            
    #return imagen_final
    # cv2.imshow("Output", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
