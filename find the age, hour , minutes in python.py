# write a python code to tell waht is my  age, hours and second 
# note we are not calculted the leap year it just the tentative date



Birth_year  = int(input('enter your birth year  in yyyy: ')) # input form  user 
Today_year  = int(input('enter today year in yyyy : '))

c =(Today_year-Birth_year)                                   # formula 

print('my age is :' ,c ,'\n')

tentative_days = (365*c)                                              # formulas
tentative_hours = (tentative_days * 24)
tentative_minutes = (tentative_hours * 60)
tentative_second =  (tentative_minutes *60)

print('the tentative day you spend and enjoy  till now :', tentative_days, 'days')  # output for user  
print('tentative hours are : ',tentative_hours,'hour')
print('tentative minutes are : ',tentative_minutes,'minutes')
print('tentative second  are : ',tentative_second ,'second ','\n')

print('All the best for your bright future with lots of success ')
