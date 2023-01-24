from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!!"


users = [
    {
        "user_id": "user1",
        "username": "fsdskkd"
    },
    {
        "user_id": "user2",
        "username": "fsdskk2"
    }
]


@app.route("/get_user_ids")
def get_user_ids():
    ids = {"idList": []}

    for user in users:
        ids["idList"].append(user["user_id"])
    return ids


@app.route("/get_user_name")
def get_user_name():
    name = {"nameList": []}

    for user in users:
        name["nameList"].append(user["username"])
    return name


# Creat an endpoint to fetch all the user sids and show it in a dictionary

# Creat an endpoint to fetch all the usernames and show it in a dictionary


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)
