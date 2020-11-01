# OEE, this term is very popular in manufacturing industry
# so we are creating  a python program which can calculated the OEE of the assembly process

# what is OEE.?
# OEE is the framework for measuring the  efficiency and effectiveness of the process by breaking down into three component
# Availability Loss,performance loss ,Quality loss

# In simple term  formula  OEE  = (good count * ideal time )/ planned production time

# so this is python program to calculated the OEE

print(''' OEE is the framework for measuring the  efficiency and effectiveness of the assembly process by breaking down
        into three component
        1.Availability Loss
        2.performance loss
        3.Quality loss ''''\n')



A = int(input('Enter the Good count,Its means finished good at the end of the working hour:''\n'))  # it will take input form user using input function          


B = float(input('Enter the Ideal time Its Minimum time required to make one peice  in second  ''\n')) # it will take input form user using input function    


C = int(input('Enter the planned production time ,total time equiment  produce good in minutes ''\n')) # it will take input form user using input function    





OEE = ((A*B)/(C*60))*100           # formula of OEE 
print('OEE in percentage',OEE )

