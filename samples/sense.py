import create
import time

SERIAL_PORT = "/dev/ttyUSB0"
r = create.Create( SERIAL_PORT )

def sensor_dict_list(sensor_list, sensor_list_keys):
    """Obtain sensor values returned as list."""
    values_list = r.getSensor(sensor_list)
    time.sleep(.015)
    sensor_dict = dict(zip(sensor_list_keys, values_list))
    return sensor_dict
    
def sensor_dict_int(sensor_keys):
    """Obtain sensor values returned as integers."""
    sensor_values  = [r.getSensor(sensor) for sensor in sensor_keys]
    time.sleep(.015)
    sensor_dict = dict(zip(sensor_keys, sensor_values))
    return sensor_dict

def sensor_print(sensor_dict):
    keys = list(sensor_dict.keys())
    keys.sort()
    for k in keys:
        print(k, ' = ',sensor_dict[k])

# list of sensor keys that have a single return value
SENSOR_KEYS = [
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

BUMP_AND_WHEEL_DROP_KEYS = [
  'WHEELDROP_CASTER',
  'WHEELDROP_LEFT',
  'WHEELDROP_RIGHT',
  'BUMP_LEFT',
  'BUMP_RIGHT'
]

BUTTON_KEYS = [
  'BUTTON_ADVANCE',
  'BUTTON_PLAY'
]

OVERCURRENT_KEYS = [
    'LEFT_WHEEL',
    'RIGHT_WHEEL',
    'LD_2',
    'LD_0',
    'LD_1'
]

sensor_dict = sensor_dict_int(SENSOR_KEYS)
sensor_dict_add = sensor_dict_list('BUMPS_AND_WHEEL_DROPS', BUMP_AND_WHEEL_DROP_KEYS)
sensor_dict.update(sensor_dict_add)
sensor_dict_add = sensor_dict_list('BUTTONS', BUTTON_KEYS)
sensor_dict.update(sensor_dict_add)
sensor_dict_add = sensor_dict_list('OVERCURRENTS', OVERCURRENT_KEYS)
sensor_dict.update(sensor_dict_add)
sensor_print(sensor_dict)
r.shutdown()
