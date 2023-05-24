from flask import Flask,render_template,request
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
sc = StandardScaler()
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt




# import seaborn as sns
# %matplotlib inline

app=Flask(__name__)
app.config['DEBUG'] = True
with open('logistic_model','rb') as m:
    model=pickle.load(m)
result=''


@app.route('/',methods=['GET','POST'])
def hello():
    print('ex')
    
   
    if request.method=='POST' :
        print('hello')
        result=''
        ip1 = request.form.get("ip1")
        ip2 = request.form.get("ip2")
        ip3 = request.form.get("ip3")
        ip4 = request.form.get("ip4")
        ip5 = request.form.get("Gender")
        if(ip5=='Male'):
            ip5=1
        if(ip5=='Female'):
            ip5=0
        print(ip1)
        print(ip2)
        print(ip3)
        print(ip4)
        print(ip5)
        data=[[ip1,ip2,ip3,ip4,ip5]]
        data= np.asarray(data, dtype = 'int')
        print(data)

        output=model.predict(data)
        if output==0:
            result='User will Not click on Ad 😏'
        if output==1:
            result='User will click on Ad 😎'
        print(output)
        print(result)
        return render_template('index.html',result=result)

    return render_template('index.html')

# @app.route('/prediction',methods=['POST'])
# def pred():
#     print('in pred')
#     return render_template('prediction.html',result=result)

if __name__=='__main__':
    app.run()