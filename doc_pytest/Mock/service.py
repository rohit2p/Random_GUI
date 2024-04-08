import requests

database = {
    1 : "Rohit",
    2 : "Ram"
}

def get_user_from_id(user_id):
    # return print(database.get(user_id))
    return database.get(user_id)
# get_user_from_id(2)

def get_user_through_api():
    responce = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if responce.status_code == 200:
        return responce.json()

    raise requests.HTTPError