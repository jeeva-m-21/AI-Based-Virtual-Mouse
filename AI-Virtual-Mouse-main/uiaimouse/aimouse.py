import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import os
import pyautogui
import keyboard
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize global variables
global  scrolling
global dragging, scroll_prev_y, zoom_prev_distance, stationary_start_time, prev_cloc, right_click_time
ai_mouse_enabled = True
sensitivity = 7
custom_shortcut_1 = "notepad.exe"
custom_shortcut_2 = "calc.exe"
dragging = False
scroll_prev_y = 0
zoom_prev_distance = 0
stationary_start_time = None
right_click_time = 0
prev_cloc = (0, 0)
stationary_threshold = 7  # pixels
scrolling = False


def toggle_ai_mouse():
    global ai_mouse_enabled
    ai_mouse_enabled = not ai_mouse_enabled


keyboard.add_hotkey("ctrl+alt+m", toggle_ai_mouse)

# AI Mouse Configuration
wCam, hCam = 640, 480
frameR = 100
pTime = 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

# Audio setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

while True:
    if not ai_mouse_enabled:
        continue

    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if len(lmList) != 0:
        fingers = detector.fingersUp()

        # Left Click &ṁṁ Drag (Thumb-Index Pinch)
        dist_thumb_index = detector.findDistance(4, 8, img)[0]
        if dist_thumb_index < 30:
            if not dragging:
                autopy.mouse.toggle(button=autopy.mouse.Button.LEFT, down=True)
                dragging = True
            x1, y1 = lmList[8][1:]
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            clocX = prev_cloc[0] + (x3 - prev_cloc[0]) / sensitivity
            clocY = prev_cloc[1] + (y3 - prev_cloc[1]) / sensitivity
            autopy.mouse.move(wScr - clocX, clocY)
            prev_cloc = (clocX, clocY)
        else:
            if dragging:
                autopy.mouse.toggle(button=autopy.mouse.Button.LEFT, down=False)
                dragging = False

        # Right Click (Index-Middle Pinch with Cooldown, only if not scrolling)
        
        dist_index_middle = detector.findDistance(8, 12, img)[0]
        if dist_index_middle < 30 and time.time() - right_click_time > 3 and not scrolling:
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
            right_click_time = time.time()

        # Cursor Movement (Index Finger Only)
        if not dragging and fingers[1] and not any(fingers[2:]):
            x1, y1 = lmList[8][1:]
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            clocX = prev_cloc[0] + (x3 - prev_cloc[0]) / sensitivity
            clocY = prev_cloc[1] + (y3 - prev_cloc[1]) / sensitivity
            autopy.mouse.move(wScr - clocX, clocY)
            
            # Stationary click detection
            current_pos = (clocX, clocY)
            distance = np.hypot(current_pos[0]-prev_cloc[0], current_pos[1]-prev_cloc[1])
            
            if distance < stationary_threshold:
                if stationary_start_time is None:
                    stationary_start_time = time.time()
                elif time.time() - stationary_start_time >= 3:
                    autopy.mouse.click()
                    stationary_start_time = None  # Reset after click
            else:
                stationary_start_time = None
            prev_cloc = (clocX, clocY)

        # Scrolling (Three Fingers Up)
        if fingers[1] and fingers[2] and fingers[3]:
            scrolling = True
            current_y = lmList[12][2]
            if scroll_prev_y:
                if current_y < scroll_prev_y - 15:
                    pyautogui.scroll(100)
                elif current_y > scroll_prev_y + 15:
                    pyautogui.scroll(-100)
            scroll_prev_y = current_y
        else:
            scrolling = False
            scroll_prev_y = 0

        # Zoom Control (Pinky Up + Thumb-Index Distance)
        if fingers[4]:
            current_dist = detector.findDistance(4, 8, img)[0]
            if zoom_prev_distance:
                if current_dist < zoom_prev_distance - 5:
                    pyautogui.hotkey('ctrl', '+')
                elif current_dist > zoom_prev_distance + 5:
                    pyautogui.hotkey('ctrl', '-')
            zoom_prev_distance = current_dist
        else:
            zoom_prev_distance = 0

    # Display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), 
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("AI Virtual Mouse", img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
