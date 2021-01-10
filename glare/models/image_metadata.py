class ImageMetadata:
    def __init__(self, latitude: float, longitude: float, epoch: float, orientation: float):
        self._latitude = latitude
        self._longitude = longitude
        self._epoch = epoch
        self._orientation = orientation

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def epoch(self) -> float:
        return self._epoch

    @property
    def orientation(self) -> float:
        return self._orientation
