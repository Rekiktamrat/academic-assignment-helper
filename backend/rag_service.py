import openai
from sqlalchemy.orm import Session
from models import AcademicSource

def search_sources(db: Session, query_embedding):
    return db.query(AcademicSource)\
        .order_by(AcademicSource.embedding.cosine_distance(query_embedding))\
        .limit(3).all()
