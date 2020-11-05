import psutil
   
def test_ip6(app,client):
    a = psutil.net_connections("inet6")
    b = str(a)
    res = client.get('/inet6')
    assert res.status_code == 200
    expected = b
    assert expected == res.get_data(as_text=True)
