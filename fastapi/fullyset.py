from fastapi import FastAPI
app = FastAPI()

models = [
    {'id':1, 'name':'YOLOv8'},
    {'id':2, 'name':'Resnet'}
]

@app.get("/models")
def get_models():
    return models

@app.post("models")
def add_model(model : dict):
    models.append(model)
    return {"message": "Model added", "data": model}

@app.put("/models/{model_id}")
def update_model(model_id: int, model: dict):
    for m in models:
        if m["id"]== model_id:
            m['name'] == model["name"]
            return {"message": "model Update", "data": m}
    return {"error": "Model not found"}