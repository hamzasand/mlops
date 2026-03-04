from fastapi import FastAPI
app = FastAPI()

users = [
    {
    'id': 1,
     'name': "Hamza",
     'Skills': ["python","ML","DL"]
     },

     {
    'id': 2 ,
     'name': "Rizwan",
     'Skills': ["python","ML","DL"]
     }

]

@app.get('/')
def root():
    return {'message':"FastAPI is running"}

@app.get('/users')
def getusers():
    return {"users": users}