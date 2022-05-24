import csv

with open('bruh.csv', 'a', newline = '') as f:
    writer = csv.writer(f)
    header = ['time', 'num_bacteria', 'initial_num_phage', 'initial_num_antibiotic', 'mean_resistance']
    writer.writerow(header)

for x in range(1):
    print('bruh')