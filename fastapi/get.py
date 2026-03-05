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

@app.post("/add_model")
def add_model(model: dict):
    models.append(model)
    return{"message": "Model added", "data": model}