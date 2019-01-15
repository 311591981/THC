def valorcoord2(x,y):
    if 5<=x<=25 and 10<=y<=30 and pow(10,2)<=pow((x-15),2)+pow((y-20),2):
        return(100)
    else:
        if x<5 and y<10:
            return(3)
        else:
            if 5<=x<=25 and y<10:
                return(7)
            else:
                if x>25 and y<10:
                    return(3)
                else:
                    if x<5 and 10<=y<=30:
                        return(5)
                    else:
                        if 5<=x<=25 and 10<=y<=30:
                            return(10)
                        else:
                            if x>25 and 10<=y<=30:
                                return(5)
                            else:
                                if x<5 and y>30:
                                    return(3)
                                else:
                                    if 5<=x<=25 and y>30:
                                        return(7)
                                    else:
                                        if x>25 and y>30:
                                            return(3)
                                        else:
                                            print "ERROR"

def valorcoord2_2(x,y):
    if 5<=x<=25 and 10<=y<=30 and pow(10,2)<=pow((x-15),2)+pow((y-20),2):
        return(100)
    else:
        if (x<5 or x>25) and (y<10 or y>30):
            return(3)
        else:
            if (x<5 or x>25) and (10<=y<=30):
                return(5)
            else:
                if (5<=x<=25) and (y<10 or y>30):
                    return(7)
                else:
                    if (5<=x<=25) and (10<=y<=30):
                        return(10)
                    else:
                        print "ERROR"

def valorcoord2_3(x,y):
    if 5<=x<=25 and 10<=y<=30 and pow(10,2)<=pow((x-15),2)+pow((y-20),2):
        return(100)
    elif (x<5 or x>25) and (y<10 or y>30):
        return(3)
    elif (x<5 or x>25) and (10<=y<=30):
        return(5)
    elif (5<=x<=25) and (y<10 or y>30):
        return(7)
    elif (5<=x<=25) and (10<=y<=30):
        return(10)
    else:
        print "ERROR"

#circulo con centro en p=(15,20), radio r=(10) y el valor en puntos es 100
