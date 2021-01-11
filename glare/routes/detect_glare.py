from glare.services import detect_glare, calculate_solar_position
import flask
from glare.models.image_metadata import ImageMetadata


# /detect_glare POST
def post():
    # Note that missing parameters, invalid parameters, bound validation, etc. is largely handled by the
    # connexion framework. We're guaranteed to have epoch, lat, lon, and orientation in our request object
    # by this point in the workflow.
    flask_request = flask.request.get_json()
    lat = flask_request['lat']
    lon = flask_request['lon']
    epoch = flask_request['epoch']
    orientation = flask_request['orientation']

    glare_detected = detect_glare(ImageMetadata(lat, lon, epoch, orientation),
                                  calculate_solar_position(epoch, lat, lon))

    # Convert glare_detected from bool to a lower cased string based on the defined project requirements
    # Note that as the boolean type is valid JSON, there needs to be a REALLY good reason to do this in production...
    return flask.jsonify({'glare': str(glare_detected).lower()})
