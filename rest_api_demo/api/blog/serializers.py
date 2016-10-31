from flask_restplus import fields
from api.restplus import api

filing = api.model('Filing', {
    'id': fields.String(readOnly=True, description='The unique identifier of a blog category'),
    'cik': fields.String(required=True, description='CIK'),
    'company_name': fields.String(required=True, description='Company Name'),
    'filing_number': fields.String(required=True, description='Filing Number'),
    'filing_type': fields.String(required=True, description='Filing Type'),
    'filing_date': fields.String(required=True, description='Filing Date'),
    'link_to_filing': fields.String(required=True, description='Link to filing on the SEC website'),
    'link_to_interactive_data': fields.String(required=True, description='Link to the interactive data')
})
