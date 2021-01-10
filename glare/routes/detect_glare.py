from glare.services import detect_glare
import flask
from glare.models.image_metadata import ImageMetadata


# /detect_glare POST
def post():
    flask_request = flask.request.get_json()
    glare_detected = detect_glare(ImageMetadata(flask_request['lat'], flask_request['lon'],
                                                flask_request['epoch'], flask_request['orientation']))
    # Convert glare_detected from bool to string based on the defined project requirements
    # Note that as the boolean type is valid JSON, there needs to be a good reason to do this in production...
    return flask.jsonify({'glare': str(glare_detected)})
