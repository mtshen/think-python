#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 载入JSON
with open(('./contentType.json'), 'r') as files:
    CONTENTTYPE = json.load(files)

# 获取文件对应的contentType值
# @param {string} fileName 文件名或文件路径 
def contentType(fileName):
    for key in CONTENTTYPE:
        if key in fileName.endsWith:
            return CONTENTTYPE[key]
    return CONTENTTYPE['+type']


# 检查文件后缀, 是否该文件应该返回utf-8格式
def hasUtf8(fileName):
    return fileName in CONTENTTYPE['+utf8']