import create

# assign robot object to r
SERIAL_PORT = "/dev/ttyUSB0"
r = create.Create( SERIAL_PORT )

# list of bump_and_wheel_drop keys
BUMP_AND_WHEEL_DROP_KEYS = [
  'WHEELDROP_CASTER',
  'WHEELDROP_LEFT',
  'WHEELDROP_RIGHT',
  'BUMP_LEFT',
  'BUMP_RIGHT'
]

# list of bump_and _wheel_drop values
BUMP_AND_WHEEL_DROP_VALUES = r.getSensor('BUMPS_AND_WHEEL_DROPS')

# sensor dictionary of bump_and_wheel_drop keys and values
SENSORDICT = dict(zip(BUMP_AND_WHEEL_DROP_KEYS, BUMP_AND_WHEEL_DROP_VALUES))

# list of sensor keys that have a single return value
SENSORKEYS = [
    'CLIFF_LEFT_SIGNAL',
    'CLIFF_FRONT_LEFT_SIGNAL',
    'CLIFF_FRONT_RIGHT_SIGNAL',
    'CLIFF_RIGHT_SIGNAL',
    'WALL_SIGNAL',
    'DISTANCE',
    'ANGLE',
    'IR_BYTE',
    'VOLTAGE',
    'OI_MODE',
    'SONG_PLAYING',
    'SONG_NUMBER',
    'VIRTUAL_WALL',
    'CHARGING_STATE',
    'CURRENT',
    'BATTERY_TEMPERATURE',
    'BATTERY_CHARGE',
    'BATTERY_CAPACITY',
    'NUMBER_OF_STREAM_PACKETS',
    'CHARGING_SOURCES_AVAILABLE',
    'WALL',
    'CLIFF_LEFT',
    'CLIFF_FRONT_LEFT',
    'CLIFF_FRONT_RIGHT',
    'CLIFF_RIGHT',
    'VELOCITY',
    'RADIUS',
    'RIGHT_VELOCITY',
    'LEFT_VELOCITY'
]

# list of sensor values associated with sensor keys
SENSORVALUES = []
for sensor in SENSORKEYS:
    value = r.getSensor(sensor)
    SENSORVALUES.append(value)

# add sensor key and value to the sensor dictionary 
SENSORDICT1  = dict(zip(SENSORKEYS, SENSORVALUES))
SENSORDICT.update(SENSORDICT1)

# list of button keys
BUTTON_KEYS = [
  'BUTTON_ADVANCE',
  'BUTTON_PLAY'
]

# list of button values
BUTTON_VALUES = r.getSensor('BUTTONS')

# sensor dictionary of bump_and_wheel_drop keys and values
SENSORDICT2 = dict(zip(BUTTON_KEYS, BUTTON_VALUES))
SENSORDICT.update(SENSORDICT2)

# list of overcurrent keys
OVERCURRENT_KEYS = [
    'LEFT_WHEEL',
    'RIGHT_WHEEL',
    'LD_2',
    'LD_0',
    'LD_1'
]

# list of overcurrent values
OVERCURRENT_VALUES = r.getSensor('OVERCURRENTS') 

# sensor dictionary of overcurrent keys and values 
SENSORDICT3 = dict(zip(OVERCURRENT_KEYS, OVERCURRENT_VALUES))
SENSORDICT.update(SENSORDICT3)

# Display the sensor dictionary
keys = list(SENSORDICT.keys())
keys.sort()
for k in keys:
    print(k, ' = ',SENSORDICT[k])

r.shutdown()
