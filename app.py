from flask import Flask
from flasgger import Swagger, LazyJSONEncoder
from flasgger import swag_from

from swagger_t_c import swagger_template as ST
from swagger_t_c import swagger_config as SC

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

swagger = Swagger(app, template=ST, config=SC)

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello World!!!"

if __name__ == '__main__':
    app.run()