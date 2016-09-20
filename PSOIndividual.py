# -*- coding: utf-8 -*-
"""
Created on 20160919

@author: Veileno
"""
import numpy as np
import ObjFunction


class PSOIndividual(object):
    '''
    individual of PSO
    个体粒子
    '''

    def __init__(self, vardim, bound):
        '''
        vardim: dimension of variables 变量维度
        bound: boundaries of variables 变量范围
        '''
        self.vardim = vardim
        self.bound = bound
        self.fitness = 0.

    def generate(self):
        '''
        generate a random particle
        生成一个随机粒子
        '''
        len = self.vardim
        rnd = np.random.random(size=len)
        self.particle = np.zeros(len)
        self.velocity = np.random.random(size=len)
        for i in xrange(0, len):
            self.particle[i] = self.bound[0, i] + (self.bound[1, i] - self.bound[0, i]) * rnd[i]
        self.bestPosition = np.zeros(len)
        self.bestFitness = 0.

    def calculateFitness(self):
        '''
        calculate the fitness of the particle
        计算个体粒子的适应度
        '''
        y = ObjFunction.GrieFunc(self.vardim, self.particle, self.bound)
        # y = ObjFunction.RastFunc(self.vardim, self.particle, self.bound)
        # 将函数值转化成适应度值，范围为(0, 1],目标是max(fitness)
        self.fitness = 1. / (1. + y)
