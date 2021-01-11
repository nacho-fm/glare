from glare.models.image_metadata import ImageMetadata
from glare.models.solar_position import SolarPosition
from pvlib import solarposition as sp
import numpy as np
from pandas import DatetimeIndex

MAX_AZIMUTH_DIFFERENCE = 30
MAX_ELEVATION = 45


def detect_glare(image_metadata: ImageMetadata, solar_position: SolarPosition) -> bool:
    """
    Process the metadata requests and determine if there is a possibility of direct glare in the associated image
    or not. We assume there is a possibility of direct glare if:
        1- Azimuthal difference between sun and the direction of the car travel (and hence the direction of
           forward-facing camera) is less than 30 degrees AND
        2- Altitude of the sun is less than 45 degrees.

    In this part we assume that the weather condition does “not” affect the glare condition, in other words,
    assume the weather condition is always sunny.

    :param image_metadata: An ImageMetadata instance representing the image that is being analyzed
    :param solar_position: A SolarPosition instance representing the location of the sun given a latitude, longitude,
                           and epoch timestamp.
    :return: True if glare is possible, False if not
    """
    return np.abs(solar_position.azimuth - image_metadata.orientation) < MAX_AZIMUTH_DIFFERENCE and (
            solar_position.altitude < MAX_ELEVATION)


def calculate_solar_position(epoch: float, latitude: float, longitude: float):
    """
    Use the NREL SPA algorithm to calculate the position of the sun relative to an observer.

    Reference: https://midcdmz.nrel.gov/spa/

    :param epoch: A unix epoch timestamp
    :param latitude: The latitude of the observer to calculate the solar position against
    :param longitude: The longitude of the observer to calculate the solar position against
    :return: A SolarPosition object representing the position of the sun
    """
    solar_position = sp.spa_python(DatetimeIndex(np.array([epoch])), latitude, longitude).to_numpy()[0]
    return SolarPosition(solar_position[3], solar_position[4])


def retrieve_weather():
    """
    TODO: Stub for future implementation. Look into https://api.weatherstack.com/historical
    """
    pass
