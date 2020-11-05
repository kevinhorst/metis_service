from app import app
import psutil
from psutil._common import bytes2human
@app.route('/')

@app.route('/index')

def index():
    return 'Welcome to the metis API!'

@app.route('/cpu')


def cpu():
    a = psutil.cpu_percent(percpu=True)  #returns the current CPU usage as float
    b = psutil.cpu_count(logical=False)  #returns the number of CPUs
    usage = str(a)
    number = str(b)
    return 'number of CPUs: ' + number + 'current CPU utilization: ' + usage

@app.route('/ram')

def ram():
    mem = psutil.virtual_memory()   #returns the current RAM usage as a named tupel
    total = str(bytes2human(mem.total)) #total physical memory
    available = str(bytes2human(mem.available))#the memory that can be given instantly to process without the system going into swap
    active = str(bytes2human(mem.active)) #memory currently in use
    inactive = str(bytes2human(mem.inactive)) #memory marked as not used
    return 'total memory: ' + total + '; ' + 'available memory: ' + available + '; ' + ' active memory: ' + active + '; '+ 'inactive memory: ' + inactive

@app.route('/disk')

def disk():
    result =""
    for part in psutil.disk_partitions(all=False): #iterates over all devices, prefers physical devices
        usage = psutil.disk_usage(part.mountpoint)
        device = part.device
        totalusage = bytes2human(usage.total) #total space
        usedusage = bytes2human(usage.used) #used space
        freeusage = bytes2human(usage.free) #free space
        percent = int(usage.percent)        #percentage
        cache = 'device: ' + str(device)+ '; total space: ' + str(totalusage) + '; used space: '+ str(usedusage) + '; free space: ' + str(freeusage) + '; percentage used: ' + str(percent) + "; "
        result = result + cache
    return result

@app.route('/inet4')

def inet4():
    a = psutil.net_connections("inet4") # returns system-wide socket connections as list of named tupels
    b = str(a)
    return b

@app.route('/inet6')

def inet6():
    a = psutil.net_connections("inet6") # returns system-wide socket connections as list of named tupels
    b = str(a)
    return b

@app.route('/mac') #return the addreses associated to each Network interface card

def mac():
    a = psutil.net_if_addrs()
    b = str(a)
    return b
