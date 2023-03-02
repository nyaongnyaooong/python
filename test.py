import serial
import time
import pyautogui
import pywinauto
import math
import random


print('serial ' + serial.__version__)

import serial.tools.list_ports as sp

## PC 연결된 COM Port 정보를 list에 넣어 확인한다.
list = sp.comports()

devideName = 'Arduino Leonardo'
PORT = ''


for i in list:
  # if devideName in str(i)[7:-6]:

  if devideName in str(i):
    PORT = str(i)[0:4]
    # print(PORT)


# Set a PORT Number & baud rate

def request(string):
  BaudRate = 9600
  ARD = serial.Serial(PORT, BaudRate)
  return ARD.write(string.encode('utf-8'))

def Trans(string):
  return string.encode('utf-8')

def ranCoord(x1, y1, x2, y2):
  coord = []
  coord.append(math.floor(x1 + (x2 - x1) * random.random()))
  coord.append(math.floor(y1 + (y2 - y1) * random.random()))
  return coord

def mouseMove(coord, button):
  timeRange = random.random()
  distance = math.sqrt(coord[0] ** 2 + coord[1] ** 2)

  if (distance < 300):
    Coefficient = 0.3
  elif (distance < 500):
    Coefficient = 0.5
  else:
    Coefficient = 0.7

  if (timeRange < 0.9):
    movingTime = random.random()
  elif (timeRange < 0.95):
    movingTime = random.random() * 2
  else:
    movingTime = random.random() * 4
  
  pyautogui.moveTo(coord[0], coord[1], movingTime / 2 * Coefficient)
  pywinauto.mouse.click(button, coords = (coord[0], coord[1]))
  return 0



def delay(delayTime):
  timeRange = random.random()

  if (timeRange < 0.85):
    Coefficient = random.random() * 1.5
  elif (timeRange < 0.95):
    Coefficient = random.random() * 2
  else:
    Coefficient = random.random() * 3

  delayTime = (delayTime * Coefficient + 0.15) / 1000
  print(delayTime)
  return time.sleep(delayTime)

def moveAlgo(x1, y1, x2, y2):

  random.random()

  return 0
  # index = 0
  # arr = range(100)
  # finish = 2.5
  # add = finish / 100
  # v = 0
  # sum = 0

  # for i in arr:
  #   v = add * index
  #   arr[index] = v * math.cos(v - 1) + math.sin(v - 1) + 1
  #   index = index + 1
  #   sum += arr[index]

  # nowX = pyautogui.position().x
  # nowY = pyautogui.position().y
  # distanceX = x - nowX
  # distanceY = y - nowY

  # index = 0
  # for i in arr:
  #   moveX = nowX + distanceX / sum * arr[index]
  #   moveY = nowY + distanceY / sum * arr[index]
  #   pyautogui.moveTo(moveX, moveY)
  
  # # aa = x * math.cos(x - 1) + math.sin(x - 1) + 1
  # # pyautogui.moveTo(100, 500, duration=1.5)  # 1.5초 동안 100, 200 위치로 이동
  # # pyautogui.moveTo(x, y) 
  # return sum

# a = range(10)
# print(pyautogui.position().x)
# print(pyautogui.position().y)

# moveAlgo(100, 100)

def ranDouble():
  if (random.random() > 0.8):
    pyautogui.click()
    if(random.random() > 0.8):
      pyautogui.click()
      pyautogui.click()
      
  return 0





for i in range(8):


  for j in range(9):
    # 몹방출 우클릭
    mouseMove(ranCoord(66, 708, 112, 754), 'right')

    delay(0)

    # 방출클릭
    tempCoord = ranCoord(50, 601, 125, 621)
    tempCoord[0] = tempCoord[0] - 90 + pyautogui.position().x
    tempCoord[1] = tempCoord[1] - 738 + pyautogui.position().y
    mouseMove(tempCoord, 'left')
    ranDouble()
    
    delay(0)

    # 방출확인1
    mouseMove(ranCoord(485, 448, 500, 463), 'left')
    ranDouble()
    delay(0)

    # 방출확인2
    pyautogui.press('enter')
    delay(0)

  # 농장꾸미기 탭
  mouseMove(ranCoord(122, 669, 183, 680), 'left')
  delay(0)

  # 몬스터 까기
  for j in range(9):
    if (j == 0):
      mouseMove(ranCoord(106, 708, 151, 753), 'left')
      ranDouble()
    else:
      pyautogui.click()
      pyautogui.click()
      ranDouble()
      
    delay(0)
    pyautogui.press('enter')
    pyautogui.press('enter')
    delay(100)
    pyautogui.press('enter')
    time.sleep(0.15 + random.random() * 0.2)


  # 자동 돌보기
  mouseMove(ranCoord(20, 284, 118, 306), 'left')
  delay(0)
  pyautogui.press('enter')
  delay(100)

  # 내 몬스터 탭
  mouseMove(ranCoord(28, 669, 100, 680), 'left')
  delay(100)


# index = 0
# arr = range(100)
# finish = 0.75
# add = finish / 100
# v = 0
# sum = 0


# arr1=[]
# size = 3
# for i in range(size):
#   j = finish / size * i
#   fomula = j * math.cos(j) + math.sin(j) + 4 * math.sin(2 * j)
#   # fomula = (j * math.cos(j - 1) + math.sin(j - 1) + 1) * 
#   arr1.append(fomula)
#   sum = sum + fomula

# print(sum)
# nowX = pyautogui.position().x
# nowY = pyautogui.position().y
# distanceX = 100 - nowX
# distanceY = 100 - nowY

# sum2 = 0

# for i in arr1:
#   sum2 = sum2 + i
#   moveX = nowX + (distanceX / sum * sum2)
#   moveY = nowY + (distanceY / sum * sum2)
#   pyautogui.moveTo(moveX, moveY, 0.5)














# for i in arr1:
#   sum2 = sum2 + i
#   moveX = distanceX / sum * sum2
#   moveY = distanceY / sum * sum2
#   pyautogui.move(moveX, moveY, duration=0.1)




# size = pyautogui.size()  # 현재 화면의 스크린 사이즈(가로, 세로)를 가져옴
# print(size)  # Size(width=1920, height=1080) 
# # size[0] : width
# # size[1] : height

# # 절대 좌표로 마우스 이동
# pyautogui.moveTo(700, 200)  # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
# pyautogui.moveTo(100, 500, duration=1.5)  # 1.5초 동안 100, 200 위치로 이동

# # 상대 좌표로 마우스 이동(현재 커서가 있는 위치로부터) - move()
# pyautogui.moveTo(100, 100, duration=1.5)
# print(pyautogui.position())  # Point(x, y) 현재 위치
# pyautogui.move(100, 100, duration=1.5)  # 100, 100 기준으로부터 +100, +100으로 이동
# print(pyautogui.position())  # Point(x, y)
# pyautogui.move(100, 100, duration=1.5)  # 200, 200 기준으로부터 +100, +100으로 이동
# print(pyautogui.position())  # Point(x, y)

# p = pyautogui.position()
# print(p[0], p[1])  # x, y
# print(p.x, p.y)  # x, y 


# [결과]
# Size(width=1920, height=1080)
# Point(x=100, y=100)
# Point(x=200, y=200)
# Point(x=300, y=300)
# 300 300
# 300 300











 




# while (True):
#   
# 
# .write(Trans("1"))  # Q12345678 전송
#   time.sleep(0.5)
#   ARD.write(Trans("0"))  # Q12345678 전송
#   time.sleep(0.5)


