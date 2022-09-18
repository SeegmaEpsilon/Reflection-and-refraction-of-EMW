from math import radians, degrees, pi, asin, sin, cos, atan, tan
from matplotlib import ticker as ticker
from matplotlib import pyplot as plt

def plot_graphics_coef(n_1, n_2):
    x = [i+1 for i in range(90)]
    R_s = []
    R_p = []
    T_s = []
    T_p = []
    angle_of_full_refraction = []
    brw_angle = degrees(atan(n_2 / n_1))
    for i in range(len(x)):
        phi_rad = radians(x[i])
        try:
            theta = asin(sin(phi_rad) * n_1 / n_2)
        except ValueError:
            angle_of_full_refraction.append(degrees(phi_rad))
            theta = pi/2
        if ((theta == pi/2)):
            R_perpendicular = R_parallel = 1.0
            T_perpendicular = T_parallel = 0.0
        elif ((n_1 == n_2)):
            R_perpendicular = R_parallel = 0.0
            T_perpendicular = T_parallel = 1.0
        else:
            R_perpendicular = pow((sin(phi_rad - theta) / sin(phi_rad + theta)), 2)
            R_parallel = pow((tan(phi_rad - theta) / tan(phi_rad + theta)), 2)
            T_perpendicular = 1 - pow((sin(phi_rad - theta) / sin(phi_rad + theta)), 2)
            T_parallel = sin(2*phi_rad)*sin(2*theta)/pow((sin(phi_rad+theta)*cos(phi_rad-theta)),2)
        R_s.append(round(R_perpendicular, 5))
        R_p.append(round(R_parallel, 5))
        T_s.append(round(T_perpendicular, 5))
        T_p.append(round(T_parallel, 5))

    coef_otr = plt.figure(2)
    fig = coef_otr
    coef_otr.clf()
    coefax = coef_otr.subplots()
    coefax.set_title('Коэффициенты пропускания (T) и отражения (R)', fontsize=10)
    coefax.set_xlabel('Угол падения', fontsize=10)
    coefax.grid(which='major', linewidth=1)
    coefax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
    coefax.plot(x, R_s, c='blue', linestyle='--', label='R перпендикулярная', linewidth=2)
    coefax.plot(x, R_p, c='red', linestyle='--', label='R параллельная')
    coefax.plot(x, T_s, c='blue', label='T перпендикулярная', linewidth=2)
    coefax.plot(x, T_p, c='red', label='T параллельная')
    coefax.vlines(brw_angle, 0, 1, color = 'g', linestyle='--', linewidth=1, label='Угол Брюстера')
    coefax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    coefax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
    coefax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    coefax.tick_params(which='major', length=10, width=2)
    coefax.tick_params(which='minor', length=5, width=1)
    if (theta == pi/2):
        if (n_1 != n_2):
            coefax.arrow(angle_of_full_refraction[0], 0.5, 90-angle_of_full_refraction[0], 0,
                     width = 0.01, head_width = 0.02, head_length = 1)
            coefax.arrow(90, 0.5, -(90 - angle_of_full_refraction[0]), 0,
                     width=0.01, head_width=0.02, head_length=1)
            coefax.text(angle_of_full_refraction[0]+angle_of_full_refraction[0]/6, 0.55,
                    'Полное \nвнутреннее \nотражение', fontsize=10, fontweight=500)
    coefax.legend()
    return fig