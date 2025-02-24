from flask import Flask, jsonify, request
import person_dao
persons = person_dao.Db_operations()

create_table_flights()

app = Flask(__name__)

@app.route('/persons',methods=['POST'])
def persons_create():
    body = request.get_json()
    new_person = person_dao.Person(body['name'], body['gender'], body['dob'], body['location'])
    id = persons.insert_row(new_person)
    person = persons.search_row(id)
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}
    return jsonify(person_dict)

@app.route('/new_persons/<id>',methods=['GET'])
def persons_read_by_id(id):
    person = search_row(id)
    print(person)
    print(type(person))
    if person == None:
        return jsonify("person not found")
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}    
    return jsonify(person_dict)

@app.route('/persons',methods=['GET'])
def persons_read_all():
    person = list_persons()
    person_dict = []
    for person in persons:
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}    
    return jsonify(person_dict)

@app.route('/flights/<id>',methods=['PUT'])
def flights_update(id):
    body = request.get_json()
    old_flight = search_flight(id)
    if not old_flight:
        return jsonify({'message': 'Flight not found'})
    old_flight.airline = body['airline']
    old_flight.source = body['source']
    old_flight.destination = body['destination']
    old_flight.duration = body['duration']
    old_flight.fare = body['fare']
    id = body['id']
    update_flight(old_flight, id)
    flight = search_flight(id)
    person_dict = {'id':person.id, 'name':person.name, 'gender':person.gender, 'dob':person.dob, 'location': person.location}    
    return jsonify(person_dict)

@app.route('/flights/<id>',methods=['DELETE'])
def flights_delete(id):
    old_flight = search_flight(id)
    if not old_flight:
        return jsonify({'message': 'Flight not found', 'is_error': 1})
    delete_flight(id)
    return jsonify({'message': 'Flight is deleted', 'is_error': 0})

app.run(debug=True)