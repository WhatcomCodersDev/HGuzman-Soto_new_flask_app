from flask import Blueprint, jsonify, request, make_response

bp = Blueprint("profiles", __name__)


@bp.route('/health', methods=['GET'])
def health_check():
    response = make_response(jsonify({'status': 'ok'}), 200)
    return response

@bp.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    response = make_response(jsonify(data), 200)
    return response
