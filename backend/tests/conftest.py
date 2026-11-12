import os
import tempfile

os.environ['CHROMA_PATH'] = tempfile.mkdtemp(prefix='rag_test_db_')
os.environ['OLLAMA_URL'] = 'http://127.0.0.1:9'

import pytest
from fastapi.testclient import TestClient

from my_rag_api import app

@pytest.fixture(scope='session')
def client():
    return TestClient(app)