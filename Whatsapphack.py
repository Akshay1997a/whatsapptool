from selenium import webdriver
from pygame import mixer
import sys
import os
import time

TEXT_BOX = '_3u328'
STATUS = '_315-i'
SEND_BUT = '_3M-N-'


class WhatsappHack:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://web.whatsapp.com/')

    def msgBomb(self):
        try:
            print('Click on user to send message bomb')
            msg = input('Enter message :: ')
            count = int(input('Enter number of message to send ::'))
            while (count):
                msg_box = self.driver.find_element_by_class_name(TEXT_BOX).send_keys(msg)
                send_button = self.driver.find_element_by_class_name(SEND_BUT).click()
                time.sleep(0.5)
                count -= 1
        except:
            print('error')

    def checkStatus():
        while True:
            try:
                status = driver.find_element_by_class_name(
                    '_315-i').get_attribute('title')
                usr = driver.find_element_by_class_name(
                    '_19RFN').get_attribute('title')

                if status == 'online':
                    time.sleep(0.5)
                    if flag == 0:
                        alert.play()
                        flag = 1
                else:
                    flag = 0
                    alert.stop()
            except:
                status = None
                flag = 0
                alert.stop()


wh = WhatsappHack()
print()
print('.......................Whatsapp Hack tool.........................')
print('1 - whatsapp message bombing')
print('2 - Whatsapp check online status')
print('3 - exit')
x = int(input('Enter feedback :: '))
if x == 1:
    wh.msgBomb()
elif x == 2:
    wh.checkStatus()
else:
    exit
