from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint #

app = Flask(__name__)
api = Api(app)

# Default Route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Enable Swagger UI
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "My Flask REST API"
    },
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):

    # GET: Retrieve data from the server without modifying it.
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    # DELETE: Remove a resource from the server.
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    # PUT: Update an existing resource on the server or create a new one if it doesn't exist.
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# Shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):

    # GET: Retrieve data from the server without modifying it.
    def get(self):
        return TODOS

    # POST: Submit data to the server to create a new resource.
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

# Setup the Api resource routing

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)