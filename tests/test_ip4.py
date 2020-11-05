import psutil
   
def test_ip4(app,client):
    a = psutil.net_connections("inet4")
    b = str(a)
    res = client.get('/inet4')
    assert res.status_code == 200
    expected = b
    assert expected == res.get_data(as_text=True)
