from glare.services import detect_glare
import flask
from glare.models.image_metadata import ImageMetadata


# /detect_glare POST
def post():
    flask_request = flask.request.get_json()
    glare_detected = detect_glare(ImageMetadata(flask_request['lat'], flask_request['lon'],
                                                flask_request['epoch'], flask_request['orientation']))
    return flask.jsonify({'glare': str(glare_detected)})
