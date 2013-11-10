from flask import Flask
from flask.ext.restful import Api, Resource

app = Flask(__name__, static_url_path='')
api = Api(app)


class MovieLocationApi(Resource):

    def get(self, location):
        return {'location': location}

api.add_resource(MovieLocationApi, '/search/<string:location>')


@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
