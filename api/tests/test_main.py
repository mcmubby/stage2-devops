import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

client = TestClient(app)

@patch('main.r')
def test_create_job(mock_redis):
    # Mock the return values for Redis commands if necessary
    # lpush and hset return integers usually, but we don't use their return values in create_job
    mock_redis.lpush.return_value = 1
    mock_redis.hset.return_value = 1
    
    response = client.post("/jobs")
    
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data
    assert len(data["job_id"]) > 0
    assert mock_redis.lpush.called
    assert mock_redis.hset.called


@patch('main.r')
def test_get_job_found(mock_redis):
    # Mock hget to return a status (bytes)
    mock_redis.hget.return_value = b"completed"
    
    job_id = "test-job-id"
    response = client.get(f"/jobs/{job_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["job_id"] == job_id
    assert data["status"] == "completed"
    mock_redis.hget.assert_called_with(f"job:{job_id}", "status")


@patch('main.r')
def test_get_job_not_found(mock_redis):
    # Mock hget to return None, simulating not found
    mock_redis.hget.return_value = None
    
    job_id = "non-existent-id"
    response = client.get(f"/jobs/{job_id}")
    
    assert response.status_code == 200
    data = response.json()
    assert "error" in data
    assert data["error"] == "not found"
    mock_redis.hget.assert_called_with(f"job:{job_id}", "status")
