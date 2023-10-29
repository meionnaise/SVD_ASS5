import math
import numpy as np

#data given from q:
e = 0
R_E = 6378 * (10 ** (3)) # m}
h = 570 * (10 ** (3)) # m}
R_sc = R_E + h # m}
mu = 3.986 * ( 10 ** (14)) # m^3s^-2
v_cell_avg = 1.6 # V
P = 6 * (10 ** (3)) # W
VDC = 32 # VDC

#calc number of cells
n_cells = math.floor(P / VDC)
print(f"number of cells: {n_cells}")

#total voltage
v = n_cells * P
print(f"total voltage: {v}")

#orbital period
period = 2 * np.pi * np.sqrt( ((R_sc ** 3) / mu) ) #s
period /= 60 #hrs
print(f"orbital period: {period} hrs")

#duration
duration = period / 2
print(f"duration: {duration} hours")

#list to store my answers : D
data = []



#template
#name = ""
#units = "Hz"
#answer = 
#ans_X = answer
#thing = name, answer, units
#data.append(thing)


#print answers
#i = 0
#message = ""
#while i < len(data):
#    part = f"{data[i][0]}: {data[i][1]} {data[i][2]}\n"
#    message = message + part
#    i += 1

#print(message)