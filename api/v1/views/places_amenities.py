#!/usr/bin/python3
""" places_reviews module """
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, abort, make_response, request
from models import storage, place, review
