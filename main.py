from enum import auto
from charset_normalizer import detect
import cv2
import mediapipe as mp
import time 
import hands_detector as detector
import numpy as np
import pyautogui


pyautogui.MINIMUM_DURATION = 0

#Settings screen
width_screen, height_screen =  pyautogui.size()

#Settings mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    model_complexity=0, 
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5,
    max_num_hands = 1)

def print_fps(image,current_time, prev_time):
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(image,f'FPS: {str(int(fps))}',(1,15),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
    return image, current_time

def main ():
    btn_pressed = False
    cap = cv2.VideoCapture(0)
    prev_time = time.time() #For FPS    

    with hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Error capturing camera image")
                break
            result = detector.hands_detector(hands,image)
            
            if result.multi_hand_landmarks:  
                image = detector.draw_hand_connections(image,result,mp_hands,mp_drawing)
                
                hand_detected = detector.get_hand(result,0)
                index_finger = detector.get_landmark(hand_detected,8)
            
                #mapeia para o tamanho da janela 
                coords_index_finger_window = tuple(np.multiply(np.array((index_finger[0],index_finger[1])) , [image.shape[1], image.shape[0]]).astype(int))
                #mapeia para o tamanho da tela
                coords_index_finger_screen = tuple(np.multiply(np.array((index_finger[0],index_finger[1])) , [width_screen, height_screen]).astype(int))
                cv2.circle(image,coords_index_finger_window,15,(0,0,255))
                pyautogui.moveTo(x = coords_index_finger_screen[0], y = coords_index_finger_screen[1])
                
                if(detector.linked_finger(hand_detected,4,11)[0] or detector.linked_finger(hand_detected,4,10)[0]):
                    cv2.putText(image,'Click',(1,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
                    pyautogui.click()
                else:
                    if(detector.linked_finger(hand_detected,8,4)[1]):
                        if not btn_pressed:
                            pyautogui.mouseDown();
                            cv2.putText(image,'Botao Segurado',(1,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
                            btn_pressed = True
                    else:
                        if btn_pressed:
                            pyautogui.mouseUp();
                            cv2.putText(image,'Botao Solto',(1,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)
                            btn_pressed = False
                #print(coords_index_finger)
                #print(detector.linked_finger(hand_detected,8,4))

            cv2.flip(image, 1)
            image, prev_time = print_fps(image,time.time(),prev_time)
            cv2.imshow('Capture',image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()

if __name__ == "__main__":
    main()