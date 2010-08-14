import create

SERIAL_PORT = "/dev/ttyUSB0"
bumpAndWheelDropKeys = ['WHEELDROP_CASTER (0 = wheel raised, 1 = wheel dropped)','WHEELDROP_LEFT (0 = wheel raised, 1 = wheel dropped)','WHEELDROP_RIGHT (0 = wheel raised, 1 = wheel dropped)','BUMP_LEFT (0 no bump, 1 bump)','BUMP_RIGHT (0 = no bump, 1 = bump)']

r = create.Create( SERIAL_PORT )
bumpAndWheelDropValues = r.getSensor('BUMPS_AND_WHEEL_DROPS')

sensorDictionary  = dict(zip(bumpAndWheelDropKeys, bumpAndWheelDropValues))

keys = list(sensorDictionary.keys())
keys.sort()

for k in keys:
    print(k, ' = ',sensorDictionary[k])


############## NOTES ######################

SLIST = ["VOLTAGE","BATTERY_TEMPERATURE","CURRENT","DISTANCE","ANGLE"]
wheelDropCaster = r.getSensor('BUMPS_AND_WHEEL_DROPS')[0]
for i in SLIST:
    data = r.getSensor(i)
    print i, "=", data

for item in bumpsAndWheelDrops:
    for data in sList:    
    print( item," = ",data )
for element in [(1, 4), (2, 5), (3, 6)]:
    k, v = element
    print( k," = ",v)

dict_as_list = [(1, 4), (2, 5), (3, 6)]
d2 = {500: 2000, 1: 'a', 2: 'b', 3: 'c'}
sensorDictionary  = dict(dict_as_list, 100=4, 900=5)
sensorDictionary.update(dict_to_add)
sensorDictionary.update(dict_to_add2)
x = {'a': 1, 'b': 2, 'c': 3}
y = {"server":500, "database":600}
