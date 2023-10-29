import math
import numpy as np

#to calculate weight and mass bc q unclear
def weight(DOD, se):

    #mass (0.2.11)
    m = (P * duration) / (DOD * se)

    #weight (0.2.12)
    W = m * g

    return m, W

#data given from q:
e = 0
R_E = 6378 * (10 ** (3)) # m}
h = 570 * (10 ** (3)) # m}
R_sc = R_E + h # m}
mu = 3.986 * ( 10 ** (14)) # m^3s^-2
v_cell_avg = 1.6 # V
global P
P = 6 * (10 ** (3)) # W
VDC = 32 # VDC


#calc number of cells (0.2.1)
n_cells = math.floor(VDC / v_cell_avg)
print(f"number of cells: {n_cells}")

#total voltage (0.2.3)
v = n_cells * v_cell_avg
print(f"total voltage: {v}")

#orbital period (0.2.6)
period = 2 * np.pi * np.sqrt( ((R_sc ** 3) / mu) ) #s
period /= (60 * 60) #hrs
print(f"orbital period: {period} hrs")

#duration (0.2.5)
global duration
duration = period / 2
print(f"duration: {duration} hours")

#acceleration due to gravity @ given alt (0.2.8)
global g
g = mu / (R_sc ** 2)
print(f"g: {g} ms^-2")

#list to store my answers : D
data = []

#a) Ni-Cd battery with 60 % DOD
name = "a)"
answer = weight(39, 0.6)
thing = name, answer
data.append(thing)

#b) Li-Ion battery with 60 % DOD
name = "b)"
answer = weight(80, 0.6)
thing = name, answer
data.append(thing)

#c) Li-Ion battery with 80 % DOD
name = "c)"
answer = weight(80, 0.8)
thing = name, answer
data.append(thing)

i = 0
message = ""
while i < len(data):
    name = data[i][0]
    mass, weight = data[i][1]
    part = f"{data[i][0]}:\n{mass} kg\n{weight} N\n"
    message = message + part
    i += 1

print(message)