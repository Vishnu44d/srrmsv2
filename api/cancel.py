from flask import request, Blueprint, jsonify
from SRRMSv2.models.userModel import User
import uuid
import datetime
from SRRMSv2.models.userModel import db
import json
from SRRMSv2.auth.auth import validate_key, validate_user

cancelBP = Blueprint('cancelApi', __name__)

#@userBP.route('/', methods=['GET', 'POST'])