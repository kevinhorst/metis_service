import psutil

def test_cpu(app,client):

    a = psutil.cpu_percent(percpu=True)  
    b = psutil.cpu_count(logical=False) 
    usage = str(a)
    number = str(b)

    res = client.get('/cpu')
    assert res.status_code == 200
    expected = 'number of CPUs: ' + number + 'current CPU utilization: ' + usage
    assert expected == res.get_data(as_text=True)
