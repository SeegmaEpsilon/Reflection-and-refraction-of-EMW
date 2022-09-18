from math import radians, degrees, pi, asin, sin, cos
from matplotlib import ticker as ticker
from matplotlib import pyplot as plt
import numpy as np

def graphs_amplitude(n_1, n_2, E01, E02):
    x = [i+1 for i in range(90)]
    E_perpendicular = []
    E_parallel = []
    angle_of_full_refraction = []
    f_phi = []
    g_phi = []
    r_1 = []
    r_2 = []

    if E01 == 0:
        E01 = 0.00000001
    if E02 == 0:
        E02 = 0.00000001
    if ((E01 == 0) and (E02 == 0)):
        E01 = 0.00000001
        E02 = 0.00000001

    for i in range(len(x)):
        phi_rad = radians(x[i])
        try:
            theta = asin(sin(phi_rad) * n_1 / n_2)
        except ValueError:
            angle_of_full_refraction.append(degrees(phi_rad))
            theta = pi/2
        if (theta == pi/2):
            E1 = E01
            E2 = E02
        elif (n_1 == n_2):
            E1 = 0.00000001
            E2 = 0.00000001
        else:
            E1 = (n_1*cos(phi_rad)-n_2*cos(theta))/(n_1*cos(phi_rad)+n_2*cos(theta))*E01
            E2 = (n_2*cos(phi_rad)-n_1*cos(theta))/(n_2*cos(phi_rad)+n_1*cos(theta))*E02
        f_phi.append(E1/E01)
        g_phi.append(-E2/E02)
        r_1.append(abs(E1)/E01)
        r_2.append(abs(E2)/E02)
        E_perpendicular.append(round(E1, 5))
        E_parallel.append(round(E2, 5))

    Amplitudes = plt.figure(3)
    Amplitudes.clf()
    ax555 = Amplitudes.subplots()
    ax555.set_title('Амплитуды перпендикулярной и параллельной составляющих\n отраженной волны', fontsize=9)
    ax555.set_xlabel('Угол падения', fontsize=10)
    ax555.grid(which='major', linewidth=1)
    ax555.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
    ax555.plot(x, E_perpendicular, c='blue', label='E⊥', linewidth=2)
    ax555.plot(x, E_parallel, c='red', label='E∥')
    ax555.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax555.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax555.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax555.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax555.tick_params(which='major', length=10, width=2)
    ax555.tick_params(which='minor', length=5, width=1)
    if (theta == pi/2):
        if (n_1 != n_2):
            ax555.arrow(angle_of_full_refraction[0], (E01+E02)/2, 90-angle_of_full_refraction[0], 0,
                     width = 0.01, head_width = 0.02, head_length = 1)
            ax555.text(angle_of_full_refraction[0]+angle_of_full_refraction[0]/6, (E01+E02)/2,
                    'Полное \nвнутреннее \nотражение', fontsize=10, fontweight=500)
    ax555.legend()

    Relation = plt.figure(4)
    Relation.clf()
    ax1 = Relation.subplots()
    ax1.set_title('Отношение амплитуд отраженной и падающей волн', fontsize=10)
    ax1.set_xlabel('Угол падения', fontsize=10)
    ax1.grid(which='major', linewidth=1)
    ax1.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)

    if (E01 != 0.00000001 and E02 != 0.00000001):
        ax1.plot(x, f_phi, c='blue', label='E⊥_отр / E⊥_пад', linewidth=2)
        ax1.plot(x, g_phi, c='red', label='-E∥_отр / E∥_пад')
    if E01 == 0.00000001 and E02 != 0.00000001:
        ax1.plot(x, g_phi, c='red', label='-E∥_отр / E∥_пад')
    if E02 == 0.00000001 and E01 != 0.00000001:
        ax1.plot(x, f_phi, c='blue', label='E⊥_отр / E⊥_пад', linewidth=2)
    if ((E01 == 0.00000001) and (E02 == 0.00000001)):
        ax1.plot(0, 0)

    ax1.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax1.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax1.tick_params(which='major', length=10, width=2)
    ax1.tick_params(which='minor', length=5, width=1)
    if (theta == pi / 2):
        if (n_1 != n_2):
            ax1.arrow(angle_of_full_refraction[0], 0, 90 - angle_of_full_refraction[0], 0,
                     width=0.01, head_width=0.02, head_length=1)
            ax1.text(angle_of_full_refraction[0] + angle_of_full_refraction[0] / 6, 0,
                    'Полное \nвнутреннее \nотражение', fontsize=10, fontweight=500)
    ax1.legend()


    Absolute_relation = plt.figure(5)
    Absolute_relation.clf()
    ax2= Absolute_relation.subplots()
    ax2.set_title('Отношение абсолютных амплитуд\n отраженной и падающей волн', fontsize=9)
    ax2.set_xlabel('Угол падения', fontsize=10)
    ax2.grid(which='major', linewidth=1)
    ax2.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)

    # ax2.plot(x, r_1, c='blue', label='r⊥ = |E⊥_отр| / E⊥_пад', linewidth=2)
    # ax2.plot(x, r_2, c='red', label='r∥ = |E∥_отр| / E∥_пад')

    if (E01 != 0.00000001 and E02 != 0.00000001):
        ax2.plot(x, r_1, c='blue', label='r⊥ = |E⊥_отр| / E⊥_пад', linewidth=2)
        ax2.plot(x, r_2, c='red', label='r∥ = |E∥_отр| / E∥_пад')
    if E01 == 0.00000001 and E02 != 0.00000001:
        ax2.plot(x, r_2, c='red', label='r∥ = |E∥_отр| / E∥_пад')
    if E02 == 0.00000001 and E01 != 0.00000001:
        ax2.plot(x, r_1, c='blue', label='r⊥ = |E⊥_отр| / E⊥_пад', linewidth=2)
    if ((E01 == 0.00000001) and (E02 == 0.00000001)):
        ax2.plot(0, 0)

    ax2.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax2.yaxis.set_minor_locator(ticker.AutoMinorLocator())
    ax2.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    ax2.tick_params(which='major', length=10, width=2)
    ax2.tick_params(which='minor', length=5, width=1)
    if (theta == pi / 2):
        if (n_1 != n_2):
            ax2.arrow(angle_of_full_refraction[0], 0, 90 - angle_of_full_refraction[0], 0,
                      width=0.01, head_width=0.02, head_length=1)
            ax2.text(angle_of_full_refraction[0] + angle_of_full_refraction[0] / 6, 0,
                     'Полное \nвнутреннее \nотражение', fontsize=10, fontweight=500)

    ax2.legend()
    return Amplitudes, Relation, Absolute_relation

