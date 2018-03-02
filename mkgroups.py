#!/usr/bin/env python

from __future__ import print_function
import re
import os

groups = {}
for root, dirs, files in os.walk("."):
    if 'items.txt' in files and len(dirs) == 0:
        root = re.sub(r'^\.\/', '', root)
        groupname = '`'.join(root.split('/'))
        if 'groupname' not in groups:
            groups[groupname] = {}
        groups[groupname] = open(root+'/items.txt', 'r').read()

groupstrings = ['group:{0},{1}'.format(group, items) for group, items in groups.items()]
print(','.join(groupstrings))
