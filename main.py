from flask import Flask


from flask import Flask, request,jsonify

app = Flask(__name__)


@app.route('/via_postman', methods = ['GET','POST'])
def math_operation_via_postman():
    if request.method == 'POST':
        operation=str(request.json['operation'])
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result = ' the sum of '+str(num1)+' and '+str(num2)+' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = ' the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = ' the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = ' the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    return result


# @app.route('/', methods=['GET','POST'])
# def index():
#     return 'starting ML Project'
#
if __name__ =='__main__':
    app.run(debug = True)