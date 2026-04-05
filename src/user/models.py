

def user_entity(user) -> dict:
    return {
        "id" : str(user["_id"]),
        "name" : str(user["name"]),
        "email" : str(user["email"])
    }