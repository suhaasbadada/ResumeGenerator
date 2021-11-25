from flask import Flask,render_template,request,redirect,url_for
from flask import jsonify
from PIL import Image
import base64
import io

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
global currUser
currUser = ""
global dictt
dictt = {"":""}
global d
d = {"":""}

app = Flask(__name__)
@app.route('/')
def begin():
    return render_template('auth.html')

@app.route('/')
def logout():
    #auth.signOut()
    return render_template('auth.html')

@app.route('/register')
def register():
    return render_template("signup.html")


@app.route('/registered',methods=['POST'])
def successful_registration():
        email = request.form["emailField"]
        password = request.form["pwdField"]
        re_password=request.form["repwdField"]
        name = request.form["nameField"]

        if(email!="" and password!="" and re_password!="" and name!=""):                      

            if(password==re_password):
                initial_dict={}

                initial_dict["name"]=name
                initial_dict["password"]=password
                initial_dict["contact"]=123
                initial_dict["address"]='Area Name,Street Line,Address Line,Landmark,City,Country'
                initial_dict["github"]='https://github.com/abc123'
                initial_dict["linkedin"]='https://www.linkedin.com/in/abc123/'
                initial_dict["email"]=email
                initial_dict["obj"]='obj1;obj2;obj3'
                initial_dict["softskills"]='s1;s2;s3'
                initial_dict["techskills"]='t1;t2;t3'
                initial_dict["aqual"]='aq1;aq2;aq3'
                initial_dict["workexp"]='we1;we2;we3'
                initial_dict["projects"]='p1;p2;p3'
                db.collection(u'users').add(initial_dict)
                return render_template("auth.html")
            else:
                return redirect(url_for('register'))
        else:
            return redirect(url_for('register'))

@app.route('/index',methods=['POST'])
def login():
    r=request.form["btn"]
    if(r=="loginBtn"):
        
        #name = request.form["nameLoginField"]
        try:   
            email = request.form["emailLoginField"]
            password = request.form["passwordLoginField"]
            docs = db.collection('users').get()
            for doc in docs:
                if email == doc.to_dict()['email']:
                    if password == doc.to_dict()['password']:
                        global currUser
                        currUser = doc.id
                        global dictt
                        dictt = db.collection('users').document(currUser).get().to_dict()
                        return render_template('sidebar.html')
            raise Exception("Exc")
        except:
            return render_template("auth.html")
    else:
        return redirect(url_for('register'))
    


@app.route('/index')
def performactions():
    return render_template('sidebar.html')

@app.route('/pick',methods=['POST'])
def choose():
    #dictt.clear()
    dicttt = {"temp":"l"}
    dp=request.files["imgField"]    
    dicttt['name']=request.form["nameField"]
    dicttt["contact"]=request.form["contactField"]
    dicttt['address']=request.form["addressField"]
    dicttt['github']=request.form["gitField"]
    dicttt['linkedin']=request.form["linkedField"]
    dicttt["email"]=request.form["emailField"]
    dicttt["obj"]=request.form["objectiveField"]
    dicttt["softskills"]=request.form["ssField"]
    dicttt["techskills"]=request.form["tsField"]
    dicttt["aqual"]=request.form["aqField"]
    dicttt["workexp"]=request.form["weffield"]
    dicttt["projects"]=request.form["pjField"]

    command=request.form["btnField"]
    db.collection("users").document(currUser).update(dicttt)
    dictt = db.collection('users').document(currUser).get().to_dict()
    global d
    d=dictt.copy()

    return render_template('choose.html',dictt=dictt)


global c
c=0

@app.route('/whatnext',methods=['POST'])
def whatnext():
    global c
    r=request.form["act"]
    if(r=="logout"):
        c=0
        return redirect(url_for('begin'))
    elif(r=="detailsButton"):
        c+=1
        return render_template('index.html',dictt=dictt)
    elif(r=="librButton"):
         return render_template('choose.html',dictt=dictt)        
    elif(r=='homeButton'):
        c+=1
        print(c)
        return redirect(url_for('performactions'))


@app.route('/output',methods=['POST'])
def display():
    
    template=request.form["select"]    
    if(template=="first"):
        if(c==0):
            return render_template('template1.html',dictt=dictt)
        else:
            return render_template('template1.html',dictt=d)
    elif(template=="second"):
        if(c==0):
            return render_template('template2.html',dictt=dictt)
        else:
            return render_template('template2.html',dictt=d)
    elif(template=="third"):
        if(c==0):
            return render_template('template3.html',dictt=dictt)
        else:
            return render_template('template3.html',dictt=d)
    elif(template=="fourth"):
        if(c==0):
            return render_template('template4.html',dictt=dictt)
        else:
            return render_template('template4.html',dictt=d)
    else:
        return render_template('error.html')




