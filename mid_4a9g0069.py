total_pins = []
stp_list = []
total_point = []
def alldown(total_pins,stp_list,i):
    if i != 9:
        if stp_list[i+1] == 2:
            return(alldown(total_pins,stp_list,i+1))
        elif stp_list[i+1] == 1:
            return(total_pins[(i+1)*2] + total_pins[(i+1)*2+1] + total_pins[(i+1)*2+2])
        else:
            return(total_pins[i*2] + total_pins[i*2+1] + total_pins[i*2+2] + total_pins[i*2+3])
    elif i==9:
        return(total_pins[i*2] + total_pins[i*2+1] + total_pins[i*2+2])
        
def score(list):
    strike = False
    spare = False
    nexts = False
    temp = 0
    sum = 0
    countlist = 0
    for i in range(20):
        if nexts:
            nexts = False
            total_pins.append(0)
            countlist += 1 
            continue
        count = list[i - countlist]
        total_pins.append(count)
        if count == 10:
            if i == 19:
                count = list[i-countlist+1]
                total_pins.append(count)
                continue   
            elif i != 18:
                nexts = True
            strike = True
        elif temp + count == 10 and i%2 == 1 and count !=10:
            spare = True
            if i == 19:
                count = list[i-countlist+1]
                total_pins.append(count)
        else:
            temp = count
        if strike:
            stp_list.append(2)
            total_point.append(0)
            strike = False
        elif spare:
            stp_list.append(1)
            total_point.append(0)
            spare = False
        else:
            if i%2 == 1:
                stp_list.append(0)
                total_point.append(0)
    for i in range(10):
        if stp_list[i] ==2:
            total_point[i] = alldown(total_pins,stp_list,i)
        elif stp_list[i] ==1:
            total_point[i] = total_pins[i*2] + total_pins[i*2+1] + total_pins[i*2+2]
        else:
            total_point[i] = total_pins[i*2] + total_pins[i*2+1]
    for i in total_point:
        sum+=i
    total_pins.clear()
    stp_list.clear()
    total_point.clear()
    return(sum)