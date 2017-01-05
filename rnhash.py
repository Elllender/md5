# /usr/bin/python
# -*- coding:utf-8 -*-

from random import randint
import hashlib
mas = []
x = 0
while x < 100:
 rand = randint(0,2000000)
 if rand not in mas:
   texth = hashlib.md5(str(rand)).hexdigest()
   f = open('hash.txt','a')
   f.write(str(texth)+'\n')
   mas.append(rand)
   x += 1
f.close()
