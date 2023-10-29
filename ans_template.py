data = []



#template
#name = ""
#units = "Hz"
#answer = 
#ans_X = answer
#thing = name, answer, units
#data.append(thing)

i = 0
message = ""
while i < len(data):
    part = f"{data[i][0]}: {data[i][1]} {data[i][2]}\n"
    message = message + part
    i += 1

print(message)