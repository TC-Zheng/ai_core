import pytest
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.ext.asyncio import AsyncSession

from ai_core.data_access.unit_of_work import UnitOfWork


@pytest.fixture
def mock_session():
    # Creates a mock AsyncSession
    session = AsyncMock(spec=AsyncSession)
    return session


@pytest.mark.asyncio
async def test_commit(mock_session):
    """Test the UnitOfWork commits successfully when no exceptions occur."""
    # Arrange
    uow = UnitOfWork(session=mock_session)

    # Act
    async with uow:
        pass  # simulate doing some operations

    # Assert
    mock_session.commit.assert_awaited_once()
    mock_session.rollback.assert_not_called()
    mock_session.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_exception_in_uow(mock_session):
    """Test the UnitOfWork performs a rollback on exception inside uow."""
    # Arrange
    uow = UnitOfWork(session=mock_session)

    # Act
    with pytest.raises(Exception) as e:
        async with uow:
            raise Exception("Test Error")

    # Assert
    assert str(e.value) == "Test Error"
    mock_session.rollback.assert_awaited_once()
    mock_session.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_exception_when_commit(mock_session):
    """Test the UnitOfWork performs a rollback on exception during commit."""
    # Arrange
    uow = UnitOfWork(session=mock_session)
    mock_session.commit.side_effect = Exception("DB Error")  # Force an exception

    # Act
    with pytest.raises(Exception) as e:
        async with uow:
            pass

    # Assert
    assert str(e.value) == "DB Error"
    mock_session.rollback.assert_awaited_once()
    mock_session.close.assert_awaited_once()
