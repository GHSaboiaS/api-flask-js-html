# Postman: create requests for the server's address (http), such as GET and POST
# These requests will call different functions in the backend

from flask import Flask, request

from main import insertUser

app = Flask("API")

@app.route("/hello", methods=["GET"])
def hello():
    return {"hello": "world"}

@app.route("/addUser", methods=["POST"])
def addUser():
    body = request.get_json()

    if ("name" not in body):
        return {"status": 400, "mensagem": "parameter 'name' is needed"}

    user = insertUser(body["name"], body["email"], body["password"])
    return genResponse(200, "user created", "user", user)

# this function will generate response from server when user is added
def genResponse(status, message, contentName=False, content=False):
    response = {}
    response["status"] = status
    response["message"] = message

    if (contentName and content):
        response["contentName"] = content

    return response

app.run()