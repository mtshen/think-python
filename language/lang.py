#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 这里是与国际化相关代码, 
# 根据用户设置的语言类型, 这里会加载相应的JSON
# 打印信息使用think.info('xxx');
# 如此可以方便的达到国际化效果
import os
import json
from think import think, dirname

THINK_LENG_PATH = os.path.join('%s.json' % think.language)
THINK_LENG_FILES_PATH = 'language'
lengInfo = ''

if not os.path.exists(os.path.join(dirname, THINK_LENG_FILES_PATH, THINK_LENG_PATH)):
    print('The loading language failed. The language file did not exist!')
    print(THINK_LENG_PATH)
    
    # 载入JSON
    with open(os.path.join(dirname, THINK_LENG_FILES_PATH, 'zh.json'), 'r') as files:
        lengInfo = json.load(files)
        print(lengInfo['loadLengN'])
else:
    # 如果找到了语言文件, 自动加载
    with open(os.path.join(dirname, THINK_LENG_FILES_PATH, THINK_LENG_PATH), 'r') as files:
        lengInfo = json.load(files)
        print(lengInfo['loadLeng'])
        print('   ' + THINK_LENG_PATH)
        print(lengInfo['loadLengY'])

def info(i):
    text = lengInfo[i]
    return text or ''

think.info = info