def ellipse_lucha(phi, n_1, n_2, E01, E02):
    phi_rad = radians(phi)
    try:
        theta = asin(sin(phi_rad)*n_1/n_2)
    except ValueError:
        theta = pi/2
    if phi == 0:
        x = E02
        y = E01
    elif (theta == pi/2):
        y = 0
        x = 0
    else:
        y = 2 * cos(phi_rad) * sin(theta) / sin(phi_rad + theta) * E01
        x = 2 * cos(phi_rad) * sin(theta) / sin(phi_rad + theta) / cos(phi_rad - theta) * E02
    t = np.linspace(0, 2 * pi, 100)
    Ellipsis_graph = plt.figure(6)
    Ellipsis_graph.clf()
    axEL = Ellipsis_graph.subplots()
    axEL.set_title('Поперечное сечение преломленного луча', fontsize=10)
    axEL.plot( x*np.cos(t) , y*np.sin(t))
    plt.xlim(-x-5, x+5)
    plt.ylim(-y-5, y+5)
    axEL.grid(linestyle='--', color='lightgray')
    axEL.fill(x*np.cos(t), y*np.sin(t), facecolor='blue', alpha=0.1)
    plt.gca().set_aspect('equal')
    # axEL.get_xaxis().set_ticklabels([])
    # axEL.get_yaxis().set_ticklabels([])

    return Ellipsis_graph





