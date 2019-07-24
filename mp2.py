import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return np.float32(np.sin(2*x*np.pi))
def g(x):
    return np.float32(np.absolute(x-.5))

def Lag(n,x,func):
    ret = []
    iterator = 0
    xk = np.arange(0, 1 + np.float32(1 / n), np.float32(1 / n))
    while iterator < len(x):
        sum = 0
        for k in xk:
            prod = np.float32(func(k))
            for i in xk:
                if(k != i):
                    prod = np.float32(prod*((x[iterator] - i)/(k-i)))
            sum = np.float32(sum + prod)
        ret.append(sum)
        iterator += 1
    return ret

def plot_pic_one(x):
    plt.plot(x, f(x))
    plt.plot(x, Lag(4, x, f))
    plt.plot(x, Lag(8, x, f))

def plot_pic_two(x):
    plt.plot(x,f(x))
    plt.plot(x,Lag(16,x,f))

def plot_pic_three(x):
    plt.plot(x,g(x))
    plt.plot(x,Lag(4,x,g))
    #plt.plot(x,Lag(8,x,g))

def plot_pic_four(x):
    plt.plot(x,g(x))
    plt.plot(x,Lag(16,x,g))

def main():
    x = np.arange(0, 1, 1 / 512)  # start,stop,step
    #plot_pic_one(x)
    #plot_pic_two(x) #uncomment to display pic two
    plot_pic_three(x) #uncomment to display pic three
    #plot_pic_four(x) #uncomment to display pic four
    plt.show()

if __name__ == "__main__":
    main()