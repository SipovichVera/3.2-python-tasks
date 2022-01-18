class Engine:
  
    id = 0

    def __init__(self, model_name, number_of_cylinders, engine_displacement, 
                 engine_resource, fuel_type):
        self.model_name = model_name
        self.number_of_cylinders = number_of_cylinders
        self.engine_resource = engine_resource
        self.engine_displacement = engine_displacement
        self.fuel_type = fuel_type 
        self.unique_number = self.id
        # id += 1

    def __str__(self):

        """Information about enginel"""

        return (f"\nModel name: {self.model_name}\nnumber of cylinders:" 
                f"{self.number_of_cylinders}\nengine displacement: {self.engine_displacement}"
                f"\nengine resource: {self.engine_resource}\nfuel type: {self.fuel_type}"
                f"\nunique_number: {self.unique_number}")


class Mileage(Engine):

    """Show current mileage"""

    def __init__(self, model_name, number_of_cylinders, engine_displacement, engine_resource, fuel_type, current_engine_mileage = 0):
        super().__init__(model_name, number_of_cylinders, engine_displacement, engine_resource, fuel_type)
        self.current_engine_mileage = current_engine_mileage

    @property
    def get_current_engine_mileage(self):
        return self.current_engine_mileage

    @get_current_engine_mileage.setter
    def count_current_mileage(self, current_engine_mileage):
        self.current_engine_mileage = current_engine_mileage + self.engine_resource
        return self.current_engine_mileage

    def show_difference_between_current_mileage_and_resource(self):
        return self.engine_resource-self.current_engine_mileage

    def __str__(self):

        """Information about current mileage"""

        infi_about_engine = super().__str__()
        return infi_about_engine+(f"\nCurrent mileage: {self.current_engine_mileage}")
                                #   f"\nunique_number: {self.unique_number}")

engine_1 = Engine("Sharan 2000-2010", 16, "longitudinal arrangement", 1000, "Gasoline; 2.8 liters.; Injector")
# print(engine_1)
engine_2 = Mileage("Sharan 2000-2010", 16, "longitudinal arrangement", 10000, "Gasoline; 2.8 liters.; Injector")
# print(engine_2)
engine_3 = Mileage("Sharan 2000-2010", 16, "longitudinal arrangement", 2000, "Gasoline; 2.8 liters.; Injector", 33)
print(engine_3, engine_3.show_difference_between_current_mileage_and_resource())