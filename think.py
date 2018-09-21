#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import json

# 为了让think-python更接近think-node, 封装了一些ECMAScript的特性
from extend.symbol import Symbol
dirname = os.getcwd()

class Think:
  def __init__(self, option):
    # 常量设置
    self.END = Symbol('end')
    self.NODATA = Symbol('nodata')
    self.DIR = os.path.join(dirname)
    self.headerInfo = {}
    self.timeInfo = 'GMT'
    self.language = 'en'
    self.option = option
    self.loadList = []

  # 设置请求头  
  def header(self, headerName, headerValue):
    self.headerInfo[headerName] = headerValue

  # 设置时区
  def timeZone(self, info):
    self.timeInfo = info
  
  # 设置语言
  def lang(self, l):
    self.language = l

  def onload(self):
    for callback in self.loadList:
      callback()

  # 将函数添加到load列表
  def loadCallback(self, callback):
      self.loadList.append(callback)

  # 设置option, 失败返回false, 成功返回true
  # python版本对这里进行了优化加强
  def opt(self, key, value):
    keyPath = key.lower().split('_')
    optVal = self.option

    # 先获取最终key
    popPath = keyPath.pop()

    # 取到最终的路径, 且该对路径应该是一个对象
    for keyItme in keyPath:
        optVal = optVal[keyItme]
        # 如果结果为空, 自动创建
        if not optVal:
          optVal[keyItme] = {}
          optVal = optVal[keyItme]

    # 设置, 如果成功为true, 失败为false
    if isinstance(optVal, dict):
      optVal[popPath] = value
      return True
    else:
      return False

  def voidCallback():
    pass



# 载入JSON
with open(os.path.join(dirname, 'bin', 'defaultOption.json'), 'r') as files:
  option = json.load(files)
  think = Think(option)
