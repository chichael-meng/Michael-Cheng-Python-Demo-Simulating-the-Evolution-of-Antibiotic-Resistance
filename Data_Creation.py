from Data_Visualization import Entity, Bacterium, Phage, distance,\
PHAGE_CONSTANT, ANTIBIOTIC_CONSTANT, MUTATION_CHANCE, REPRODUCTION_CHANCE,\
DEATH_CHANCE, BACTERIA_DEATH_MODIFIER, PHAGE_DEATH_MODIFIER, RADIUS, BOUNDS
import csv
import numpy as np
import time

file_name = 'Small_Treatment_Data.csv'
BACTERIA_RANGE = 5
PHAGE_RANGE = 5
ANTIBIOTIC_RANGE = 5
TIME_RANGE = 20

def main():
    with open(file_name, 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'num_bacteria', 'initial_num_phage', 'initial_num_antibiotic', 'mean_resistance'])
        for num_bacteria in range(1, BACTERIA_RANGE + 1):
            for num_phages in range(1, PHAGE_RANGE + 1):
                for num_antibiotics in range(1, ANTIBIOTIC_RANGE + 1):
                    all_bacteria = []
                    all_phages = []
                    all_antibiotics = []
                    for i in range(num_bacteria):
                        all_bacteria.append(Bacterium([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])], np.random.random()))
                    for i in range(num_phages):
                        all_phages.append(Phage([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])]))
                    for i in range(num_antibiotics):
                        all_antibiotics.append(Entity([np.random.uniform(0,BOUNDS[0]), np.random.uniform(0,BOUNDS[1])]))
                    print(len(all_bacteria))
                    
                    #calculating mean resistance
                    total_resistance = 0
                    for bacterium in all_bacteria:
                        total_resistance += bacterium.resistance
                    mean_resistance = total_resistance/len(all_bacteria)
                    
                    writer.writerow([0, len(all_bacteria), num_phages, num_antibiotics, mean_resistance])
                    for time in range(1, TIME_RANGE + 1):
                        if len(all_bacteria) == 0:
                            break
                        total_resistance = 0
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
                            total_resistance += bacterium.resistance

                        for phage in all_phages:
                            if 1/PHAGE_DEATH_MODIFIER * np.random.random() <= DEATH_CHANCE:
                                all_phages.remove(phage)
                                continue
                            phage.update_location()

                        for antibiotic in all_antibiotics:
                            antibiotic.update_location()

                        if len(all_bacteria) > 0:
                            mean_resistance = total_resistance/len(all_bacteria)
                        else:
                            mean_resistance = None

                        writer.writerow([time, len(all_bacteria), num_phages, num_antibiotics, mean_resistance])

    
if __name__ == '__main__':
    start_time=time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
