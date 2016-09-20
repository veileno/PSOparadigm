# -*- coding: utf-8 -*-
"""
Created on 20160919

@author: Veileno
"""
import numpy as np
from PSOIndividual import PSOIndividual
import copy
import matplotlib.pyplot as plt


class PSO(object):
    '''
    the class for Particle Swarm Optimization
    粒子群类
    '''

    def __init__(self, sizepop, vardim, bound, MAXGEN, params):
        '''
        sizepop: population sizepop 粒子个数
        vardim: dimension of variables 变量维度
        bound: boundaries of variables 变量边界
        MAXGEN: termination condition 最大迭代次数
        params: algorithm required parameters, it is a list which is consisting of[w, c1, c2] 惯性权重和学习因子
        '''
        self.sizepop = sizepop
        self.vardim = vardim
        self.bound = bound
        self.MAXGEN = MAXGEN
        self.params = params
        self.population = []
        self.fitness = np.zeros((self.sizepop, 1))
        self.trace = np.zeros((self.MAXGEN, 2))

    def initialize(self):
        '''
        initialize the population of pso
        PSO种群初始化
        '''
        for i in xrange(0, self.sizepop):
            ind = PSOIndividual(self.vardim, self.bound)
            ind.generate()
            self.population.append(ind)

    def evaluation(self):
        '''
        evaluation the fitness of the population
        评价适应度
        '''
        for i in xrange(0, self.sizepop):
            self.population[i].calculateFitness()
            self.fitness[i] = self.population[i].fitness
            if self.population[i].fitness > self.population[i].bestFitness:
                self.population[i].bestFitness = self.population[i].fitness
                # self.population[i].bestIndex = copy.deepcopy(self.population[i].particle)

    def update(self):
        '''
        update the population of pso
        更新PSO种群
        '''
        for i in xrange(0, self.sizepop):
            self.population[i].velocity = self.params[0] * self.population[i].velocity + \
                                          self.params[1] * np.random.random(self.vardim) * (
                                              self.population[i].bestPosition - self.population[i].particle) + \
                                          self.params[2] * np.random.random(self.vardim) * (
                                              self.gbest.particle - self.population[i].particle)
            self.population[i].particle = self.population[i].particle + self.population[i].velocity

    def solve(self):
        '''
        the evolution process of the pso algorithm
        PSO进化过程
        '''
        self.t = 0
        self.initialize()  # 初始化粒子群
        self.evaluation()  # 第一次评估
        bestIndex = np.argmax(self.fitness)  # argmax!!!!找出当前适应度最大的个体的索引
        self.gbest = copy.deepcopy(self.population[bestIndex])  # 深度拷贝最优粒子个体
        self.avefitness = np.mean(self.fitness)  # 平均适应度
        # self.trace[self.t, 0] = self.gbest.fitness
        # self.trace[self.t, 1] = self.avefitness
        self.trace[self.t, 0] = (1 - self.gbest.fitness) / self.gbest.fitness
        self.trace[self.t, 1] = (1 - self.avefitness) / self.avefitness
        print "Generation %d: optimal function value is: %f; average function value is %f" % \
              (self.t, self.trace[self.t, 0], self.trace[self.t, 1])
        while self.t < self.MAXGEN - 1:
            self.t += 1
            self.update()
            self.evaluation()
            bestIndex = np.argmax(self.fitness)
            if np.max(self.fitness) > self.gbest.fitness:
                self.gbest = copy.deepcopy(self.population[bestIndex])
            self.avefitness = np.mean(self.fitness)
            # self.trace[self.t, 0] = self.gbest.fitness
            # self.trace[self.t, 1] = self.avefitness
            self.trace[self.t, 0] = (1 - self.gbest.fitness) / self.gbest.fitness
            self.trace[self.t, 1] = (1 - self.avefitness) / self.avefitness
            print "Generation %d: optimal function value is: %f; average function value is %f" % \
                  (self.t, self.trace[self.t, 0], self.trace[self.t, 1])
        print "Optimal function value is: %f; " % self.trace[self.t, 0]
        print "Optimal solution is:"
        print self.gbest.particle
        self.printResult()

    def printResult(self):
        '''
        plot the result of pso algorithm
        绘制PSO迭代过程结果
        '''
        x = np.arange(0, self.MAXGEN)
        y1 = self.trace[:, 0]
        y2 = self.trace[:, 1]
        plt.plot(x, y1, 'r', label='optimal value')
        plt.plot(x, y2, 'g', label='average value')
        plt.xlabel("Iteration")
        plt.ylabel("function value")
        plt.title("Particle Swarm Optimization algorithm for function optimization")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    bound = np.tile([[-400], [400]], 30)
    pso = PSO(60, 30, bound, 300, [0.6298, 1.4962, 1.4962])
    pso.solve()
