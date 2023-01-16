from fastapi import FastAPI


app = FastAPI()


def home():
    return 'Hello There!'