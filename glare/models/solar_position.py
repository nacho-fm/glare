class SolarPosition:
    def __init__(self, altitude: float, azimuth: float):
        self._altitude = altitude
        self._azimuth = azimuth

    @property
    def altitude(self) -> float:
        return self._altitude

    @property
    def azimuth(self) -> float:
        return self._azimuth
