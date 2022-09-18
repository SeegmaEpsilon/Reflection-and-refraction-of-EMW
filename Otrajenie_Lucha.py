from math import radians, pi, asin, sin, cos
from matplotlib import pyplot as plt
from matplotlib import patches as patches

def refraction_reflection_graph(n_1, n_2, phi):
    arrow_length = 50
    phi_rad = radians(phi)
    try:
        theta = asin(sin(phi_rad)*n_1/n_2)
    except ValueError:
        theta = pi/2
    x_pad = -sin(phi_rad) * arrow_length
    y_pad = cos(phi_rad) * arrow_length
    x_otr = sin(phi_rad) * arrow_length
    x_prelom = sin(theta)*arrow_length
    y_prelom = -cos(theta)*arrow_length

    otraj_prel = plt.figure(1)
    fig = otraj_prel
    otraj_prel.clf()
    ax5 = otraj_prel.subplots()

    ax5.arrow(x_pad, y_pad, -x_pad, -y_pad,  label='Падающий луч', width=0.5, color='blue',head_width=3,  head_length=5, length_includes_head=True)
    if ((n_1 != n_2) and (phi_rad != 0)):
        if (theta == pi/2):
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч', width=0.5, color='r',head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, 40, 0, label='Преломленный луч', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
        else:
            ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч', width=0.5, color='r',head_width=3,  head_length=5, length_includes_head=True)
    elif ((phi_rad == 0) or (n_1 == n_2)):
        ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
    ax5.set_title('Отражение и преломление падающего луча', fontsize=14)
    if (n_1 > n_2):
        rect = patches.Rectangle((-60, 0), 120, 60, linewidth=1, edgecolor='blue', facecolor='blue')
        rect.set_alpha(0.1)
        ax5.add_patch(rect)
    elif (n_1 < n_2):
        rect = patches.Rectangle((-60, 0), 120, -60, linewidth=1, edgecolor='blue', facecolor='blue')
        rect.set_alpha(0.1)
        ax5.add_patch(rect)
    else:
        rect = patches.Rectangle((-60, -60), 120, 120, linewidth=1, edgecolor='blue', facecolor='blue')
        rect.set_alpha(0.1)
        ax5.add_patch(rect)
    ax5.grid(which='major', linewidth=1, alpha=0.2)
    ax5.grid(which='minor', linestyle='--', color='gray', linewidth=0.5, alpha=0.2)
    ax5.get_xaxis().set_ticklabels([])
    ax5.get_yaxis().set_ticklabels([])
    ax5.legend(fontsize=8)
    ax5.text(-40, 45, f'n1 = {n_1}')
    ax5.text(-40, -30, f'n2 = {n_2}')
    ax5.hlines(0, -60, 60, linewidth=1, color='grey')
    plt.xlim(-60,60)
    plt.ylim(-60,60)
    return fig