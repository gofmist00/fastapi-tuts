from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="This is the default route.")
async def root():
    return {"message": "hello world"}
