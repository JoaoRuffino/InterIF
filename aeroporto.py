import sys

entry = ""
mode = ""
um = [] #oeste
dois = [] #sul
tres = []  #norte
quatro = [] #leste
numeros = [0, 0, 0, 0]

for line in sys.stdin:  
        entry = line.strip()
        if entry == "0":
            break 
    
        if 'A' in entry: 
            number = int(entry[1:])
            if number < 0 or number > 1000:
                continue
            
            if(mode == "-4"):
                quatro.append(entry)
                numeros[3] = numeros[3] + 1
            if(mode == "-3"):
                tres.append(entry)
                numeros[2] = numeros[2] + 1
            if(mode == "-2"):
                dois.append(entry)
                numeros[1] = numeros[1] + 1
            if(mode == "-1"):
                um.append(entry)
                numeros[0] = numeros[0] + 1
        else:
            if(int(entry) >= -4 and int(entry) <= -1):
                mode = entry
            else:
                if entry != "0":
                    continue
        

count = 0
while max(numeros) >= count:
    if(len(um) > 0):
        print(um[0])
        um.pop(0)
    if(len(tres) > 0):
        print(tres[0])
        tres.pop(0)
    if(len(dois) > 0):
        print(dois[0])
        dois.pop(0)
    if(len(quatro) > 0):
        print(quatro[0])
        quatro.pop(0)
    count = count + 1
