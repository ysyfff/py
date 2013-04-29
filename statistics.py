#!usr/bin/evn python
#coding:utf8

# 1：自动统计本文件夹里面及其以下共有多少个文件
import os
_cur_path = os.getcwd()
f1 = os.listdir(_cur_path)
# print f1, len(f1)
# print _cur_path