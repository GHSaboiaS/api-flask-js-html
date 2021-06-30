# Postman: create requests for the server's address (http), such as GET and POST
# These requests will call different functions in the backend

from flask import Flask, request
from main import insertUser

# create application backend
app = Flask("API")

# define "hello" route, which uses method GET and calls function hello()
@app.route("/hello", methods=["GET"])
def hello():
    return {"hello": "world"}

# define "addUser" route, which uses method POST and calls function addUser()
@app.route("/addUser", methods=["POST"])
def addUser():
    # store user info in body
    body = request.get_json()

    # check if all parameters have been specified in the request
    if ("name" not in body):
        return {"status": 400, "message": "parameter 'name' is needed"}
    if ("email" not in body):
        return {"status": 400, "message": "parameter 'email' is needed"}
    if ("password" not in body):
        return {"status": 400, "message": "parameter 'password' is needed"}

    # call insertUser function passing all arguments sent by user
    user = insertUser(body["name"], body["email"], body["password"])
    # call genResponse function, passing "user" as content
    return genResponse(200, "user created", "user", user)

# function will generate response from server
def genResponse(status, message, contentName=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if (contentName and content):
        response[contentName] = content

    return response

app.run()