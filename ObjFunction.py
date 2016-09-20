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


def RoseFunc(vardim, x, bound):
    """
    Rosenbrock function
    此函数在x为2，3维时还能正确求解，4维及以上貌似不能求解
    :param vardim:
    :param x:
    :param bound:
    :return:
    """
    s = 0
    for i in range(vardim - 1):
        s = s + 100. * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    return s
