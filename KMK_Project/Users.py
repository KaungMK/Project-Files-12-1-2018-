class Users():
    def __init__(self, name, goal, duration):
        self.__name = name
        self.__goal = goal
        self.__duration = duration

    def get_name(self):
        return self.__name
    def get_goal(self):
        return self.__goal
    def get_duration(self):
        return self.__duration

    def set_name(self,name):
        self.__name = name
    def set_goal(self,goal):
        self.__goal = goal
    def set_duration(self,duration):
        self.__duration = duration
