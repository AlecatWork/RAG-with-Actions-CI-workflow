

def test_root_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['message'] == 'RAG API is running'


def test_health_returns_expected_fields(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert set(data) == {'chromadb', 'ollama', 'documents'}
    assert data['chromadb'] == 'ok'
    assert data['ollama'] in ('connected', 'unavailable')
    assert isinstance(data['documents'], int)


def test_stats_returns_document_count(client):
    response = client.get('/stats')
    assert response.status_code == 200
    data = response.json()
    assert 'document_count' in data
    assert isinstance(data['document_count'], int)


def test_ask_rejects_empty_question(client):
    response = client.post('/ask', json={'question': ''})
    assert response.status_code == 422


def test_ask_with_empty_database_gives_clear_message(client):
    response = client.post('/ask', json={'question': 'What is shonen?'})
    assert response.status_code == 200
    assert 'No documents have been ingested' in response.json()['answer']

