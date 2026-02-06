from fastapi import FastAPI

app = FastAPI(title="Daily Growth OS")

@app.get("/")
def health_check():
    return {"status": "Backend running"}