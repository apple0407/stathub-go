#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
/*
 * A smart Hub for holding server stat
 * https://www.likexian.com/
 *
 * Copyright 2015-2019, Li Kexian
 * Released under the Apache License, Version 2.0
 *
 */
'''


import os
import re


def read_file(fname):
    fp = open(fname, 'r')
    text = fp.read()
    fp.close()
    return text


def write_file(fname, text):
    fp = open(fname, 'w')
    fp.write(text)
    fp.close()


build = os.popen("git rev-parse --short HEAD").read().strip()

template = '''/*
 * A smart Hub for holding server stat
 * https://www.likexian.com/
 *
 * Copyright 2015-2019, Li Kexian
 * Released under the Apache License, Version 2.0
 *
 */

package main

// variable for tpl file
var (
\tTPL_REVHEAD  = "%s"
\tTPL_CERT     = map[string]string{}
\tTPL_STATIC   = map[string]string{}
\tTPL_TEMPLATE = map[string]string{}
)

func init() {''' % (build)


mapper = {'cert': 'TPL_CERT', 'static': 'TPL_STATIC', 'template': 'TPL_TEMPLATE'}
for i in mapper:
    for j in os.listdir(i):
        f = '%s/%s' % (i, j)
        t = read_file(f)
        template += '\n%s%s["%s"] = `%s`\n' % ("\t", mapper[i], j, t)

template += '\n}\n'
write_file('template.go', template)
