from fastapi import FastAPI
app = FastAPI()

# models registery
models = [
    {'id':1, 'name':'YOLOv8'},
    {'id':2, 'name':'ResNet'}
]

@app.get("/models")
def get_models():
    return models