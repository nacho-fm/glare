from pandas import DatetimeIndex

from glare.models.image_metadata import ImageMetadata
from pvlib import solarposition as sp
import numpy as np


MAX_AZIMUTH_DIFFERENCE = 30
MAX_ELEVATION = 45


def detect_glare(image_metadata: ImageMetadata) -> bool:
    """
    Process the metadata requests and determine if there is a possibility of direct glare in the associated image
    or not. We assume there is a possibility of direct glare if:
        1- Azimuthal difference between sun and the direction of the car travel (and hence the direction of
           forward-facing camera) is less than 30 degrees AND
        2- Altitude of the sun is less than 45 degrees.

    In this part we assume that the weather condition does “not” affect the glare condition, in other words,
    assume the weather condition is always sunny.

    :param image_metadata: An ImageMetadata instance representing the image that is being analyzed
    :return: True if glare is possible, False if not
    """
    # Uses NREL SPA algorithm (https://midcdmz.nrel.gov/spa/)
    solar_position = sp.spa_python(DatetimeIndex(np.array([image_metadata.epoch])), image_metadata.latitude,
                                   image_metadata.longitude).to_numpy()[0]

    return np.abs(
        solar_position[4] - image_metadata.orientation) < MAX_AZIMUTH_DIFFERENCE and solar_position[3] < MAX_ELEVATION
