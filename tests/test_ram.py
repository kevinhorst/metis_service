import psutil
from psutil._common import bytes2human
   
def test_ram(app,client):
    mem = psutil.virtual_memory()
    total = str(bytes2human(mem.total))
    available = str(bytes2human(mem.available))
    active = str(bytes2human(mem.active))
    inactive = str(bytes2human(mem.inactive))

    res = client.get('/ram')
    assert res.status_code == 200
    expected = 'total memory: ' + total + '; ' + 'available memory: ' + available + '; ' + ' active memory: ' + active + '; '+ 'inactive memory: ' + inactive
    assert expected == res.get_data(as_text=True)
