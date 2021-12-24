from flask import Flask,request
from producer.producer import file_Produceres
app = Flask(__name__)

@app.route('/<string:value>',methods=['GET'])
def create_file(value):
    file_Produceres().create_file(value)
    return {'message': 'file created'}


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0',debug=True)