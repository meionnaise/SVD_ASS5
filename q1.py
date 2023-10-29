import numpy as np

#solve part a)
def a(Pin, eta, A, d):

    #calculate solar flux
    J_s = solar_flux(Pin, d)

    #equation FIX
    Psa = J_s * eta * A

    return Psa

#equation FIX
def solar_flux(P, d):
    J = P / (4 * np.pi * (d ** 2))
    print(f"Solar flux: {J} W/m^2")
    return J

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
k = 1.381 * (10 ** (-23)) #JK^-1
T_r = 300 #K
G_t = 68
G_r = 1 * (10 ** (7))
B = 1 * (10 ** (3)) #Hz


#################################################
#a) What is the solar array power output?
#################################################
name = "Power output"
units = "W"
answer = a(P_s, sol_arr_eff, A_eff, d_S)
ans_a = answer
thing = name, answer, units
data.append(thing)

#######################################################################################################
#b) Assuming 100 \% of the solar array power output is used to power the spacecraft transmitter, 
#what is the signal-to-noise ratio at the Earth-based receiver?
#######################################################################################################
name = "SNR"
units = ""
answer = 0
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