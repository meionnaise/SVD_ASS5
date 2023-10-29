import numpy as np

def a(x):
    test = "placeholder""
    return test

#list to store my answers : D
data = []

#data given from q:
d_S = 1 * (10 ** (11)) #m
P_s = 3.8 * (10 ** (26)) #W
A_eff = 0.75 #m^2
sol_arr_eff = 0.2
d_E = 5 * (10 ** (10)) #m
wl = 0.01 #m
global k
k = 1.381 * 1 * (10 ** (-23)) #JK^-1
T_r = 300 #k
G_t = 68
G_r = 1 * 1 * (10 ** (7))
B = 1 * (10 ** (3)) #Hz


#################################################
#a) What is the solar array power output?
#################################################
name = "Power output"
units = "W"
answer = 
ans_a = answer
thing = name, answer, units
data.append(thing)

#######################################################################################################
#b) Assuming 100 \% of the solar array power output is used to power the spacecraft transmitter, 
#what is the signal-to-noise ratio at the Earth-based receiver?
#######################################################################################################
name = "SNR"
units = ""
answer = 
ans_b = answer
thing = name, answer, units
data.append(thing)

#print answers
i = 0
message = ""
while i < len(data):
    part = f"{data[i][0]}: {data[i][1]} {data[i][2]}\n"
    message = message + part
    i += 1

print(message)