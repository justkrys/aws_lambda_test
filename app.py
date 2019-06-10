import json

import numpy as np
import pandas as pd
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


@app.route('/')
def root():
    return 'Hello World!'


@api.resource('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}


@api.resource('/data')
class Data(Resource):
    def get(self):
        dates = pd.date_range('20130101', periods=6)
        df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list(
            'ABCD'))
        return json.loads(df.to_json(orient='records'))


if __name__ == '__main__':
    app.run()

