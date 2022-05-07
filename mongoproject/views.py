from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
import pymongo
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient

#uri = 'localhost:27017'
# host = 'localhost'
# port = 27017
# client = MongoClient(host, port)

uri = 'mongodb://54.174.38.160:27017'
client = MongoClient(uri)

#my_client = pymongo.MongoClient(settings.DB_NAME)

# First define the database name
dbname = client['yelp']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
business_collection_name = dbname["business"]
reviews_collection_name = dbname["review"]

def business_top(request):
    print("In business top")
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

def business_find_topten(request, id):
    dictlist = []
    cursor = business_collection_name.aggregate(
        [{"$match": {"postal_code": "85711", "categories": {"$regex": "Restaurants"}}},
         {"$sort": {"stars": -1, "review_count": -1}},
         {"$limit": 10}
         ])
    for d in cursor:
        dictlist.append(d)
    print(dictlist)
    return HttpResponse(json.dumps(dictlist))

def business_category(request, category):

    dictlist = []
    for d in business_collection_name.find({"categories":{"$regex":str(category)}}):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))

def business_display_timings(request, name):

    dictlist = []
    for d in business_collection_name.find({"name":str(name), "categories":{ "$regex": "Restaurants" }},{"hours":1,"_id":0}):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))

def business_display_latestreview(request, id):
    dictlist = []
    cursor = reviews_collection_name.aggregate([{"$match": {"business_id": str(id)}},
                                                {"$sort": {"date": -1}},
                                                {"$limit": 1}
                                                ])

    for d in cursor:
        dictlist.append(d)

    print(dictlist)

    return HttpResponse(json.dumps(dictlist))

def business_takeout(request):

    dictlist = []
    for d in business_collection_name.find({'attributes.RestaurantsTakeOut' : "True"},{"_id":0}).limit(10):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))

def business_avgrating_city(request, city):
    dictlist = []
    cursor = business_collection_name.aggregate(
        [{"$match": {"city": str(city), "categories": {"$regex": "Restaurants"}}},
         {"$group": {"_id": "$city", "avg_val": {"$avg": "$stars"}}}
         ])

    for d in cursor:
        dictlist.append(d)

    print(dictlist)

    return HttpResponse(json.dumps(dictlist))

def business_avgrating_state(request, state):
    dictlist = []
    cursor = business_collection_name.aggregate(
        [{"$match": {"state": str(state), "categories": {"$regex": "Restaurants"}}},
         {"$group": {"_id": "state", "avg_val": {"$avg": "$stars"}}}
         ])

    for d in cursor:
        dictlist.append(d)

    print(dictlist)

    return HttpResponse(json.dumps(dictlist))

def business_keyword_search(request, keyword):

    dictlist = []
    for d in business_collection_name.find({"name":{"$regex":str(keyword)}}).limit(10):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))

def business_display_longestreview(request, id):
    dictlist = []
    cursor = reviews_collection_name.aggregate([{"$match": {"business_id": str(id)}}, {
        "$addFields": {
            "length": {"$strLenCP": "$text"}
        }},
                                                {"$sort": {"length": -1}},
                                                {"$limit": 1}
                                                ])

    for d in cursor:
        dictlist.append(d)

    print(dictlist)

    return HttpResponse(json.dumps(dictlist))

def business_openday(request):

    dictlist = []
    for d in business_collection_name.find({"hours.Monday": {"$exists":True}, "categories":{ "$regex": "Restaurants" }}).limit(10):
        dictlist.append(d)

    print(dictlist)
    return HttpResponse(json.dumps(dictlist))
