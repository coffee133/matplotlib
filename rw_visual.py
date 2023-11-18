import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from random_walk import RandomWalk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    # print(rw.x_values)
    plt.style.use('Solarize_Light2')

    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
    #            cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values,  linewidth=1)
    # 突出起点和终点
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    # plt.savefig('squares_plot1.png', bbox_inches='tight')
    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break