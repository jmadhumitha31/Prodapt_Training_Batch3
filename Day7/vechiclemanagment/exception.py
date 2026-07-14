class VehicleError(Exception):
    pass

class OwnerAlreadyExistsError(VehicleError):
    def __init__(self,owner_name):
        message=f"Owner '{owner_name}' already exists."
        super().__init__(message)


class InvalidBatteryCapacityError(VehicleError):
    def __init__(self, capacity):
        message = f"Invalid battery capacity: {capacity}"
        super().__init__(message)
         

