from E2E_sense_test import *
import time

roomT = 23.4
roomH = 34.5
cribM = 1.23
fixedData = [roomT, roomH, cribM]

uploadData(roomT, roomH, cribM)
time.sleep(5)
readData = readLast()

comparison(fixedData, readData)
