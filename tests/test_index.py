def test_index(app,client):
    res = client.get('/')
    assert res.status_code == 200
    expected = 'Welcome to the metis API!'
    assert expected == res.get_data(as_text=True)
