class Fan:
    no_of_wings = 0
    speed_level = 0
    motor_name = ''

    def __init__(self, no_of_wings, speed_level, motor_name):
        self.no_of_wings = no_of_wings
        self.speed_level = speed_level
        self.motor_name = motor_name


fan_object = Fan(3, 2, 'qmotor')
print(str(fan_object.no_of_wings) + ' ' + fan_object.motor_name)
