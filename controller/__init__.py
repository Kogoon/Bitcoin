from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='')
api = Api(blueprint, 
        title = 'Test',
        version = '0.1',
        description = 'Test', 
        doc = '/api/doc'
)