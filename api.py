from fastapi import FastAPI
from fastapi import Depends, Query, Path, HTTPException, status, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Socioscope API", version="1.0.0")