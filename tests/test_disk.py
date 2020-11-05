import psutil
from psutil._common import bytes2human
   
def test_disk(app,client):
    result =""
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        device = part.device
        totalusage = bytes2human(usage.total)
        usedusage = bytes2human(usage.used)
        freeusage = bytes2human(usage.free)
        percent = int(usage.percent)
        cache = 'device: ' + str(device)+ '; total space: ' + str(totalusage) + '; used space: '+ str(usedusage) + '; free space: ' + str(freeusage) + '; percentage used: ' + str(percent) + "; "
        result = result + cache
    res = client.get('/disk')
    assert res.status_code == 200
    expected = result
    assert expected == res.get_data(as_text=True)
