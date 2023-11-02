def dataperimg(res, bpp):
    hehe = res * bpp
    return hehe

def imgperorbit(period, freq):
    wawaweewa = period / freq
    return wawaweewa

def total_data(orbits, imgpo, datapimg):
    verrrrynice = orbits * imgpo * datapimg
    return  verrrrynice

def data_rate(dataqty, time):
    slay = dataqty / time 
    return slay

#given data:
r = 2048 * 2048 #px
b = 16 #bits
tau = 103 * 60 #s
f = 10 #s
t = 13 * 60 #s
x = 1

#list to store my answers : D
data = []

name = "D_image"
units = "bits per image"
answer = dataperimg(r, b)
ans_dim = answer
thing = name, answer, units
data.append(thing)

name = "n"
units = "images per orbit"
answer = imgperorbit(tau, f)
ans_n= answer
thing = name, answer, units
data.append(thing)

name = "D_total"
units = "bits"
answer = total_data(x, ans_n, ans_dim)
ans_dto = answer
thing = name, answer, units
data.append(thing)

name = "Data rate"
units = "bits * s^ -1"
answer = data_rate(ans_dto, t)
ans_ddot = answer
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