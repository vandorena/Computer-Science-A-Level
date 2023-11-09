class Program_State:
    def __init__(self):
        self.running = True
        self.time_keeper = 0
        self.at_sea = False
        

class Boat:
    def __init__(self,name_of_boat,boat_polar_file):
        self._boat_name = name_of_boat
        # True Wind Variables
        self.true_wind_angle = 0
        self.true_wind_direction = 0
        self.true_wind_speed = 0
        # Apparent Wind Variables
        self.apparent_wind_angle = 0
        self.apparent_wind_speed = 0
        self.apparent_wind_direction = 0
        # Boat Heading and Course
        self.course_over_ground = 0
        self.heading = 0
        self.speed_over_ground = 0
        self.speed_through_water = 0
        self.depth = 0
        # Boat Handling
        self.current_heel = 0
        self.max_heel_last_10_minutes = 0
        self.current_range_of_pitches = 0 # this is for sea state calculations
        self.percentage_polar = 0
        # GPS
        self.gps_lattitude = 0
        self.gps_longitude = 0
        # Boat Safety
        self.crew_on_board = 0
        self.mmsi_number = 0
        self.fire_alarm = False
        self.dismast = False
        self.rudder_damage = False