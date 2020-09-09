#!/usr/bin/python3
""" places view """
from flask import Flask, Blueprint
from flask import abort, make_response
from flask import jsonify, request
from models import storage, city, place
from api.v1.views import app_views


@app_views.route('/places',
                 methods=['GET'],
                 strict_slashes=False)
def retrieve_places():
    """ retrieve all places """
    places = []
    all_places = storage.all('Place').values()
    for place in all_places:
        places.append(place.to_dict())
    return jsonify(places)


@app_views.route('/cities/<string:city_id>/places',
                 methods=['GET'],
                 strict_slashes=False)
def get_a_place(city_id):
    """ Retrieves the list of all Place objects of a City """
    places = []
    my_city = storage.get('City', city_id)
    if my_city is None:
        abort(404)
    for my_place in my_city.places:
        places.append(my_place.to_dict())
    return jsonify(places)


@app_views.route('/places/<string:place_id>',
                 methods=['GET'],
                 strict_slashes=False)
def place_by_id(place_id):
    """ Retrieves a Place object """
    a_place = storage.get('Place', place_id)
    if a_place is None:
        abort(404)
    return jsonify(a_place.to_dict())


@app_views.route('/places/<string:place_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """ delete a Place """
    a_place = storage.get('Place', place_id)
    if a_place is None:
        abort(404)
    a_place.delete()
    storage.save()
    return jsonify({})


@app_views.route('cities/<city_id>/places',
                 methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """ create a Place """
    the_city = storage.get('City', city_id)
    if the_city is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    if 'user_id' not in request.json:
        abort(400, 'Missing user_id')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    my_user = storage.get('User', request.json.get('user_id', ""))
    if my_user is None:
        abort(404)
    req = request.get_json(silent=True)
    req['city_id'] = city_id
    the_place = place.Place(**req)
    storage.new(the_place)
    the_place.save()
    return make_response(jsonify(the_place.to_dict()), 201)


@app_views.route('/places/<string:place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """ update a Place """
    a_place = storage.get('Place', place_id)
    if a_place is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    for req in request.get_json(silent=True):
        if req not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(a_place, req, request.json[req])
    a_place.save()
    return jsonify(a_place.to_dict())
