import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','no-latex','grid'])
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 20})
plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams["axes.formatter.use_mathtext"] = True
plt.rcParams["axes.formatter.limits"] = [-2, 2]

m = 1
l = 1
g = 1

def propagate(theta_1, theta_2, p_1, p_2, dt):
    d_theta_1 = dt * ((p_1-p_2*np.cos(theta_1-theta_2))/(m*(l**2)*(1+(np.sin(theta_1-theta_2))**2)))
    d_theta_2 = dt * ((2*p_2-p_1*np.cos(theta_1-theta_2))/(m*(l**2)*(1+(np.sin(theta_1-theta_2))**2)))
    ps_main_part = ((p_1**2+2*(p_2**2)-2*p_1*p_2*np.cos(theta_1-theta_2))*np.sin(2*(theta_1-theta_2)))/(2*m*(l**2)*(1+np.sin(theta_1-theta_2)**2)**2)
    d_p_1 = dt * (ps_main_part - 2*m*g*l*np.sin(theta_1))
    d_p_2 = dt * (ps_main_part - m*g*l*np.sin(theta_2))    
    return theta_1 + d_theta_1, theta_2 + d_theta_2, p_1 + d_p_1, p_2 + d_p_2

def main():
    time = 10
    resolution = 0.01
    
    times = np.arange(0, time, resolution)
    points1 = [(0,0,0,0.7)]
    points2 = [(0.01,0,0,0.7)]
    points3 = [(0,0,0.5,1.9)]
    points4 = [(0.01,0,0.5,1.9)]
    points = [points1, points2, points3, points4]
    for time in times:
        for pointset in points:
            pointset.append(propagate(*pointset[-1], resolution))
    
    for pointset in points:
        theta_1, theta_2, p_1, p_2 = zip(*pointset)
        plt.plot(theta_1, theta_2, label=pointset[0])
    plt.xlabel("theta 1")
    plt.ylabel("theta 2")
    legend = plt.legend(fancybox=False, edgecolor="black")
    legend.get_frame().set_linewidth(0.5)
    plt.show()

if __name__ == '__main__':
    main()