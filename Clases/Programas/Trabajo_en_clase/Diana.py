#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def valorcoord1(x,y):
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

def valorcoord1_2(x,y):
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
                    
def valorcoord1_3(x,y):
    if (x<5 or x>25) and (y<10 or y>30):
        return(3)
    elif (x<5 or x>25) and (10<=y<=30):
        return(5)
    elif (5<=x<=25) and (y<10 or y>30):
        return(7)
    elif (5<=x<=25) and (10<=y<=30):
        return(10)
