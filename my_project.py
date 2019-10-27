import psutil
import json
import time
import datetime

filename = "config.json"
with open(filename) as config_file:
    config = json.load(config_file)
    output = config["output"]
    interval = config["interval"]
    print("output = ", output)
    print('interval = ', interval)


class SystemData():
    """Overall system data"""

    def cpu(self):
        """Return a float representing the current system-wide CPU
        utilization as a percentage.
        Interval 0.5 second in this case"""
        return psutil.cpu_percent(interval=0.5)

    def memory_used(self):
        """Return statistics about system memory usage"""
        return psutil.virtual_memory().used

    def disk(self):
        """Return disk usage statistics about the partition"""
        return psutil.disk_usage('/')

    def network(self):
        """Return system-wide network I/O statistics"""
        return psutil.net_io_counters()


count_of_interval = 0
date = datetime.datetime.now()
my_class = SystemData()
ecount = 1
my_list = []
if "txt" in output:
    while count_of_interval < interval:
        with open("out_of_data.txt", "a") as out:
            out.write(
                'SNAPSHOT{0}: {1} : '
                'cpu = {2} '
                'memory = {3} '
                'disk = {4} '
                'network = {5} '.format(ecount, date, my_class.cpu(),
                                        my_class.memory_used(), my_class.disk(),
                                        my_class.network()) + '\n')
        count_of_interval += 1
        ecount += 1
    time.sleep(1)
elif "json" in output:
    while count_of_interval < interval:
        my_list = {'SNAPSHOT': str(ecount),
                   'date = ': str(date),
                   'cpu = ': str(my_class.cpu()),
                   'memory = ': str(my_class.memory_used()),
                   'disk = ': str(my_class.disk()),
                   'network = ': str(my_class.network())}
        with open("out_of_data.json", "a") as out:
            json.dump(my_list, out)
            out.write('\n')
        count_of_interval += 1
        ecount += 1
