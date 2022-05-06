#This program simulates the evolution of antibiotic resistance in a bacterial population
#Efflux pumps are an important mechanism of antiobiotic resistance that allows bacteria to expel antibiotics
#However, efflux pumps can also be targeted by phages
#I was interested in exploring this evolutionary tradeoff and simulating how bacterial population would react to exposure to phages and antibiotics
#Bacteria show variation in their efflux pump expression (represented nummerically as a numerical "mean antibiotic resistance value") and will occasionally mutate
#The user can set an initial number of bacteria (blue dots), phages (green dots), and antiobiotic molecules (red dots) to interact in a physical space
#The extent to which the bacterial population adapts to the presence of phages and antibiotics is measured by tracking the mean antibiotic resistance value over time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

print('This program simulates the evolution of antibiotic resistance in a bacterial population.\n\
Efflux pumps are an important mechanism of antiobiotic resistance that allows bacteria to expel antibiotics, providing an evolutionary incentive for their expression when antibiotics are present.\n\
However, efflux pumps can also be targeted by phages, causing efflux pump expression to be disincentivised when phages are present.\n\
I was interested in exploring this evolutionary tradeoff and simulating how bacterial population would react to exposure to phages and antibiotics.\n\
Bacteria show variation in their efflux pump expression (represented nummerically as a numerical "mean antibiotic resistance value") and will occasionally mutate.\n\
The user can set an initial number of bacteria (blue dots), phages (green dots), and antiobiotic molecules (red dots) to interact in a physical space\n\
The extent to which the bacterial population adapts to the presence of phages and antibiotics is measured by tracking the mean antibiotic resistance value over time.')

BOUNDS = (40,40)
all_bacteria = []
all_antibiotics = []
all_phages = []
PHAGE_CONSTANT = 1
ANTIBIOTIC_CONSTANT = 1
NUM_BACTERIA = int(input('How many bacteria would you like? '))
NUM_PHAGES = int(input('How many phages would you like? '))
NUM_ANTIBIOTICS = int(input('How many antibiotic molecules would you like? '))
#The program will prompt the user to input the number bacteria, phages, and antibiotic molecules they would like
MUTATION_CHANCE = 0.05 
REPRODUCTION_CHANCE = 0.01
DEATH_CHANCE = 0.01
BACTERIA_DEATH_MODIFIER = 1
PHAGE_DEATH_MODIFIER = 0.25
RADIUS = 0.25


def distance(coord_1,coord_2):
    return np.sqrt((coord_1[0]-coord_2[0])**2 + (coord_1[1]-coord_2[1])**2)

class Entity:
    def __init__(self, coords):
        self.coord = coords
        self.angle = np.random.uniform(0,2*np.pi)
        self.x_direction = np.cos(self.angle)
        self.y_direction = np.sin(self.angle)

    def update_location(self):
        distance = np.random.uniform(0.5, 1)

        if self.coord[0] + distance*self.x_direction < 0:
            new_x = -distance*self.x_direction - self.coord[0]
            self.x_direction *= -1
        elif self.coord[0] + distance*self.x_direction > BOUNDS[0]:
            new_x = 2*BOUNDS[0] - distance*self.x_direction - self.coord[0]
            self.x_direction *= -1
        else:
            new_x = self.coord[0] + distance*self.x_direction

        if self.coord[1] + distance*self.y_direction < 0:
            new_y = -distance*self.y_direction - self.coord[1]
            self.y_direction *= -1
        elif self.coord[0] + distance*self.y_direction > BOUNDS[1]:
            new_y = 2*BOUNDS[1] - distance*self.y_direction - self.coord[1]
            self.y_direction *= -1
        else:
            new_y = self.coord[1] + distance*self.y_direction

        self.coord = (new_x, new_y)

class Phage(Entity):
    def reproduce(self, offspring):
        for i in range(offspring):
            all_phages.append(Phage(self.coord))

class Bacterium(Entity):
    def __init__(self, coords, resistance):
        self.coord = coords
        self.angle = np.random.uniform(0,2*np.pi)
        self.x_direction = np.cos(self.angle)
        self.y_direction = np.sin(self.angle)
        self.resistance = resistance
   
    def reproduce(self, offspring):
        for i in range(offspring):
            all_bacteria.append(Bacterium(self.coord, self.resistance))

    def interact(self):
        is_phage = False
        for phage in all_phages:
                if PHAGE_CONSTANT * self.resistance * np.random.uniform(0,2) > 1 and distance(self.coord, phage.coord) < RADIUS: 
                    #the bacterium is more vulnerable to phages if its resistance is high
                    all_bacteria.remove(self)
                    phage.reproduce(2)
                    is_phage = True
                    break
        if not is_phage:
            for antibiotic in all_antibiotics: 
                if ANTIBIOTIC_CONSTANT * self.resistance * np.random.uniform(0,2) < 1 and distance(self.coord, antibiotic.coord) < RADIUS: 
                    #the bacterium is more vulnerable to phages if its resistance is low
                    all_bacteria.remove(self)
                    break
    def mutate(self):
        self.resistance += 0.25 * np.random.normal()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=(0, BOUNDS[0]), ylim=(0, BOUNDS[1]))

for i in range(NUM_BACTERIA):
    all_bacteria.append(Bacterium([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])], np.random.random()))
for i in range(NUM_PHAGES):
    all_phages.append(Phage([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])]))
for i in range(NUM_ANTIBIOTICS):
    all_antibiotics.append(Entity([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])]))

def animate(frame):
    bacteria_x_coords = []
    bacteria_y_coords = []
    phage_x_coords = []
    phage_y_coords = []
    antibiotic_x_coords = []
    antibiotic_y_coords = []
    global total_resistance 
    total_resistance = 0
    artists = []

    average_resistance = ax.text(8.5,35,'No Bacteria')
    for bacterium in all_bacteria:
        bacteria_x_coords.append(bacterium.coord[0])
        bacteria_y_coords.append(bacterium.coord[1])
        total_resistance += bacterium.resistance
    for phage in all_phages:
        phage_x_coords.append(phage.coord[0])
        phage_y_coords.append(phage.coord[1])       
    for antibiotic in all_antibiotics:
        antibiotic_x_coords.append(antibiotic.coord[0])
        antibiotic_y_coords.append(antibiotic.coord[1])

    for bacterium in all_bacteria:
        x = len(all_bacteria)
        bacterium.interact()
        if len(all_bacteria) < x:
            continue
        if np.random.random() <= MUTATION_CHANCE:
            bacterium.mutate()
        if np.random.random() <= REPRODUCTION_CHANCE:
            bacterium.reproduce(1)
        if 1/BACTERIA_DEATH_MODIFIER * np.random.random() <= DEATH_CHANCE:
            all_bacteria.remove(bacterium)
            continue
        bacterium.update_location()

    for phage in all_phages:
        if 1/PHAGE_DEATH_MODIFIER * np.random.random() <= DEATH_CHANCE:
            all_phages.remove(phage)
            continue
        phage.update_location()

    for antibiotic in all_antibiotics:
        antibiotic.update_location()

    if len(all_bacteria) > 0:
        average_resistance.set_text('Mean Antibiotic Resistance Value: '+ str(round(total_resistance/len(all_bacteria), 4)))
  
    return [ax.scatter(bacteria_x_coords, bacteria_y_coords, color = 'b'), ax.scatter(phage_x_coords, phage_y_coords, color = 'g'), ax.scatter(antibiotic_x_coords, antibiotic_y_coords, color = 'r'), average_resistance]

anim = FuncAnimation(fig, animate, interval=20, blit=True, frames = 100)

plt.show()
