#   OLD CODE
# ==========================
# class Robot:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def sensors_amount():
#         return 1
#
#
# class MedicalRobot(Robot):
#     @staticmethod
#     def medical_robot_sensors_amount():
#         return 6
#
#
# class ChefRobot(Robot):
#     @staticmethod
#     def chef_robot_sensors_amount():
#         return 4
#
#
# class WarRobot(Robot):
#     @staticmethod
#     def war_robot_sensors_amount():
#         return 12
#
#
# def number_of_robot_sensors(robot):
#     if isinstance(robot, Robot):
#         print(robot.sensors_amount())
#     if isinstance(robot, MedicalRobot):
#         print(robot.medical_robot_sensors_amount())
#     elif isinstance(robot, ChefRobot):
#         print(robot.chef_robot_sensors_amount())
#     elif isinstance(robot, WarRobot):
#         print(robot.war_robot_sensors_amount())
#
#
# basic_robot = Robot('Robo')
# da_vinci = MedicalRobot('Da Vinci')
# moley = ChefRobot('Moley')
# griffin = WarRobot('Griffin')
#
# number_of_robot_sensors(basic_robot)
# number_of_robot_sensors(da_vinci)
# number_of_robot_sensors(moley)
# number_of_robot_sensors(griffin)
# =====================================================


# from abc import ABC, abstractmethod
#
#
# class BaseRobot(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     @abstractmethod
#     def sensors_amount():
#         pass


# class Robot(BaseRobot):
#     @staticmethod
#     def sensors_amount():
#         return 1


class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
