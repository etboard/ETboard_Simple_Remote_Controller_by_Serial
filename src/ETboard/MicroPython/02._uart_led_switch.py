# ******************************************************************************************
# FileName     : 02._uart_led_switch.py
# Description  : 시리얼 통신으로 '3', '4' 문자를 받으면 파랑 또는 녹색 LED를 깜밖임
# Author       : 손철수
# Created Date : 2023.06.16
# Reference    : 주의1. pyserial 모듈을 import 해야 함
# Reference    : 주의2. 코딩한 후에 PC와 USB 시리얼 통신을 위하여
#                       Thonny가 시리얼 통신 포트 disconnect
# Reference    : 주의3. ETboard의 reset 버튼을 눌러야 Thonny가 다시 ETboard를 connect 함
# Modified     : 
# ******************************************************************************************

# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
from machine import UART

# global variable
led_red = Pin(D2)                     # 빨강 LED 핀 지정 / heart beat
led_blue = Pin(D3)                    # 파랑 LED 핀 지정 
led_green = Pin(D4)                   # 초록 LED 핀 지정
led_yellow = Pin(D5)                  # 노랑 LED 핀 지정 / 메시지 수신 타임아웃
uart = UART(1)                        # 시리얼 통신 포트 지정 

# setup
def setup():    
    led_red.init(Pin.OUT)             # 빨강 LED를 출력모드 설정
    led_blue.init(Pin.OUT)            # 파강 LED를 출력모드 설정
    led_green.init(Pin.OUT)           # 초록 LED를 출력모드 설정
    led_yellow.init(Pin.OUT)          # 노랑 LED를 출력모드 설정
    uart.init(baudrate=115200,        # 시리얼 통신 속도 지정
              timeout=1000,           # 최대 1초만 수신 대기
              tx=1, rx=3)             # 이티보드 통신 핀 번호 지정


# main loop
def loop():
    led_red.value(HIGH)               # 빨강 LED 켜기
    time.sleep(0.5)                   # 0.5초 기다리기
    
    receive()    

    led_red.value(LOW)                # 빨강 LED 끄기
    time.sleep(0.5)                   # 0.5초 기다리기

# receive
def receive():    
    msg = uart.readline()             # 메시지를 1줄씩 읽음
    if msg is None:                   # 어떤 메시지도 받지 못하면
        led_yellow.value(HIGH)        # 노랑 LED 깜밖임
        time.sleep(0.5)      
        led_yellow.value(LOW)      
        time.sleep(0.5)      
        return
    
    cmd = msg.rstrip()                # 받은 메시지 끝에 \n 제거
    cmd = int(cmd)                    # 문자형을 숫자로 변경
    
    if (cmd == 3):                    # 3이면 파랑 LED 깜밖임
      led_blue.value(HIGH)
      time.sleep(1)      
      led_blue.value(LOW)      
      time.sleep(1)
    elif (cmd == 4):                   # 4면 녹색 LED 깜밖임
      led_green.value(HIGH)
      time.sleep(1)      
      led_green.value(LOW)      
      time.sleep(1)

if __name__ == "__main__":
    setup()
    while True:
        loop()
        
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================  