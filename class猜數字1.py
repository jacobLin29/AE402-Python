# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:37:36 2019

@author: 林澤洋
"""
import random

print("歡迎來到猜數字~請在1~20之間猜一個數字~如果猜對電腦選的數字,就答對了喔~那答對可以幹嘛呢?不能幹嘛。")

answer = random.randint(1,20)

guess = input("1~20給我猜啦!!")
guess = int(guess)

if guess > answer:
    print("太大了啦!猜得準點好嗎?")
elif guess < answer:
    print("是要猜多小?不會大一點嗎?")
else :
    print("好ㄅ算你會猜")