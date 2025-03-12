from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de la base de datos
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    sector = Column(String)
    text = Column(String)
    result = Column(String)
    emotion = Column(String)
    suicide_probability = Column(Float)

Base.metadata.create_all(bind=engine)

class PredictionRequest(BaseModel):
    name: str
    age: int
    gender: str
    sector: str
    text: str
    result: str = None
    emotion: str = None
    suicide_probability: float = None

@app.post("/predecir")
async def predecir(data: PredictionRequest):
    # Guardar los datos en la base de datos
    db = SessionLocal()
    prediction = Prediction(
        name=data.name,
        age=data.age,
        gender=data.gender,
        sector=data.sector,
        text=data.text,
        result=data.result,
        emotion=data.emotion,
        suicide_probability=data.suicide_probability,
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    db.close()
    
    return {"message": "Data received", "data": data.dict()}
