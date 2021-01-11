import logging
from glare.models.image_metadata import ImageMetadata
from glare.models.solar_position import SolarPosition
from numpy import random
import glare.services as services
import sys
import unittest


logging.basicConfig(level=logging.DEBUG)


# Some simulation results: 714 / 10000, 698 / 10000, 720 / 10000
#     Looks like its roughly 7% positive
def simulate_detect_glare(iterations: int = 10000) -> int:
    true_counter = 0
    for i in range(0, iterations):
        lat = random.uniform(0, 90)
        lon = random.uniform(-180, 180)
        epoch = random.uniform(0, sys.maxsize)
        orientation = random.uniform(-180, 180)

        test_im = ImageMetadata(lat, lon, epoch, orientation)
        test_sp = services.calculate_solar_position(epoch, lat, lon)

        if services.detect_glare(test_im, test_sp):
            logging.info(i)
            logging.info('latitude: ' + str(test_im.latitude))
            logging.info('longitude: ' + str(test_im.longitude))
            logging.info('epoch: ' + str(test_im.epoch))
            logging.info('orientation: ' + str(test_im.orientation))
            true_counter += 1
            logging.info("Number of glares detected: " + str(true_counter))

    return true_counter


class TestDetectGlare(unittest.TestCase):
    _test_lat = 49.2699648
    _test_lon = -123.1290368
    _test_epoch = 1588704959.321
    _test_orientation = -10.2

    def test_detect_glare(self):
        # Example given in the problem description, should come back as False
        self.assertFalse(services.detect_glare(
            ImageMetadata(self._test_lat, self._test_lon, self._test_epoch, self._test_orientation),
            services.calculate_solar_position(self._test_epoch, self._test_lat, self._test_lon)))

    def test_detection_rate(self):
        # Seem to have a 7% glare detection on some initial runs, so should be safe to expect 6 with a large enough
        # sample size. If this frequently breaks, might need to remove or tune accordingly...
        self.assertGreaterEqual(simulate_detect_glare(1000), 60)

    def test_solar_position(self):
        test_solar_pos = services.calculate_solar_position(self._test_epoch, self._test_lat, self._test_lon)
        self.assertEqual(test_solar_pos.altitude, 2.1996376615262245)
        self.assertEqual(test_solar_pos.azimuth, 229.81004254045857)


if __name__ == '__main__':
    unittest.main()
