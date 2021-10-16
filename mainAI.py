

from flask import Flask, request, jsonify
from flask_cors import CORS
from DCGSModel import DCGSModel


# init
app = Flask(__name__)
CORS(app)
dcgs_model_obj = DCGSModel(Adult_or_Junior='Adult')



@app.route('/dcgs20api_post', methods=['POST'])
def DCGSServicePost():
    insertValues = request.get_json()
    StartDate = insertValues['StartDate']
    Stage = insertValues['Stage']
    if Stage == 'first':
        # lauch dcgs 2.0 model
        dcgs_model_obj.main()
        return jsonify({'return': 'Success(StartDate:{})'.format(StartDate)})
    elif Stage == 'second':
        # call output of dcgs 2.0
        scheduling_classroom = dcgs_model_obj.scheduling_classroom
        if scheduling_classroom is None:
            return jsonify({'return': 'Fail(Model)(StartDate:{})'.format(StartDate)})
        else:
            return jsonify({'return' : scheduling_classroom})
    else:
        return jsonify({'return': 'Fail(Stage)(StartDate:{})'.format(StartDate)})
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)