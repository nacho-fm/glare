import logging
from glare.models.image_metadata import ImageMetadata
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
        test_im = ImageMetadata(random.randint(0, 90), random.randint(-180, 180),
                                random.randint(sys.maxsize), random.randint(-180, 180))
        if services.detect_glare(test_im):
            logging.info(i)
            logging.info('latitude: ' + str(test_im.latitude))
            logging.info('longitude: ' + str(test_im.longitude))
            logging.info('epoch: ' + str(test_im.epoch))
            logging.info('orientation: ' + str(test_im.orientation))
            true_counter += 1
            logging.info("Number of glares detected: " + str(true_counter))

    return true_counter


class TestDetectGlare(unittest.TestCase):
    def test_detect_glare(self):
        # Example given in the problem description, should come back as False
        self.assertFalse(services.detect_glare(ImageMetadata(49.2699648, -123.1290368, 1588704959.321, -10.2)))

    def test_detection_rate(self):
        # Seem to have a 7% glare detection on some initial runs, so should be safe to expect 6 with a large enough
        # sample size. If this frequently breaks, might need to remove or tune accordingly...
        self.assertGreaterEqual(simulate_detect_glare(1000), 60)


if __name__ == '__main__':
    unittest.main()
