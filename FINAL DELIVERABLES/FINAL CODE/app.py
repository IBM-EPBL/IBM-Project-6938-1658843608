from flask import Flask, request,render_template

app = Flask(__name__)



import pickle
model = pickle.load(open('model.pkl','rb'))


app=Flask(__name__)

@app.route('/')
def predict():
    return render_template("index.html")

@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test=[[float(x) for x in request.form.values()]]
    print('actual',x_test)
    pred=model.predict(x_test)

    return render_template("index.html",\
                           prediction_text=("Car fuel Consumption(L/100km)\
                                            :",pred[0]))

if __name__=='__main__':
    app.run(debug= False)
    
