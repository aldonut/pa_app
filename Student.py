class Student:

    global __name
    global __id
    global __email
    global __major
    global __intended_majors
    global __about
    global __city_of_origin
    global __housing_type
    global __schedule

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_email(self):
        return self.__email
    def set_id(self, email):
        self.__email = email

    def get_major(self):
        return self.__major
    def set_major(self, major):
        self.__major = major

    def get_intended_majors(self):
        return self.__intended_majors
    def set_intended_majors(self, intended_majors):
        self.__intended_majors = intended_majors

    def get_about(self):
        return self.__about
    def set_id(self, about):
        self.__about = about

    def get_city_of_origin(self):
        return self.__city_of_origin
    def set_city_of_origin(self, city_of_origin):
        self.__city_of_origin = city_of_origin

    def get_housing_type(self):
        return self.__housing_type
    def set_housing_type(self, housing_type):
        self.__housing_type = housing_type

    def get_schedule(self):
        return self.__schedule
    def set_schedule(self, schedule):
        self.__schedule = schedule

