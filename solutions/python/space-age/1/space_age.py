class SpaceAge:
    def __init__(self, seconds):   # فقط یک پارامتر
        self.seconds = seconds
        self.earth_year_seconds = 31557600
        self.orbital_period = {
            "earth": 1.0,
            "mercury": 0.2408467,
            "venus": 0.61519726,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132,
        }

    def compute_year(self, planet:str):
        earth_year = self.seconds / self.earth_year_seconds
        return round(earth_year / self.orbital_period[planet], 2)


    def on_earth(self):
        return self.compute_year("earth")
    def on_mercury(self):
        return self.compute_year("mercury")
    def on_venus(self):
        return self.compute_year("venus")
    def on_mars(self):
        return self.compute_year("mars")
    def on_jupiter(self):
        return self.compute_year("jupiter")
    def on_saturn(self):
        return self.compute_year("saturn")
    def on_uranus(self):
        return self.compute_year("uranus")
    def on_neptune(self):
        return self.compute_year("neptune")