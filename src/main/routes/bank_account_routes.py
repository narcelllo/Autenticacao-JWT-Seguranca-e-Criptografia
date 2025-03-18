from flask import jsonify, Blueprint

bank_routes_bp = Blueprint("banck_routes", __name__)

@bank_routes_bp.route("/", methods={"GET"})
def hello():
    return jsonify({"hello": "world"}), 200