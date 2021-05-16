
import numpy as np
from matplotlib import pyplot as plt

def plot_fig(data,heading="plot"):
    #print(data['pickups_deliveries'])
    loc=data['locations']
    plt.figure(figsize=(15,15))
    for i,row in enumerate(loc):
        #print(row)
        if i==0:
            plt.scatter(row[0],row[1],c='r')
            plt.text(row[0]+0.2, row[1]+0.2, 'DEPOT')
        else:
            plt.scatter(row[0], row[1], c='black')
            plt.text(row[0] + 0.2, row[1] + 0.2,i )
    plt.ylim(-10,600)
    plt.xlim(-10,600)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.title(heading)


def inputvisualize(data):
    plot_fig(data)

    arrowprops = dict(arrowstyle='->', connectionstyle='arc3', edgecolor='blue')
    for i, j in data['pickups_deliveries']:

        plt.annotate('', xy=[data['locations'][j][0], data['locations'][j][1]], \
                     xytext=[data['locations'][i][0],data['locations'][i][1] ], \
                     arrowprops=arrowprops)
    plt.show()

def outputvisualize(data,solution):
    plot_fig(data)

    #setcolor=['red, blue']
    setcolors = np.random.random((250, 3))
    for n,trip in enumerate(solution):
        arrowprops = dict(arrowstyle='->', connectionstyle='arc3', edgecolor=setcolors[n])
        for i in range(len(trip)-1):
            plt.annotate('', xy=[data['locations'][trip[i+1]][0], data['locations'][trip[i+1]][1]], \
                         xytext=[data['locations'][trip[i]][0], data['locations'][trip[i]][1]], \
                         arrowprops=arrowprops)




    plt.show()