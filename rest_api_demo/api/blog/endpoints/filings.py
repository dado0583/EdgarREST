import json
import logging
import urllib

from flask import request
from flask_restplus import Resource

from api.blog.parsers import pagination_arguments
from api.blog.serializers import filing  # , page_of_blog_posts
from api.restplus import api
from database.MongoDb import MongoDb


#from database.models import Post
#from rest_api_demo.api.blog.business import create_blog_post, update_post, delete_post
#from rest_api_demo.api.blog.serializers import blog_post, page_of_blog_posts
#from rest_api_demo.api.blog.parsers import pagination_arguments
#from rest_api_demo.api.restplus import api
#from rest_api_demo.database.models import Post
log = logging.getLogger(__name__)

ns = api.namespace('filings', description='Operations related to filings')


@ns.route('/')
class FilingsCollection(Resource):
    mongo = MongoDb().getDb('sec')['filings']

    @api.expect(pagination_arguments)
    #@api.marshal_with(filing)
    @api.marshal_list_with(filing)
    def get(self):
        """
        Returns list of SEC Filings.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        #posts_query = Post.query
        #posts_page = posts_query.paginate(page, per_page, error_out=False)
         
        low = (page * per_page) - per_page

        records = self.mongo.find({}, {"RawText":0,"InteractiveDataTables":0}).skip(low).limit(per_page)
        
        json =  []
        
        for record in records:
            json.append(record)
        
        return json #"hello" #posts_page

    @api.expect(filing)
    def post(self):
        """
        Creates a new SEC filing.
        """
        #create_blog_post(request.json)
        return None, 201


@ns.route('/<string:id>')
@api.response(404, 'Post not found.')
class FilingItem(Resource):
    mongo = MongoDb().getDb('sec')['filings']
        
    @api.marshal_with(filing)
    def get(self, id):
        """
        Returns a summary about an SEC filing.
        """
        id = urllib.request.unquote(id)
        ##TODO - Can we encode this on the swagger level?
        
        #example_id = "001-05794/121170625"
        record = self.mongo.find_one({"_id":id}, {"RawText":0,"InteractiveDataTables":0})
        
        if record is None:
            api.abort(code=404, message="No match found for _id: "+ id)
        
        return record

    @api.expect(filing)
    @api.response(204, 'Post successfully updated.')
    def put(self, id):
        """
        Updates an SEC filing.
        """
        data = request.json
        #update_post(id, data)
        return None, 204

    @api.response(204, 'Post successfully deleted.')
    def delete(self, id):
        """
        Deletes an SEC filing.
        """
        #delete_post(id)
        return None, 204
