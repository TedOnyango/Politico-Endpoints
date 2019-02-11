from flask import Flask, jsonify, make_response, request
from app.api.v1.models.officemodels import OfficeModel
from app.api.v1.models.partymodels import PartiesModel
from app.api.v1.routes import endpoint


@endpoint.route('/offices', methods=['POST'])
def create_office():
    data = request.get_json()
    try:
        type = data['type']
        name = data['name']
        id = data['id']
    except:
        return make_response(jsonify({"status": 400,
									  "error": "Must provide id, name and type"
									  }), 400)

    newoffice = OfficeModel(name=name, type=type, id=id)
    newoffice.save_office()

    return make_response(jsonify({ "status": 201,
									"data": [{
										"type": type,
										"name": name,
										"id": id
									}]
								}), 201)
@endpoint.route('/offices', methods=['GET'])
def get_all_offices():
    return make_response(jsonify({"status": 200, "data": OfficeModel.view_all_offices()}), 200)

@endpoint.route('/offices/<int:id>')
def get_specific_office(id):
	office = OfficeModel.get_specific_office(id)
	if office:
		return make_response(jsonify({"status": 200,
										"data": office
									}), 200)

	return make_response(jsonify({"status": 404,
									"error": "Office not found"
								}), 404)

@endpoint.route('/offices/<int:id>/name', methods=['PATCH'])
def edit_office(id):
    data = request.get_json()
    name = data["name"]

    office  = OfficeModel.edit_office(id, name)
    if office:
        return make_response(jsonify({"status": 200,
                                  "data": [
                                      {
                                          "id": id,
                                          "name": name
                                      }
                                  ]
                                  }), 200)
    return make_response(jsonify({"status": 404,
                                  "error": "Party not found"
                                  }), 404)
     

 