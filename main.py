from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Render"}

if _name_ == "_main_":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    print("🚀 Running on port", port)

    uvicorn.run("test_api:app", host="0.0.0.0",port=port)
