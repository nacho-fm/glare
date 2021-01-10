import connexion
from connexion.resolver import RestyResolver
from flask_cors import CORS

app = connexion.FlaskApp(__name__, specification_dir='openapi')
app.add_api('detect_glare.yaml', resolver=RestyResolver('glare.routes'))

# add CORS support
# https://connexion.readthedocs.io/en/latest/cookbook.html#cors-support
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
CORS(app.app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
