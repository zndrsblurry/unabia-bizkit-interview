import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")

# Preprocess the match data, converting lists to sets
converted_matches = [(set(fave_numbers_1), set(fave_numbers_2)) for fave_numbers_1, fave_numbers_2 in MATCHES]

@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(converted_matches):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*converted_matches[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200

# Check if there are  any matches
def is_match(fave_numbers_1, fave_numbers_2):
    return fave_numbers_2.issubset(fave_numbers_1)
