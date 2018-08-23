#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
technology_stack.txt  -->  technology_stack.json
"""

import codecs
import json
import os
import pprint

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

txt_file_path = os.path.join(CURRENT_DIR, 'technology_stack.txt')
json_file_path = os.path.join(CURRENT_DIR, 'technology_stack.json')

json_dict = {}

with codecs.open(txt_file_path, 'r', 'utf-8') as txt_obj:
    while True:
        line = txt_obj.readline()
        if line:
            line = line.strip()
            if line:
                line_split_list = line.split(':')
                key = line_split_list[0]
                values = line_split_list[1]
                values_split_list = values.split(u'、')
                json_dict[key] = values_split_list
        else:
            break
        
pprint.pprint(json_dict)

with codecs.open(json_file_path, 'w', 'utf-8') as json_obj:
    json.dump(json_dict, json_obj, ensure_ascii=False, indent=4)

print 'The end!'