#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

file_name = "origin_eng.txt"
wirte_file = "eng_6.txt"

cet_file = "cet.txt"
wirte_file2 = "eng_all.txt"

words = []
count = 1

# with open(file_name, 'r') as f:
#     for line in f:
#         if count % 3 is 2:
#             # print line
#             words.append(line)
#         count = count + 1
# f.close()
#
# count = 1
# tmp = ""
# with open(wirte_file, 'w') as fw:
#     for word in words:
#         word = word.strip('\n')
#         tmp = tmp + word.ljust(20)
#         if count % 6 is 0:
#             print tmp
#             fw.write(tmp + '\n')
#             tmp = ""
#         count = count + 1
#
# fw.close()
# count = 1
# with open(wirte_file2, 'w') as f:
#     with open(cet_file, 'r') as fi:
#         for line in fi:
#             count = count + 1
#             if count < 3666:
#                 line = line.split(" ")[0]
#                 f.write(line + '\n')
#             else:
#                 line = line.split("         ")[0].lstrip()
#                 f.write(line + '\n')
#
#     fi.close()
# f.close()

# eng_defor_file = "eng_defor.txt"
# write_defor_file = "eng_defor_op.txt"
#
# with open(write_defor_file, 'w') as f:
#     with open(eng_defor_file, 'r') as fi:
#         for line in fi:
#             line = line.strip()
#             if len(line) is not 0:
#                 line = line.lstrip()
#                 f.write(line + '\n')
#
#     fi.close()
# f.close()

pinyin_file = "pinyin.txt"
out_file = "pinyin_op.txt"

with open(out_file, 'w') as f:
    with open(pinyin_file, 'r') as fi:
        for line in fi:
            line = line.strip()
            if len(line) is not 0:
                jihe = line.split(" ")
                for i in jihe:
                    f.write(i + '\n')
    fi.close()
f.close()




