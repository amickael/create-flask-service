import os

from flask_restx import Api
from marshmallow import ValidationError


########################################################################################################################
# Config
########################################################################################################################

VERSION = "v1"
api = Api(
    title="{{ %SERVICE_NAME% }}",
    version=VERSION,
    prefix=f"/api/{VERSION}",
    doc="/" if os.getenv("FLASK_ENV") == "development" else False,
)


@api.errorhandler(ValidationError)
def handle_validation_error(error: ValidationError):
    del error.data
    return {"message": error.messages}, 400


########################################################################################################################
# Namespaces
########################################################################################################################
