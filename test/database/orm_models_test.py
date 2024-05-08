from datetime import datetime, timedelta
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ai_core.database.orm_models import LLM, TrainingHistory, Dataset, Base

# Setup test database and session
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


def test_multiple_traininghistory_to_one_llm():
    # Creating an LLM instance
    llm = LLM(name="LLM Model", source="Source", storage_path="/path/to/llm")
    session.add(llm)
    session.commit()

    # Creating multiple TrainingHistory instances linked to the LLM
    th1 = TrainingHistory(
        llm_id=llm.llm_id, dataset_id=1
    )  # assuming dataset_id=1 exists
    th2 = TrainingHistory(
        llm_id=llm.llm_id, dataset_id=2
    )  # assuming dataset_id=2 exists
    session.add_all([th1, th2])
    session.commit()

    # Retrieving to check correct relationship
    retrieved_llm = session.query(LLM).filter_by(name="LLM Model").first()
    assert len(retrieved_llm.training_history) == 2


def test_one_traininghistory_per_dataset():
    # Creating Dataset instances
    dataset1 = Dataset(
        name="Dataset 1", details="Details 1", storage_path="/path/dataset1"
    )
    session.add(dataset1)
    session.commit()

    # Creating TrainingHistory instance linked to the Dataset
    th1 = TrainingHistory(
        llm_id=1, dataset_id=dataset1.dataset_id
    )  # assuming llm_id=1 exists
    session.add(th1)
    session.commit()

    # Retrieving to ensure only one TrainingHistory per Dataset
    retrieved_dataset = session.query(Dataset).filter_by(name="Dataset 1").first()
    assert retrieved_dataset.training_history is not None
    assert (
        retrieved_dataset.training_history[0].training_history_id
        == th1.training_history_id
    )

    # Trying to add another TrainingHistory to the same Dataset should be handled by your logic or constraints
