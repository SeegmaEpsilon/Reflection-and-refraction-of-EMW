from math import radians, pi, asin, sin, cos
from matplotlib import pyplot as plt
from matplotlib import patches as patches

def mnogootr_graph(n_1, n_2, phi, n_3):
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

    try:
        theta2 = asin(sin(theta)*n_2/n_3)
    except ValueError:
        theta2 = pi/2
    x_prelom2 = sin(theta2)*arrow_length
    y_prelom2 = -cos(theta2)*arrow_length
    y_otr2 = cos(theta) * arrow_length
    x_otr2 = sin(theta) * arrow_length

    try:
        theta3 = asin(sin(theta2)*n_2/n_1)
    except ValueError:
        theta3 = pi/2
    x_prelom3 = sin(theta3) * arrow_length
    y_prelom3 = cos(theta3) * arrow_length

    otraj_prel = plt.figure(9)
    fig = otraj_prel
    otraj_prel.clf()
    ax5 = otraj_prel.subplots()

    ax5.arrow(x_pad, y_pad, -x_pad, -y_pad, label='Падающий луч (n1)', width=0.5, color='blue',head_width=3,  head_length=5, length_includes_head=True)
    # print('theta', theta)
    # print('theta2', theta2)
    # print('theta3', theta3)
    if (phi_rad == 0):
        ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч (n2)', width=0.5, color='b', head_width=3, head_length=5, length_includes_head=True)
        ax5.arrow(x_prelom, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5, color='darkcyan',
                  head_width=3, head_length=5, length_includes_head=True)
    elif (phi_rad == pi/2):
        ax5.arrow(0, 0, 100, 0, label='Преломленный луч (n2)', width=0.5, color='b', head_width=3, head_length=5,
                  length_includes_head=True)
    elif (n_1 == n_2 == n_3):
        ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч (n2)', width=0.5, color='b', head_width=3,
                  head_length=5, length_includes_head=True)
        ax5.arrow(x_prelom, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5, color='b',
                  head_width=3, head_length=5, length_includes_head=True)
    elif ((n_1 != n_2)):
        if (theta == pi/2):
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч (n1)', width=0.5, color='r', head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, 40, 0, label='Преломленный луч (n2)', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
        elif (n_2 == n_3):
            ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч', width=0.5, color='g', head_width=3,
                      head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч', width=0.5, color='r', head_width=3, head_length=5,
                      length_includes_head=True)
            ax5.arrow(x_prelom, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5, color='darkcyan',head_width=3,  head_length=5, length_includes_head=True)
            ax5.text(-40, y_prelom - 10, f'n3 = {n_3}')
        elif theta3 == pi/2 and theta2 == pi/2 :
            ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч (n2)', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч (n1)', width=0.5, color='r', head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(x_prelom, y_prelom, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='g', alpha=0.5,head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2*2, 0, x_prelom, y_prelom, label='Преломленный луч', width=0.5, color='g', head_width=3,
                      head_length=5, length_includes_head=True)
            ax5.arrow(x_prelom*3, y_prelom, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='g', alpha=0.5,
                      head_width=3, head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2*4, 0, x_prelom/2, y_prelom/2, label='Преломленный луч', width=0.5, color='g', head_width=3,
                      head_length=5, length_includes_head=True, alpha=0.2)
            ax5.text(-40, y_prelom - 10, f'n3 = {n_3}')
        else:
            ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч (n2)', width=0.5, color='g',head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(0, 0, x_otr, y_pad, label='Отраженный луч (n1)', width=0.5, color='r',head_width=3,  head_length=5, length_includes_head=True)

            ax5.arrow(x_prelom, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5, color='darkcyan',head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(x_prelom, y_prelom, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='g', alpha=0.5,head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2*2, 0, x_prelom3, y_prelom3, label='Преломленный луч (n1)', width=0.5, color='black', alpha=0.5,head_width=3,  head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2*2, 0, x_prelom, y_prelom, label='Преломленный луч', width=0.5, color='g', head_width=3,
                      head_length=5, length_includes_head=True)
            ax5.arrow(x_prelom*3, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5,
                      color='darkcyan', head_width=3, head_length=5, length_includes_head=True)
            ax5.arrow(x_prelom*3, y_prelom, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='g', alpha=0.5,
                      head_width=3, head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2 * 4, 0, x_prelom3, y_prelom3, label='Преломленный луч (n1)', width=0.5, color='black',
                      alpha=0.5, head_width=3, head_length=5, length_includes_head=True)
            ax5.arrow(x_otr2*4, 0, x_prelom/2, y_prelom/2, label='Преломленный луч', width=0.5, color='g', head_width=3,
                      head_length=5, length_includes_head=True, alpha=0.2)

            ax5.vlines(x_prelom, -y_otr2-5, 0, color='black', linestyles='--', alpha=0.5)
            ax5.vlines(x_prelom*3, -y_otr2 - 5, 0, color='black', linestyles='--', alpha=0.5)
            ax5.text(-40, y_prelom - 10, f'n3 = {n_3}')

    elif (n_1 == n_2):
        ax5.arrow(0, 0, x_prelom, y_prelom, label='Преломленный луч (n2)', width=0.5, color='b',head_width=3,  head_length=0, length_includes_head=True)

        ax5.arrow(x_prelom, y_prelom, x_prelom2, y_prelom2, label='Преломленный луч (n3)', width=0.5, color='darkcyan',
                  head_width=3, head_length=5, length_includes_head=True)
        ax5.arrow(x_prelom, y_prelom, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='r', alpha=0.5,
                  head_width=3, head_length=5, length_includes_head=True)
        ax5.arrow(x_prelom*2, 0, x_otr2, y_otr2, label='Отраженный луч (n2)', width=0.5, color='r', alpha=0.5,
                  head_width=3, head_length=5, length_includes_head=True)

        ax5.vlines(x_prelom, -y_otr2 - 5, 0, color='black', linestyles='--', alpha=0.5)
        ax5.text(-40, y_prelom - 10, f'n3 = {n_3}')

    ax5.hlines(0, -500, 500, linewidth=1, color='grey')
    ax5.hlines(y_prelom, -500, 500, linewidth=1, color='grey')
    ax5.vlines(0, -10, 10, color='black', linestyles='--', alpha=0.5)
    ax5.set_title('Многократное \n отражение и преломление падающего луча', fontsize=8)
    ax5.grid(which='major', linewidth=1, alpha=0.2)
    ax5.grid(which='minor', linestyle='--', color='gray', linewidth=0.5, alpha=0.2)
    ax5.get_xaxis().set_ticklabels([])
    ax5.get_yaxis().set_ticklabels([])
    ax5.text(-40, 60, f'n1 = {n_1}')
    ax5.text(-40, -10, f'n2 = {n_2}')

    plt.xlim(-50,120)
    plt.ylim(-100,80)
    # plt.show()
    return fig