from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from blog.models import Article, Category


@registry.register_document
class UserDocument(Document):
    class Index:
        name = "users"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username"
        ]

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = "categories"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = Category
        fields = [
            "name", 
            "description"
        ]

@registry.register_document
class ArticleDocument(Document):
    author = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "first_name": fields.TextField(),
        "last_name": fields.TextField(),
        "username": fields.TextField()
    })

    categories = fields.ObjectField(properties={
        "id": fields.IntegerField(),
        "name": fields.TextField(),
        "description": fields.TextField()
    })

    type = fields.TextField(attr="type_to_string")

    class Index:
        name = "article"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    
    class Django:
        model = Article
        fields = [
            "title", 
            "content",
            "created_datetime",
            "updated_datetime"
        ]
    

# from elasticsearch import Q


# query = "how to"
# q = Q(
#     "multi_match",
#     query=query,
#     fields=[
#         "title"
#     ]
# )

# search = ArticleDocument.search().query(q)
# response = search.execute()

# for hit in response:
#     print(hit.title)