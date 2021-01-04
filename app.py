from flask import Flask, request as req, make_response,render_template
app = Flask(__name__)

data={"id":0,"users":[]}

@app.route('/')
def index():
    return render_template("index.html",**data)

@app.route('/new-user',methods=["POST"])
def new():
    users=data["users"]
    users.append({"id":data["id"],"name":req.form["name"],"lastName":req.form["lastName"]})
    data["id"]+=1
    return render_template("index.html",**data)

@app.route('/update-user',methods=["POST"])
def update():
    users=data["users"]
    id=int(req.form["id"])
    user=findById(id)
    user["name"]=req.form["name"]
    user["lastName"]=req.form["lastName"]
    return render_template("index.html",**data)


@app.route('/remove-user',methods=["POST"])
def remove():
    id=int(req.form["id"])
    user=findById(id)
    users=data["users"]
    users.remove(user)
    return render_template("index.html",**data)

@app.route('/remove-all',methods=["GET"])
def removeAll():
    data["users"]=[]
    return render_template("index.html",**data)

def findById(id):
    users=data["users"]
    return list(filter(lambda x:x["id"]==id,users))[0]
