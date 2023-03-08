import pymongo
from flask import Flask,render_template, request, session, redirect, jsonify
import os
import socket
from flask_session import Session
import functools
import redis
from flask_cors import CORS, cross_origin

dburl = os.environ.get("MONGOURI","mongodb://mongodbserver:27017/")
# dburl = f""
mongo = pymongo.MongoClient(dburl)
db = mongo["test"]
coll = db["samples"]

app = Flask(__name__)
cors = CORS(app)
app.secret_key="Riuhidsuf8dsn"
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem" #not working in docker cluster
# app.config["SESSION_TYPE"] = "mongodb"
# app.config["SESSION_MONGODB"] = mongo
# app.config["SESSION_MONGODB_DB"] = 'test'
# app.config["SESSION_MONGODB_COLLECTION"] = 'sessions' #flask-session not working with pymongo>4.0
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
redis_server_ip = os.environ.get("REDISIP","redisserver")
app.config['SESSION_REDIS'] = redis.from_url(f"redis://{redis_server_ip}:7000")

Session(app)

# def login_required(func):
#     @functools.wraps(func)
#     def secure_func(*args, **kwargs):
#         if not session.get("username"):
#             return redirect("/login")
#         return func(*args, **kwargs)
    
#     return secure_func

@app.route("/api/")
# @login_required
def index():
    message = f"Host Name : {socket.gethostname()}" 
    return jsonify(message)
    # return render_template("index.html", message=message)

@app.route("/api/search/<string:term>")
# @login_required
def search(term):
    print(term)
    res = coll.find({"title":{"$regex":term, "$options":'i'}},{"_id":0}).limit(10)
    alist = list(res)
    message = ""
    if len(alist) == 0:
        message = f"{term} Not Found"
    return jsonify(alist)
    # return render_template("index.html", alist = alist, message=message)

@app.route("/api/sample")
# @login_required
def sample():
    # res = coll.find({},{"_id":0}).limit(10)
    res = coll.aggregate([{"$sample": {"size": 5}}, {"$project":{"_id":0}}])
    alist = list(res)
    # message = ""
    # if len(alist) == 0:
    #     message = "Not Found"
    return jsonify(alist)
    # return render_template("index.html", alist = alist, message=message)

# @app.route("/id/page")
# @login_required
# def id():    
#     message = f"Host Name : {socket.gethostname()}"    
#     return render_template("index.html", alist = [], message=message)

@app.route("/api/login", methods = ["GET", "POST"])
def login():
    if session.get("username"):
        # return redirect("/")
        status = {"message":"logged in already"}
    if request.method == "POST":
        session['username'] = request.form.get("uname")
        status = {"message":"successfully logged in"}
        # return redirect("/")
    # message = f"Host Name : {socket.gethostname()}"
    return jsonify(status)
    # return render_template("login.html", message=message)

@app.route("/api/logout")
# @login_required
def logout():
    session["username"]=None
    status = {"message":"successfully logged out"}
    return jsonify(status)
    # return redirect("/")

@app.route("/api/id")
@cross_origin()
def api_id():
    hname = { "hostname" : socket.gethostname() }
    return jsonify(hname)

if __name__=="__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
