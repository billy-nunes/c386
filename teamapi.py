from fastapi import FastAPI, Response, Request, Body
app = FastAPI()

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.post('/active_users')
async def active_users(session: UserSession):
    users = []
    keys = cache.keys() # get all keys
    for k in keys:
        k = k.decode('utf-8') # make bytes into string
        # the keys with usernames look like "admin-sessionid"
        if "-sessionid" in k: #
            users.append(k.replace("-sessionid", "")) # append only the username
        
    return {"active-users": users}





@app.post("/active_users")
async def do_active_user(
    response: Response,
    session: UserSession):
    
    if not authorize(session.uname, session.sessionid, ["admin"]): 
        return [{"msg":"not authorized"}]

    users = []
    keys = cache.keys() # get all keys
    for k in keys:
        k = k.decode('utf-8') # make bytes into string
        # the keys with usernames look like "admin-sessionid"
        if "-sessionid" in k: 
            users.append(k.replace("-sessionid", "")) # append only the username

    return { "active-users" : users }