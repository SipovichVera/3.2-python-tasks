 class Engine():


    def __init__(self, model_name, number_of_cylinders, engine_displacement, engine_resource, fuel_type):
        self.model_name = model_name
        self.number_of_cylinders = number_of_cylinders
        self.engine_displacement = engine_displacement
        self.engine_resource = engine_resource
        self.fuel_type = fuel_type 

    def __str__(self):
        return print("Model name: %s\n number of cylinders: %d\n engine displacement: %s\n engine resource: %d\n fuel type: %s", 
                    self.model_name, self.number_of_cylinders, self.engine_displacement, self.engine_resource, self.fuel_type)