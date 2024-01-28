import math

class Planet:

    def __init__(self):
        self.mass = 0
        self.gravitational_acceleration = 0
        self.air_density = 0
    
    def projectile_motion_object(self,Projectile,Object):
        holder = False
        while not holder:
            hit_input = ("Enter 1 to Hit the Object, Enter 2 to Go Over the Object: ")
            if hit_input == 1 or hit_input == 2:
                holder = True
        if hit_input == 1:
            hit = True
        else:
            hit = False
        holder = False
        while not holder:
            try:
                Projectile.distance_from_launcher = int("input the distance away from the edge of the object the launcher is in meters: ")
                holder = True
            except ValueError:
                print("The input was not a valid integer, please do not input units")
        
        

class Earth(Planet):

    def __init__(self):
        super().__init__()
        self.mass = 5.972*(10**24)
        self.gravitational_acceleration = 9.81
        
class Projectile:

    def __init__(self):
        self._theta_horizontal_degrees = int(input("Enter the angle to the horizontal the projectile starts at in degrees: "))
        self._initial_speed_along_theta = int(input("Enter the initial speed of the projectile along this angle: "))
        self._theta_horizontal_radians = math.radians(self._theta_horizontal_degrees)
        self._sin_theta = math.degrees(math.sin(self._theta_horizontal_radians))
        self._cos_theta = math.degrees(math.cos(self._theta_horizontal_radians))
        self.velocity_x = self._initial_speed_along_theta * self._cos_theta
        self.velocity_y = self._initial_speed_along_theta * self._sin_theta


class Object:
    def __init__(self):
        holder = False
        while not holder:
            try:
                self._height = int("input the height of the object here in metres: ")
                holder = True
            except ValueError:
                print("The input was not a valid integer, please do not put a unit")

        

class Heavy_Object(Object):

    def __init__(self):
        super().__init__()

class Light_Object(Object):

    def __init__(self):
        super().__init__()
        self._mass = 0


class Simulation:
    def __init__(self):
        self.object_list = []
        self.planet_list = [Earth]
        self.projectile_list = []