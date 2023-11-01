import numpy as np

def wl(x):
    wl = 3 * (10 ** (8)) / x 
    return wl 

def area(d):
    area = np.pi * ((d ** 2) / (2))
    return area

def gain(A, efficiency, wl):
    G = (4 * np.pi * A * efficiency) / (wl ** 2)
    return G 

def SNR(Pt, Gt, bandwidth, wavelength, R, Gr, T):
    SNR = ( (Pt * Gt) / (k * B) ) * ( ( (wavelength) / (4 * np.pi * R) ) ** 2 ) * ( (Gr) / (T) )
    return SNR

#given data
B = 300 #Hz}  
P_t = 15 #W 
T = 300 #K 
R = 2500 * (10**3) #m 
eta = 0.6 
f = 2 * (10**9) #Hz 
G_t = 280 
d_r = 0.35 #m 

global k
k = 1.381 * (10 ** (-23)) #JK^-1

#list to store my answers : D
data = []

#wavelength
name = "wavelength"
units = "m"
answer = wl(f)
ans_wl = answer
thing = name, answer, units
data.append(thing)

#receiver antenna area
name = "A"
units = "m^2"
answer = area(d_r)
ans_A = answer
thing = name, answer, units
data.append(thing)

#receiver gain
name = "G_r"
units = ""
answer = gain(ans_A, eta, ans_wl)
ans_Gr = answer
thing = name, answer, units
data.append(thing)

#SNR
name = "SNR"
units = ""
answer = SNR(P_t, G_t, B, ans_wl, R, ans_Gr, T)
ans_SNR = answer
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