from flask import *
import numpy as np
import pickle
with open('models\svc_linear_model.pkl', 'rb') as file:
  model = pickle.load(file)
app=Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")
def level1():
    return render_template("")
def level2():
    return render_template("")
def level3():
    return render_template("")
def level4():
    return render_template("")
def level5():
    return render_template("")
@app.route('/predict', methods=['POST', 'GET']) 
def predict():
    q1=int(request.form['q1'])
    q2=int(request.form['q2'])
    q3=int(request.form['q3'])
    q4=int(request.form['q4'])
    q5=int(request.form['q5'])
    q6=int(request.form['q6'])
    q7=int(request.form['q7'])
    q8=int(request.form['q8'])
    q9=int(request.form['q9'])
    q10=int(request.form['q10'])
    q11=int(request.form['q11'])
    q12=int(request.form['q12'])
    q13=int(request.form['q13'])
    q14=int(request.form['q14'])
    q15=int(request.form['q15'])
    q16=int(request.form['q16'])
    q17=int(request.form['q17'])
    q18=int(request.form['q18'])
    q19=int(request.form['q19'])
    q20=int(request.form['q20'])
    q21=int(request.form['q21'])
    q22=int(request.form['q22'])
    q23=int(request.form['q23'])
    q24=int(request.form['q24'])
    q25=int(request.form['q25'])
    q26=int(request.form['q26'])
    q27=int(request.form['q27'])
    q28=int(request.form['q28'])
    q29=int(request.form['q29'])
    q30=int(request.form['q30'])
    q31=int(request.form['q31'])
    q32=int(request.form['q32'])
    q33=int(request.form['q33'])
    q34=int(request.form['q34'])
    q35=int(request.form['q35'])
    q36=int(request.form['q36'])
    q37=int(request.form['q37'])
    q38=int(request.form['q38'])
    q39=int(request.form['q39'])
    q40=int(request.form['q40'])
    q41=int(request.form['q41'])
    q42=int(request.form['q42'])
    p1=int(request.form['p1'])
    p2=int(request.form['p2'])
    p3=int(request.form['p3'])
    p4=int(request.form['p4'])
    p5=int(request.form['p5'])
    p6=int(request.form['p6'])
    p7=int(request.form['p7'])
    p8=int(request.form['p8'])
    p9=int(request.form['p9'])
    p10=int(request.form['p10'])
    education=request.form['education']
    residental_area=request.form['residental_area']
    gender=request.form['gender']
    age=request.form['age']
    religion=request.form['religion']
    race=request.form['race']
    marital_status=request.form['marital_status']
    children=request.form['children']
    major=request.form['major']
    lis_q=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33,q34,q35,q36,q37,q38,q39,q40,q41,q42]
    lis_p=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
    lis=[education,residental_area,gender,age,religion,race,marital_status,major]
    l=[]
    l.append(lis_q)
    l.append(lis_p)
    l.append(lis)
    print(l)
    npar=np.array([np.array(item) for item in l])
    res1=model.predict(np.reshape(npar, (-1,61)))
    res=f"your car price is {res1}"
    if res<143:
       redirect(url_for())
    elif res>=143 and res<=157:
       redirect(url_for())
    elif res>=157 and res<=180:
       redirect(url_for())
    elif res>=180 and res<=204:
       redirect(url_for())
    else:
       redirect(url_for())
    return render_template('index.html', result=res)
if __name__=="__main__":
   app.run(debug=True)