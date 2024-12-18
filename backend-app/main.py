import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis

load_dotenv()

REDIS_URI = os.getenv("REDIS_URI")

client = Redis.from_url(REDIS_URI, decode_responses=True)
client.ping()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    hits = client.incr("hits")
    return {"hits": hits}