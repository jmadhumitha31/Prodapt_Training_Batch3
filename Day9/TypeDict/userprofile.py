from typing import List, Optional, TypedDict
class UserProfile(TypedDict):
    id:int
    name:str
    email:str
    bio:Optional[str]

def format_user_profile(user:List[UserProfile]) -> List:
    return [f"{u['name']} ({u['email']})" for u in user]

user=[
    {"id":1,
     "name":"Alice",
     "email":"alice@example.com",
     "bio":"Software Engineer"},

    {
        "id":2,
        "name":"Bob",
        "email":"bob@example.com",
        "bio":None
    }
]
print(format_user_profile(user))