# -*- coding:utf-8 -*-

a, da, b, db = map(str, raw_input().split())

pa = 0

pb = 0

for i in a:

    if i == da:

        pa = pa * 10 + int(da)

for i in b:

    if i == db:

        pb = pb * 10 + int(db)

print pa + pb
