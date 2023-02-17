# Import the necessary modules and packages for the application
import pymongo # For connecting to MongoDB
from fastapi.responses import HTMLResponse # For returning an HTML response
from fastapi.templating import Jinja2Templates  # For rendering HTML templates with Jinja2
from pydantic import BaseModel  # For creating models for request and response data
from pymongo import MongoClient  # For connecting to MongoDB
from fastapi import FastAPI, Form, Request # For creating the FastAPI application and handling requests
from passlib.context import CryptContext # For password hashing and verification
from router import router



app = FastAPI()
# Create an instance of the Jinja2Templates class
app.include_router(router.router)

# app.include_models(models.models)

