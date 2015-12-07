__author__ = 'ccq18'
# !/usr/bin/python
# coding: utf8
import sys
import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)


IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


# ǰ��
def forward(tf):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


# ����
def reverse(tf):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(tf)
    GPIO.cleanup()


# ��ת��
def left(tf):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


# ��ת��
def right(tf):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


# ����ת��
def pivot_left(tf):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


# ����ת��
def pivot_right(tf):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(tf)
    GPIO.cleanup()


# ԭ����ת
def p_left(tf):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


# ԭ����ת
def p_right(tf):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(tf)
    GPIO.cleanup()


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
