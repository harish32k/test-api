from flask_restful import Resource, reqparse
from db import query

class Dept(Resource):

    #defined get method for Dept resource/endpoint
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deptno', type=int, required=True,
                            help="deptno cannot be left blank!")
        data = parser.parse_args()
        print(data)
        try:
            return query(f"""SELECT * FROM testapi.dept WHERE deptno={data['deptno']}""")
        except:
            return {"message": "There was an error connecting to dept table."}, 500

    #defined post method for Dept resource/endpoint
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('deptno', type=int, required=True,
                            help="deptno cannot be left blank!")
        parser.add_argument('dname', type=str, required=True,
                            help="dname cannot be left blank!")
        parser.add_argument('loc', type=str, required=True,
                            help="loc cannot be left blank!")
        data = parser.parse_args()
        try:
            x = query(
                f"""SELECT * FROM testapi.dept WHERE deptno={data['deptno']}""", return_json=False)
            if len(x) > 0:
                return {"message": "A dept with that deptno already exists."}, 400
        except:
            return {"message": "There was an error inserting into dept table."}, 500


        try:
            query(f"""INSERT INTO testapi.dept VALUES({data['deptno']},
                                                    '{data['dname']}',
                                                    '{data['loc']}')""")
        except:
            return {"message": "There was an error inserting into dept table."}, 500
        return {"message": "Successfully Inserted."}, 201