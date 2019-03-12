import math
DAY=int(input("input the day you want to find"))
print("ENTER THE MONTH IN INTEGER FORM (1 TO 12)")
MONTH=int(input("input the month you want to find"))
YEAR=int(input("input the year you want to find"))

if MONTH in [1,3,5,7,8,10,12]:
   days_max=31

elif MONTH not in [2,1,3,5,7,8,10,12]:
    days_max=30
else:
    if MONTH==2 and YEAR%4==0 and YEAR%100!=0 or YEAR%400==0:
        days_max=29
    else:
        days_max=28
    
    
if days_max>=days_max:
    print("invalid input")


C=(YEAR%4)
if (DAY>31):
    print ("invalid input")

if (MONTH>12):
    print("invalid input")
if MONTH in [1,3,5,7,8,10,12]:
   days_max=31

elif MONTH not in [2,1,3,5,7,8,10,12]:
    days_max=30
else:
    if MONTH==2 and YEAR%4==0 and YEAR%100!=0 or YEAR%400==0:
        days_max=29
    else:
        days_max=28
    
CENTUARY=(YEAR%400)
CENTUARY1=math.floor(CENTUARY/100)
ODOC=CENTUARY1*5
RYS=CENTUARY%100
RYS1=RYS-1
LPYR=math.floor(RYS1/4)
LPYRODD=(2*LPYR)
NLPYR=(RYS1-LPYR)
ODYO=LPYRODD+NLPYR
ODYO1=ODYO%7
if (MONTH==1):
    ODMO=0
if (MONTH==2):
    ODMO=3
if ((C!=0)and(MONTH==3)):
    ODMO=4
if ((C!=0)and(MONTH==4)):
    ODMO=6
if ((C==0)and(MONTH==4)):
    ODMO=7
if ((C!=0)and(MONTH==5)):
    ODMO=8
if ((C==0)and(MONTH==5)):
    ODMO=9
if ((C!=0)and(MONTH==6)):
    ODMO=11
if ((C==0)and(MONTH==6)):
    ODMO=12
if ((C!=0)and(MONTH==7)):
    ODMO=13
if ((C==0)and(MONTH==7)):
    ODMO=14
if ((C!=0)and(MONTH==8)):
    ODMO=16
if ((C==0)and(MONTH==9)):
    ODMO=17
if ((C!=0)and(MONTH==9)):
    ODMO=19
if ((C==0)and(MONTH==9)):
    ODMO=20
if ((C!=0)and(MONTH==10)):
    ODMO=21
if ((C==0)and(MONTH==10)):
    ODMO=22
if ((C!=0)and(MONTH==11)):
    ODMO=24
if ((C==0)and(MONTH==11)):
    ODMO=25
if ((C!=0)and(MONTH==12)):
    ODMO=26
if ((C==0)and(MONTH==12)):
    ODMO=27
    
ODTO=DAY+ODMO+ODYO1+ODOC
ODTO=ODTO%7
if(ODTO==0):
    print ("SUNDAY")
if(ODTO==1):
    print ("MONDAY")
if(ODTO==2):
    print ("TUESDAY")
if(ODTO==3):
    print ("WEDNSEDAY")
if(ODTO==4):
    print ("THURSDAY")
if(ODTO==5):
    print ("FRIDAY")
if(ODTO==6):
    print ("SATURDAY")
