#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(10,20):
    print 'num is : ================== ', num, '  start'

    for i in range(2,num):
        #print 'i is: ', i
        if num%i==0:
            j = num/i
            print '%d 等于%d * %d' % (num,i,j)
            break

    else:
        print num, '是一个质数'

    print 'num is : ================== ', num, '  stop '
    print '\n'
    print "test"



