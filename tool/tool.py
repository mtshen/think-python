#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re
# 移除了is, copy等方法, 这些方法python已经实现了
from think import think, dirname

#  装载内置函数
from tool.contentType import contentType, hasUtf8

# import {createFileSync, createFilesSync, createFile, createFiles} from './createfiles';
# import {stringifyForm, paramForm} from './form';
# import {Stak} from './stak';
# import {TestModel} from './random';
# const __ISMASTER: boolean = cluster.isMaster;
# __ISMASTER && console.log(think.info('loadTool'));

THINK_TOOL_URL = think.option.tool


think.tool = {
    "contentType": contentType,
    "hasUtf8": hasUtf8,
    # createFileSync, createFilesSync,
    # createFile, createFiles, Stak,
    # stringifyForm: stringifyForm.bind(think.tool),
    # paramForm: paramForm.bind(think.tool),
    # TestModel: TestModel,
}


# // 装载第三方函数, 同步装载
if os.path.exists(THINK_TOOL_URL):
    maindir, subdir, fileNameList in os.walk(THINK_TOOL_URL):
    for item in fileNameList:
        fileName = os.path.join(THINK_TOOL_URL, item)
        # if ()
        # 

#     stat.forEach((file: string) => {
#         // 得到文件
#         let 
#         let stats: fs.Stats = fs.statSync(fileName);
#         if (stats.isFile() && /^[.-_$\w]+\.js$/.test(fileName)) {
#             try {
#                 let toolCallback = require(fileName.slice(0, -3));
#                 think.tool[getFileName(fileName)] = toolCallback;
#                 __ISMASTER && console.log('   ' + (fileName as any).file);
#             } catch (error) {
#                 __ISMASTER && (think.log(fileName, error), console.log('   ' + (fileName as any).error));
#             }
#         }
#     });

# 将文件名转换为一个变量名
# 将.-去除, 并使首字母大写, 
# 如 a.min.js 转换为 aMin
# a-min.js 也转换为 aMin
# @param fileName 文件名称
def getFileName(fileName):
    fileNameList = re.split('[\.-]+', fileName.slice(0, -3))
    fileNameList = [item.capitalize() for item in fileNameList]
    return ''.join(fileNameList)