import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)

fig = plt.figure(figsize=(5,5))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
l1, = ax1.plot(x, x*x, 'r')             #这里关键哦
l2,= ax2.plot(x, x*x, 'b')           # 注意

plt.legend([l1, l2], ['$first(x)$', '$second(x)$'], loc = 'upper right')             #其中，loc表示位置的；
#plt.show()

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(10,5))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()