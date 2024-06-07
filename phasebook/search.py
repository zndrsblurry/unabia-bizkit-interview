from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database
    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!
    results = []
    for user in USERS:
        matches = []
        # Check ID if it matches
        if "id" in args and user["id"] == args["id"]:
            matches.append("id")
        # Check name
        if "name" in args and args["name"].lower() in user["name"].lower():
            matches.append("name")
        # Check age range
        if "age" in args:
            try:
                age = int(args["age"])
                if age - 1 <= user["age"] <= age + 1:
                    matches.append("age")
            except ValueError:
                pass  # Ignore invalid age input
        # Check occupation
        if "occupation" in args and args["occupation"].lower() in user["occupation"].lower():
            matches.append("occupation")
        if matches:
            results.append((user, matches))
    # return the search results sorted based on the following priority on how they were matched
    return [user for user, _ in sorted(results, key=lambda x: [
        "id" in x[1], 
        "name" in x[1], 
        "age" in x[1], 
        "occupation" in x[1]
    ], reverse=True)]
