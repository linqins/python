#!/bash/python

# 一元一次方程

import matplotlib.pyplot as plt
import numpy as np
'''
x0 = np.linspace(-2,2,5) #(从-1到1，50个点)
y0 = x0 *2
plt.figure(num=1,figsize=(10,5))
plt.plot(x0,y0)
#plt.show()

#一元二次方程
x = np.linspace(-1,1,50)
y1 = x ** 2
y2 = -x * x
plt.figure(num=2,figsize=(10,5))
plt.plot(x,y1)

plt.figure(num=2,figsize=(10,5))
plt.plot(x,y2)
#plt.show()


import matplotlib.pyplot as plt
import numpy as np

#在指定的位置标记 

x = np.linspace(-3,3,50)
y = 2*x + 1
 
plt.figure(num = 1,figsize =(8,5))
plt.plot(x,y)
 
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
 
#将底下的作为x轴
ax.xaxis.set_ticks_position('bottom')
#并且data，以y轴的数据为基本
ax.spines['bottom'].set_position(('data',0))
 
#将左边的作为y轴
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
 
print("-----方式一-----")
x0 = 1
y0 = 2*x0 + 1
plt.plot([x0,x0],[0,y0],'k--',linewidth = 2.5)
plt.scatter([x0],[y0],s = 50,color='b')
plt.annotate(r'$2x+1 = %s$'% y0,xy = (x0,y0),xycoords = 'data',
             xytext=(+30,-30),textcoords = 'offset points',fontsize = 16
             ,arrowprops = dict(arrowstyle='->',
                                connectionstyle="arc3,rad=.2"))

'''
#多图合并
plt.figure(figsize=(6,6))
ax1 = plt.subplot(2,3,1)
ax1.set_title("AX1 Title")
plt.plot([0,1],[0,5])

ax2 = plt.subplot(2,3,2)
plt.plot([0,1],[0,5])
ax2.set_title("AX2 Title")

ax3 = plt.subplot(2,3,3)
plt.plot([0,1],[0,5])
ax3.set_title("AX3 Title")

ax4 = plt.subplot(2,3,4)
plt.plot([0,1],[0,5])
ax4.set_title("AX4 Title")

ax5 = plt.subplot(2,3,5,facecolor="red")
plt.plot([0,1],[0,5])
ax5.set_title("AX5 Title")

ax6 = plt.subplot(2,3,6,facecolor="#A9A9A9")
plt.plot([0,1],[0,5])
ax6.set_title("AX 6 Title")

#画的是动图

from matplotlib import animation
 
fig,ax = plt.subplots()
 
x = np.arange(0,2*np.pi,0.01)
#因为这里返回的是一个列表，但是我们只想要第一个值
#所以这里需要加,号
line, = ax.plot(x,np.sin(x))
 
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))#updata the data
    return line,
 
def init():
    line.set_ydata(np.sin(x))
    return line,
 
 
# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency
#frames帧数
ani = animation.FuncAnimation(fig=fig, func=animate, frames=1000, init_func=init,
                              interval=2, blit=False)
 
plt.show()
plt.show()