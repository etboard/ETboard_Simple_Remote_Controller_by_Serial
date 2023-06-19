# ******************************************************************************************
# FileName     : ETboard_Simple_Remote_Controller_by_Serial
# Description  : 이티보드를 시리얼 통신으로 원격에서 제어하기
# Author       :
# Created Date : 2023.06.16
# Reference    :
# Modified     : 2023.06.19 : SCS : To add comment
# ******************************************************************************************


# import
import time                             # 시간 모듈 가져오기
import serial                           # 시리얼 통신 모듈

# global variable
com_port = 'COM4'                       # 시리얼 포트 번호
ser = serial.Serial()                   # 시리얼 포트


# setup
def setup():
    global ser, com_port
    ser.baudrate = 115200               # 이티보드 시리얼 통신 속도 115,200
    ser.port = com_port                 # 시리얼 통신 포트 지정
    ser.open()                          # 시리얼 통신 포트 열기


# main
def loop():
    send_etboard()                      # 이티보드에 메시지 보내기
    time.sleep(1)                       # 1초 기다리기


# send_etboard
def send_etboard():                     
    msg = "3"                           # 메시지 파랑 LED 깜밖이라는 메시지 '3' 보내기
    result = bytes(msg + '\n', 'utf-8')
    ser.write(result)
    print('send ' + msg + ' to blink blue led')
    time.sleep(3)

    msg = "4"                           # 메시지 파랑 LED 깜밖이라는 메시지 '4' 보내기
    result = bytes(msg + '\n', 'utf-8')
    ser.write(result)
    print('send ' + msg + ' to blink green led')
    time.sleep(3)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================