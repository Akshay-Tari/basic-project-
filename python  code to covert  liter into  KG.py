# write a python code to convert liter in kg
# data is taken from  https://vodoprovod.blogspot.com/p/convert-kg-to-liters.html

print('''\n Before converion to liter to Kg  please read the density data  Density data:
 
Density of water for 4C = 1             1000 kg/m3
Density of milk         = 1027          1033 kg/m3
Density of juice        = 1030          1300 kg/m3
Density of oil          = 800           1050 kg/m3
Density of petrol       = 700           780 kg/m3
Density of kerosene     = 780           830 kg/m3
Density of diesel fuel  = 830           860 kg/m3
 
 Density is usually indicated under normal of conditions (Pressure = 1 bar; Temperature = 273.15 K) \n''')



'''Formulas for conversion kg to liters:

1) Mass (weight) = Volume * Density '''



liter = float(input('Enter the value in liter '))
density = float(input ('Enter the value of density'))


Mass = (liter*density)

print('After conversion from liter the mass is ', Mass,'Kg')
