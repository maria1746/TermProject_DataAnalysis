class MassPercentage:
    """쓰레기 종류별 percentage"""
    def __init__(self, first, secod):
        self.first = first[:]
        self.second = secod[:]
        
    def percentage_of_mass(self):
        percentage_mass = []
        for i in range(9):
            result = round(self.second[i] / self.first[i] * 100)
            percentage_mass.append(result)
        return percentage_mass