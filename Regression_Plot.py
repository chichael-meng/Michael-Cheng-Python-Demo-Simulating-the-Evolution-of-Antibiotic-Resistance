import pandas
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot():
    colnames = ['time', 'num_bacteria', 'initial_num_phage', 'initial_num_antibiotic', 'mean_resistance']
    data = pandas.read_csv('Small_Treatment_Data.csv', names=colnames)

    time = np.delete(np.array(data['time'].tolist()), 0).astype(float)
    num_bacteria = np.delete(np.array(data['num_bacteria'].tolist()), 0).astype(float)
    initial_num_phage = np.delete(np.array(data['initial_num_phage'].tolist()), 0).astype(float)
    initial_num_antibiotic = np.delete(np.array(data['initial_num_antibiotic'].tolist()), 0).astype(float)
    mean_resistance = np.delete(np.array(data['mean_resistance'].tolist()), 0).astype(float)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    user = ''
    img = ''
    while user != '1' and user != '2':
        user = input('Input 1 to plot the mean resistance and input 2 to plot the number of bacteria ')
    if user == 1:
        img = ax.scatter(time, initial_num_phage, initial_num_antibiotic, c=mean_resistance, cmap=plt.hot())
    elif user == 2:
        img = ax.scatter(time, initial_num_phage, initial_num_antibiotic, c=num_bacteria, cmap=plt.hot())
    
    fig.colorbar(img)
    ax.set_xlabel('Time')
    ax.set_ylabel('Initial Phage Count')
    ax.set_zlabel('Initial Antibiotic Count')
    plt.show()

if __name__ == '__main__':
    plot()