# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:52:44 2015

@author: hyde    
"""

import numpy as np
import time 

compare_times = 0

def gen_list(length):
    return np.random.randint(0, 100000000, length)

def check(s, _n, _max):
    global compare_times
    _len = 0
    for i in xrange(_n, _max-1):
        compare_times += 1
        if array[i+1] > array[i]:
            _len += 1
        else:
            break
    return _len
    
def find_out(s):
    global compare_times
    v = np.zeros(array.shape, dtype=np.int32)
    _max = 0
    _n = 0
    while _max + _n + 1 < len(s):
        compare_times += 1
        if v[_n] == 0:
            v[_n] = 1
            if s[_n+1] > s[_n] and s[_n + _max + 1] > s[_n + _max]:
                _len = check(s, _n, _max)
                if _len == _max:
                    _max += 1
                else:
                    _n += _len
            else:
                _n += 1
        else:
            if s[_n + _max + 1] > s[_n + _max]:
                _max += 1
            else:
                _n += _max + 1 
    return _max + 1 
                
if __name__ == '__main__':
    array = gen_list(100000000)#np.array([1, 2, 3, 4, 7, 2, 1, 9, 10, 12, 18, 20, 2])
    t = time.time()
    num = find_out(array)
    print 'result = %d | (%d,  %d) | Done in %.3f sec' %(num, compare_times, len(array), time.time() - t)