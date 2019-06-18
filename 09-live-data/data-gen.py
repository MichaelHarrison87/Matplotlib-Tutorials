import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_values", "total_1", "total_2"]


csv_path = "../data/generated-data.csv"

with open(csv_path, "a") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    
    with open(csv_path, "a") as csv_file:
        
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        info = {"x_values": x_value,
                "total_1": total_1,
                "total_2": total_2}
        
        csv_writer.writerow(info)
        print(x_value, total_1, total_2)
        
        x_value += 1
        total_1 += random.randint(-6, 8)
        total_2 += random.randint(-5, 6)

    time.sleep(1)
    

