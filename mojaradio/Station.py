class Station:
    def __init__(self, station_id, name, programs):
        self.id = station_id
        self.name = name
        self.programs = programs

    def show_info(self):
        print(self.id, self.name)

    def show_programs(self):
        for program in self.programs:
            program.show_info()
