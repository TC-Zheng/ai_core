from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime



Base = declarative_base()

class LLM(Base):
    __tablename__ = 'llm'
    llm_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    source = Column(String, nullable=False)  # E.g., 'HuggingFace'
    storage_path = Column(String, nullable=False)
    training_history = relationship('TrainingHistory', back_populates='llm')

class TrainingHistory(Base):
    __tablename__ = 'training_history'
    training_history_id = Column(Integer, primary_key=True)
    llm_id = Column(Integer, ForeignKey('llms.id'))
    dataset_id = Column(Integer, ForeignKey('datasets.id'))
    trained_on = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    llm = relationship('LLM', back_populates='training_history')
    dataset = relationship('Dataset', back_populates='training_history')

class Dataset(Base):
    __tablename__ = 'dataset'
    dataset_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    details = Column(String, nullable=False)  # Additional details about the dataset
    storage_path = Column(String, nullable=False)
    training_history = relationship('TrainingHistory', back_populates='dataset')

