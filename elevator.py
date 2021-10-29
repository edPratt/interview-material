class System:
    def __init__(self, count):
        self.count = count

class Elevator:
    def __init__(self, size, current_floor):
       self.size = size
       self.current_floor = current_floor
    #    destinations = []
    #    self.calling_location
    
    def go_to_floor(floor_number):
        pass

    def go_down():
        pass
    
    def go_up():
        pass

    def go_to_destination(self, destination):
        pass

    def call_elevator(self, calling_location):
        # 7, current 4
        # 5, current 10
        diff = calling_location - self.current_floor
        for _ in range(diff):
            if diff >= 0:
                self.current_floor = calling_location + 1
            elif diff <= 0:
                self.current_floor = calling_location - 1
