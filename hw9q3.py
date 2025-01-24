from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science','no-latex','grid'])
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 20})
plt.rcParams["figure.figsize"] = (10,10)
plt.rcParams["axes.formatter.use_mathtext"] = True
plt.rcParams["axes.formatter.limits"] = [-2, 2]

def main():
    gamma = 10 # 1/s
    m = 1 # g
    omega = 2 # 1/s
    gamma_tag = np.sqrt(gamma**2 - 4*omega**2)
    start_time = 0
    end_time = 1
    times = np.linspace(start_time, end_time, 100)
    start_conditions = [
        (1,0),
        (1.2,0),
        (-1,0),
        (-1.2,0)
    ]
    colors = [
        'b',
        'r',
        'g',
        'y'
    ]
    
    for i,cond in enumerate(start_conditions):
        qs, ps = [], []
        q0, p0 = cond
        for t in times:
            A = (np.e**(-gamma*t/2)/(2*gamma_tag))*((gamma_tag+gamma)*np.e**(gamma_tag*t/2) + (gamma_tag-gamma)*np.e**(-gamma_tag*t/2))
            B = (np.e**(-gamma*t/2)/(m*gamma_tag))*(np.e**(gamma_tag*t/2) + np.e**(-gamma_tag*t/2))
            C = (np.e**(gamma*t/2)*(gamma_tag**2-gamma**2)/(4*gamma_tag))*m*(np.e**(gamma_tag*t/2) + np.e**(-gamma_tag*t/2))
            D = (np.e**(gamma*t/2)/(2*gamma_tag))*((gamma_tag+gamma)*np.e**(-gamma_tag*t/2) + (gamma_tag-gamma)*np.e**(gamma_tag*t/2))
            q = q0*A + p0*B
            p = q0*C + p0*D
            qs.append(q)
            ps.append(p)
        plt.plot(qs, ps, linestyle='-', color=colors[i], label=f'$q_0={cond[0]} [cm]$', linewidth=2)
    plt.xlabel("q(t) [cm/s]")
    plt.ylabel("p(t) [g cm/s]")
    legend = plt.legend(fancybox=False, edgecolor="black")
    legend.get_frame().set_linewidth(0.5)
    plt.show()
    

if __name__ == '__main__':
    main()