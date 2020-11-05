import psutil
   
def test_mac(app,client):
    a = psutil.net_if_addrs()
    b = str(a)
    res = client.get('/mac')
    assert res.status_code == 200
    expected = b
    assert expected == res.get_data(as_text=True)
