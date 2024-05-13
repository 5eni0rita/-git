from numpy import *
from matplotlib.pyplot import *
def lorentz(x,t,v):
    gamma = 1/(sqrt(1 - v**2))
    x1 = gamma*(x - v*t)
    t1 = gamma*(t - v*x)
    return x1,t1

def velocity(v,u):
    return (v+u) / (1 + v*u)

def inverse_lorentz(x,t,v):
    gamma = 1/(sqrt(1 - v**2))
    x1 = gamma*(x + v*t)
    t1 = gamma*(t + v*x)
    return x1,t1   
x = linspace(0,10,10)
t = linspace(0,10,10)
v = 0.1
u = 0.5
x_prime , t_prime = lorentz(x,t,v)
u_prime = velocity(v,u)
figure()
plot(x,zeros_like(x),color='black',label='K frame')
plot(zeros_like(t),t,color='black')
plot(x,u*x,color='green',label='Event with speed u')
plot(x,x,'--',color='red',label='light')
legend()
figure()
plot(x_prime,zeros_like(x_prime),color='blue')
plot(zeros_like(t_prime),t_prime,color='blue',label='K$^|$ frame')
plot(x_prime,u_prime*x_prime,color='green',label='Event')
plot(x_prime,x_prime,'--',color='red',label='light')
xlim(-0.5,10)
ylim(-0.5,10)
legend()
show()
x = linspace(0,10,10)
t = linspace(0,10,10)
v = 0.3
slope = arctan(v)
t_slope = pi/2 - slope
x_p , t_p = lorentz(x,t,v)
x1,x2 = 1,6
t1,t2 = 3,3
x1_prime , t1_prime = lorentz(x1,t1,v)
x2_prime , t2_prime = lorentz(x2,t2,v)
figure(figsize=(8,7))
plot(x,zeros_like(x),color='black')
plot(zeros_like(t),t,color='black',label='K frame')
x_prime = v*x
t_prime = tan(t_slope)*x
plot(x,x_prime,color='blue',label='K$^|$ frame')
plot(x,t_prime,color='blue')
plot([x1,x2],[t1,t2],'-o',color='green',label='Simultaneous event in K frame')
ylim(-0.2,10)
xlim(-0.2,10)
xticks([])
yticks([])
legend()
show()
x = linspace(0,10,10)
t = linspace(0,10,10)
v = 0.3
slope = arctan(v)
t_slope = pi/2 - slope
x_p , t_p = lorentz(x,t,v)
x1,x2 = 1,6
t1,t2 = 3,3
x1_prime , t1_prime = inverse_lorentz(x1,t1,v)
x2_prime , t2_prime = inverse_lorentz(x2,t2,v)
figure(figsize=(8,7))
plot(x,zeros_like(x),color='black',label='K frame')
plot(zeros_like(t),t,color='black')
x_prime = v*x
t_prime = tan(t_slope)*x
plot(x,x_prime,color='blue',label='K$^|$ frame')
plot(x,t_prime,color='blue')
plot([x1_prime,x2_prime],[t1_prime,t2_prime],'-o',color='green',label='Simultaneous event in K$^|$ frame')
ylim(-0.2,10)
xlim(-0.2,10)
xticks([])
yticks([])
legend()
show()
