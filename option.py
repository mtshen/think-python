#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# dirname 是程序目录的位置, 可以根据这个路径设置绝对路径
from think import think, dirname

# 设置时区, 非必填
think.timeZone('GMT')

# 设置请求头, 这里的请求头会在所有接口中加入, 非必填
# 一般不需要设置, 每个文件的请求头都会被自动设置
think.header("Content-Type", 'text/html; charset=utf-8')

# 跨域解决方案
think.header("Access-Control-Allow-Origin", "*")
think.header("Access-Control-Allow-Headers", "X-Requested-With")
think.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS")

# 设置国际化, 默认为zh, 需要配合 think.info 使用, 非必填
think.lang('en')

# 设置您的项目目录, 这个目录中的文件会自动加入路由
# 这里必须设置为一个绝对路径
think.opt('path', '')

# 设置端口号, 默认80, 非必填
think.opt('port', 8088)

# 设置首页, 这里首页位置相对于设置的path, 非必填, 默认index.html
think.opt('default', 'index.html')

# 路由过滤, 考虑到项目中某些文件不希望公开, 则可以在这里设置, 默认为 **/*.*
# 通过设置的过滤文件才能够被访问, 可以设置多个过滤, 非必填
think.opt('staticresource', '**/*.*')

# 设置日志存放路径, 必须是绝对路径
# 记录日志是非常必要的, 日志中会记录大部分异常
think.opt('log_path', '')

# 设置接口地址, 必须是绝对路径
# 理论上该项是必填项, 因为如果不设置接口, 则没有了创建服务器的必要
think.opt('user_path', '')

# 如果你不希望记录日志, 可以设置日志开关, 默认是开启的
think.opt('log_switch', True)

# 如果你希望使用https服务, 可以配置如下指令
think.opt('https_switch', False)

# 此外除了需要手动开启http外还需要配置2个必填的参数
# 服务器私钥
think.opt('https_key', 'server-key.pem')

# 服务器证书
think.opt('https_cert', 'server-cert.pem')

# 还可以设置https端口, 默认443
think.opt('https_port', 443)

# 设置二级域名
# 当访问该项目时, 可以限制访问的域名
think.opt('host', '')

# 如果你希望快速建立一个多级域名的应用, 可以使用启用以下模式, 默认不开启
# 开启后设置的path将作为顶级域, 其中的文件夹将作为二级域名, 文件夹中还可以有文件夹, 做到多级域名
# 每个文件夹作为域, 每个域中都必须额外配置option.js
think.opt('offsprdomain', True)

# 如果你想要在think.tool中追加函数, 可以设置你的tool文件夹, 文件夹内的JS文件只能用.-_及数字字母命名
# 必须是绝对路径
think.opt('tool', '')

# 如果你是测试环境, 可以设置debugger为true, 如此, 当你的文件内容更变后, 不需要重启服务, 即可测试
think.opt('debugger', True)

option = think.option