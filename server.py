#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# server.py
from wsgiref.simple_server import make_server
# 载入think
from think import think
# 载入用户配置项
from option import option
# 载入webbrowser
import webbrowser
# 载入语言模块
import language.lang
# 载入tool模块
# import './tool/tool'
# 载入日志模块
# import './log/log'
# 载入jarvis
# import './socket/main'
# 载入路由
# import route from './route/route'

def createServerCallback(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
  return [body.encode('utf-8')]

def run():
  LOCAL_HREF = 'http://localhost:%s/' % option['port']
  print('\n     ___________\n    | S T A R T |\n    |thinkPython|\n     ***********')
  print('\n%s' % LOCAL_HREF)
  think.onload()
  webbrowser.open(LOCAL_HREF)

def createServer():
  run()
  httpd = make_server('', option['port'], createServerCallback)
  # 开始监听HTTP请求:
  httpd.serve_forever()

createServer()
