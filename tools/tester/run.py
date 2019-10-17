# path
import sys
sys.path.append(".\\robot")
sys.path.append(".\\gen_protocol")

from login_test_robot import LoginRobot

# config
tab_config = [
    ['39.96.244.26', 7000, 1],  # linux
    ['192.168.44.101', 6380, 2004],  # mine
    ['192.168.44.47', 6380, 2015],  # wenjun
    ['192.168.44.11', 6380, 2010],  # Debian
]
idx = 0

data = {}
data['id'] = 1
data['name'] = 'robot1'
data['server_id'] = tab_config[idx][2]
data['channel'] = '425800000'
data['region'] = 1

#
thread_num = 500
name = 'bot'


def main():
    threads = []

    for i in range(0, thread_num):
        #
        data['name'] = name + str(i)
        data['id'] = str(i)

        #
        r = LoginRobot(tab_config[idx][0], tab_config[idx][1], data)
        threads.append(r)

    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    print "Thread num %d all over!" % thread_num


if __name__ == "__main__":
    main()
