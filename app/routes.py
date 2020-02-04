#
# This file is part of MonopriceSwitcherService. https://github.com/NicholeMattera/MonopriceSwitcherService
# Copyright (C) 2020 Nichole Mattera
#

from app.views.av_view import AVView
from flask import Blueprint

api_v1_bp = Blueprint('api_v1', __name__)
api_v1_bp.add_url_rule('/av', view_func=AVView.as_view('av_view'))
