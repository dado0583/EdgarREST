from flask_restplus import fields
from api.restplus import api

filing = api.model('Filing', {
    '_id': fields.String(readOnly=True, description='The unique identifier of a blog category'),
    'cik': fields.String(required=True, description='CIK'),
    'companyName': fields.String(required=True, description='Company Name'),
    'File/Film Number': fields.String(required=True, description='Filing Number'),
    'Filings': fields.String(required=True, description='Filing Type'),
    'Filing Date': fields.String(required=True, description='Filing Date'),
    'DocumentsLink': fields.String(required=True, description='Link to filing on the SEC website'),
    'InteractiveDataUrl': fields.String(required=True, description='Link to the interactive data')
})

search_results = api.model('search_results', {
    '_id': fields.String(readOnly=True, description='The unique identifier of a blog category'),
    'cik': fields.String(required=True, description='CIK'),
    'companyName': fields.String(required=True, description='Company Name'),
    'File/Film Number': fields.String(required=True, description='Filing Number'),
    'Filings': fields.String(required=True, description='Filing Type'),
    'Filing Date': fields.String(required=True, description='Filing Date'),
    'DocumentsLink': fields.String(required=True, description='Link to filing on the SEC website'),
    'InteractiveDataUrl': fields.String(required=True, description='Link to the interactive data'),
    'raw_matches': fields.String(required=False, description='Matches found in the raw text of the filing'),
    'table_matches': fields.String(required=False, description='Matches found in the interactive tables')
})
