speed_kps = 299792.458
kmToMiles = .621
speed_mips = speed_kps * kmToMiles
half_speed_mips = speed_mips/2
quarter_speed_mips = half_speed_mips/2


earth_speed_mph = 66600
earth_speed_kps = ((earth_speed_mph / kmToMiles) / 60) / 60
speedAsPercentage = earth_speed_kps/speed_kps

print('Speed of light (Kilometers / sec):    ' +str()  + ' kps')
print('Speed of light (Miles / sec):    ' + str() + ' mps')
print('Half speed of light (Miles / sec):    ' + str() + ' mps')
print('Quarter speed of light (Miles / sec):    ' + str() + ' mps' )
print()
print('The earth moves 66,600 miles / hour around the sun')


print('66,600 miles per hour is equal to:    ' + str() +' kps')
print('66,600 miles per hour is equal to:    '+ str() +' % of the speed of light')
