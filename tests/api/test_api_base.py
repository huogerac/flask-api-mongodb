def test_obter_status(client):
    resp = client.get("/api/status")

    assert resp.status_code == 200
    assert resp.json == {
        "debug": False,
        "env": "tests",
        "status": "ok",
    }


def test_swagger_docs(client):
    """Test the docs is working"""
    response = client.get("/openapi/rapidoc")

    assert response.status_code == 200
