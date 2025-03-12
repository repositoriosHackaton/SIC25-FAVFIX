from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import func
from datetime import datetime, timedelta

app = FastAPI()

# Configuración de CORS (como antes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de la base de datos (como antes)
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
    timestamp = Column(DateTime, default=datetime.utcnow)  # Add timestamp

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

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/predecir")
async def predecir(data: PredictionRequest, db: Session = Depends(get_db)):
    # Guardar los datos en la base de datos
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

    return {"message": "Data received", "data": data.dict()}

class EmotionData(BaseModel):
    emotion: str
    count: int
    time: datetime

@app.get("/emotions_over_time", response_model=list[EmotionData])
async def get_emotions_over_time(time_interval: int = 60, db: Session = Depends(get_db)):  # time_interval in minutes
    """
    Retrieves emotion data aggregated over a specified time interval.
    """
    time_threshold = datetime.utcnow() - timedelta(minutes=time_interval)

    # Query to count emotions within the time interval
    emotions_data = db.query(
        Prediction.emotion,
        func.count(Prediction.emotion),
        func.strftime('%Y-%m-%d %H:%M:00', Prediction.timestamp)  # Truncate to minute
    ).filter(Prediction.timestamp >= time_threshold).group_by(
        Prediction.emotion,
        func.strftime('%Y-%m-%d %H:%M', Prediction.timestamp)  # Group by minute
    ).all()

    # Format the results
    result = []
    for emotion, count, time in emotions_data:
        result.append({"emotion": emotion, "count": count, "time": datetime.strptime(time, '%Y-%m-%d %H:%M:%S')})

    return result

class SectorSentiment(BaseModel):
    sector: str
    average_suicide_probability: float
    time: datetime

@app.get("/sentiment_by_sector", response_model=List[SectorSentiment])
async def get_sentiment_by_sector(time_interval: int = 60, db: Session = Depends(get_db)):
    """
    Retrieves the average sentiment (suicide probability) by sector over a specified time interval.
    """
    time_threshold = datetime.utcnow() - timedelta(minutes=time_interval)

    # Query to calculate the average suicide probability by sector
    sector_sentiment_data = db.query(
        Prediction.sector,
        func.avg(Prediction.suicide_probability),
        func.strftime('%Y-%m-%d %H:%M:00', Prediction.timestamp)  # Truncate to minute
    ).filter(Prediction.timestamp >= time_threshold).group_by(
        Prediction.sector,
        func.strftime('%Y-%m-%d %H:%M', Prediction.timestamp)  # Group by minute
    ).all()

    # Format the results
    result = []
    for sector, avg_sentiment, time in sector_sentiment_data:
        result.append({
            "sector": sector,
            "average_suicide_probability": avg_sentiment,
            "time": datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        })

    return result