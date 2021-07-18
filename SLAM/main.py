import cv2 as cv

ores = cv.imread('ores.jpg',cv.IMREAD_UNCHANGED)
lapis = cv.imread('lapis_ore.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(ores, lapis, cv.TM_CCOEFF_NORMED)
