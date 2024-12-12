# app/main.py

from fastapi import FastAPI

# Create FastAPI instance (main entry point of your application)
app = FastAPI()

# Example Route: Root route (just a simple test route)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Tourism API"}

# You can add more routes here later for specific features.
