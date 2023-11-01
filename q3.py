

#given data
B = 300 #Hz}  
P_t = 15 #W 
T = 300 #K 
R = 2500 times 10^3 #m 
eta = 0.6 
f = 2 times 10^9 #Hz 
G_t = 280 
d_r = 0.35 #m 

global k
k = 1.381 * (10 ** (-23)) #JK^-1

#list to store my answers : D
data = []

#wavelength
name = "wavelength"
units = "m"
answer = 
ans_wl = answer
thing = name, answer, units
data.append(thing)

#receiver antenna area
name = "A"
units = "m^2"
answer = 
ans_A = answer
thing = name, answer, units
data.append(thing)

#receiver gain
name = "G_r"
units = ""
answer = 
ans_A = answer
thing = name, answer, units
data.append(thing)

#SNR
name = "SNR"
units = ""
answer = 
ans_A = answer
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