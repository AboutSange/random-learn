#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
今天想学什么？不要纠结，随机一下获取今日关键字吧

TODO:
    1.知识点的扩充
    2.一天可学多个知识点
    3.一个知识点可能需要多天学习
"""

import random
import json
import os
import codecs
import pprint
import sys
import time
import logging

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
LOG = logging.getLogger(__name__)

def print_coding():
    print '='*20
    print 'sys.getdefaultencoding():{}'.format(sys.getdefaultencoding())
    print 'sys.getfilesystemencoding():{}'.format(sys.getfilesystemencoding())
    print 'sys.stdout.encoding:{}'.format(sys.stdout.encoding)
    print 'sys.stdin.encoding:{}'.format(sys.stdin.encoding)
    print '='*20

def init_log():
    """
    1.初始化日志对象
    2.日志对象的基本设置(setLevel)
    3.初始化处理器并设置处理器(setLevel、setFormatter)
    4.将处理器加入日志对象
    """
    log_path = os.path.join(CURRENT_DIR, 'run.log')
    fm = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    LOG.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(fm)
    LOG.addHandler(file_handler)

    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.INFO)
    # console_handler.setFormatter(fm)
    # LOG.addHandler(console_handler)

def get_one_keyword():
    """
    获取今日学习关键字
    """
    json_file_path = os.path.join(CURRENT_DIR, 'technology_stack.json')
    technology_dict = {}
    knowledge_point_list = []

    with codecs.open(json_file_path, 'r', 'utf-8') as json_obj:
        technology_dict = json.load(json_obj)

    for value in technology_dict.values():
        knowledge_point_list.extend(value)

    keyword = random.choice(knowledge_point_list)
    LOG.info(keyword)
    print keyword.encode(sys.getfilesystemencoding())
    return keyword
    # random.shuffle(knowledge_point_list)  # 将列表随机
    # print json.dumps(knowledge_point_list, ensure_ascii=False, indent=4).encode(sys.getfilesystemencoding())  # 打印到窗口中（处理中文）

def main():
    init_log()
    # print_coding()
    keyword = get_one_keyword()

if __name__ == '__main__':
    main()