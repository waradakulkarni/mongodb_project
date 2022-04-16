from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import pymongo
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient

#uri = 'localhost:27017'
uri = 'mongodb://54.224.111.187:27017'
client = MongoClient(uri)

#my_client = pymongo.MongoClient(settings.DB_NAME)

# First define the database name
dbname = client['dummy']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
business_collection_name = dbname["business"]
reviews_collection_name = dbname["review"]

def business_top(request):

    dictlist=[]
    for d in business_collection_name.find({'stars':{'$gt':4}},{'_id':0}).limit(10):
        dictlist.append(d)

    return HttpResponse(json.dumps(dictlist))

def business_happyhour(request):

    dictlist=[]
    for d in business_collection_name.find({'attributes.HappyHour' : "True"}, {'_id': 0}).limit(10):
        dictlist.append(d)

    return HttpResponse(json.dumps(dictlist))


def business_isopen(request, id, open):

    business_collection_name.update_one({"business_id": id}, {"$set": {"is_open": int(open)}})

    return HttpResponse(status=200)

def business_delete(request, id):

    business_collection_name.delete_one({"business_id": id})

    reviews_collection_name.delete_many({"business_id": id})

    return HttpResponse(status=200)

@csrf_exempt
def reviews_insert(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    reviews_collection_name.insert_one(body)

    return HttpResponse(status=200)

def business_find(request, id):

    dictlist = []
    for d in business_collection_name.find({"business_id": str(id)}, {'_id': 0}).limit(1):
        dictlist.append(d)

    return HttpResponse(json.dumps(dictlist))

def review_find(request, id):

    dictlist = []
    for d in reviews_collection_name.find({"review_id": str(id)}, {'_id': 0}).limit(1):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))
