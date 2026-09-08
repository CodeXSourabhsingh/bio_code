# Bio_Python project

while True:
    try:
        BC = int(input('enter bacterial count : ')) #Bacterial count
        NG = int(input('enter nutrient glucose : ')) #Nutrient growth
        IT = float(input('enter incubation tempreature : ')) # Incubation tempreatue

        multiplier = 1.0

        if BC >= 1000000 :          
            multiplier = 1.0
        elif NG <= 0 :
             multiplier = 0.5
        elif (IT <10):
           multiplier = 1.0
        elif (10<=IT<=25):
            multiplier = 1.2
        elif (26<=IT<=40) :
            multiplier = 2.0
        elif (IT>40) :
             multiplier = 0.0 
        else:
            print('!warning!')        
        print(int(BC*multiplier))   
        break 
    except:
        print('Invalid input. Please enter a valid number.')

import time
current_hour = 1
while current_hour<=24:
    if BC >= 1000000 :
         multiplier = 1.0
    elif NG <= 0:
         multiplier = 0.5
    elif (IT <10):
         multiplier = 1.0
    elif (10<=IT<=25):
         multiplier = 1.2
    elif (26<=IT<=40) :
         multiplier = 2.0
    elif (IT>40) :
          multiplier = 0.0 
    else:
        print('!warning!')
    BC = (int(BC*multiplier))
    NG = (int(NG - (BC*0.1)))
     
    if NG < 0:
        NG = 0
    print("Hour:",current_hour,"|Bacteria:",BC,'|Nutrients:',NG)
    current_hour = current_hour+1
    time.sleep(1)
   
   
        