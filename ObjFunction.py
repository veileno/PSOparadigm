# -*- coding: utf-8 -*-
"""
Created on 20160919

@author: Veileno
"""
import math


def GrieFunc(vardim, x, bound):
    """
    Griewank function
    """
    s1 = 0.
    s2 = 1.
    for i in range(vardim):
        s1 = s1 + x[i] ** 2
        s2 = s2 * math.cos(x[i] / math.sqrt(i + 1))
    y = (1. / 4000.) * s1 - s2 + 1
    return y


def RastFunc(vardim, x, bound):
    """
    Rastrigin function
    """
    s = 10 * 25
    for i in range(vardim):
        s = s + x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return s
