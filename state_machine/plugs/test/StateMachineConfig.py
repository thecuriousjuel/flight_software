from Tasks.battery_task import task as battery
from Tasks.beacon_task import task as beacon
from Tasks.blink_task import task as blink
from Tasks.imu_task import task as imu
from Tasks.time_task import task as time
from Tasks.test_task import task as test
from Tasks.lowpower5 import task as lowpower5
from Tasks.lowpower5later import task as lowpower5later
from Tasks.detumble import task as detumble

from TransitionFunctions import announcer

TaskMap = {
    'Battery': battery,
    'Beacon': beacon,
    'Blink': blink,
    'IMU': imu,
    'Time': time,
    'Test': test,
    'LowPower5': lowpower5,
    'LowPower5Later': lowpower5later,
    'Detumble': detumble,
}

TransitionFunctionMap = {
    'Announcer': announcer
}

config = {
    'Normal': {
        'Tasks': {
            'Battery': {
                'Interval': 10,
                'Priority': 3,
                'ScheduleLater': False
            },
            'IMU': {
                'Interval': 10,
                'Priority': 5,
                'ScheduleLater': False
            },
            'Beacon': {
                'Interval': 20,
                'Priority': 1,
                'ScheduleLater': True
            },
            'Blink': {
                'Interval': 2,
                'Priority': 255,
                'ScheduleLater': False
            },
            'Time': {
                'Interval': 20,
                'Priority': 4,
                'ScheduleLater': False
            },
            'Test': {
                'Interval': 3,
                'Priority': 1,
                'ScheduleLater': False
            },
            'Detumble': {
                'Interval': 5.0,
                'Priority': 3,
                'ScheduleLater': False
            }
        },
        'StepsTo': ['LowPower', 'DeTumble'],
        'EnterFunctions': ['Announcer'],
        'ExitFunctions': ['Announcer'],
    },
    'LowPower': {
        'Tasks': {
            'Battery': {
                'Interval': 15.0,
                'Priority': 1,
                'ScheduleLater': False
            },
            'LowPower5': {
                'Interval': 5.0,
                'Priority': 2,
                'ScheduleLater': False
            },
            'LowPower5Later': {
                'Interval': 15.0,
                'Priority': 2,
                'ScheduleLater': True
            }
        },
        'StepsTo': ['Normal']
    },
    'DeTumble': {
        'Tasks': {
            'Battery': {
                'Interval': 15.0,
                'Priority': 3,
                'ScheduleLater': False
            },
            'Detumble': {
                'Interval': 5.0,
                'Priority': 3,
                'ScheduleLater': False
            }
        },
        'StepsTo': ['Normal']
    }
}
