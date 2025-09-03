import psutil
import speedtest
import math

# cpus = psutil.cpu_count()
print(psutil.cpu_count())
print(psutil.cpu_percent(1))
# while (1):
#     print(psutil.cpu_percent(1))
print("Total System Memory",math.floor(psutil.virtual_memory()[0]/100000000))
print("Available Memory",math.floor(psutil.virtual_memory()[1]/100000000))
print("Percentage Memory used",math.floor(psutil.virtual_memory()[2]))
print("Used memory is: ",math.floor(psutil.virtual_memory()[3]/100000000))
print("Free memory is: ",math.floor(psutil.virtual_memory()[4]/100000000))

## Getting the Network Speed
st = speedtest.Speedtest()
print("Download Speed :",math.floor(st.download()/100000000))
print("Upload Speed :",math.floor(st.upload()//100000000))
print("Ping is :",st.results.ping)