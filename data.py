#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

file_name = "origin_eng.txt"
wirte_file = "eng_6.txt"

words = []
count = 1

with open(file_name, 'r') as f:
    for line in f:
        if count % 3 is 2:
            # print line
            words.append(line)
        count = count + 1
f.close()

count = 1
tmp = ""
with open(wirte_file, 'w') as fw:
    for word in words:
        word = word.strip('\n')
        tmp = tmp + word.ljust(20)
        if count % 6 is 0:
            print tmp
            fw.write(tmp + '\n')
            tmp = ""
        count = count + 1

fw.close()

