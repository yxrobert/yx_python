#! /usr/bin/env pythontools
#coding=utf-8

import os.path

file_dir = "./log_filter"
filter_name = 'Notice'
# redis_log = "redis statistics cmd="
check_redis_lv = 5
check_mem_get_lv = 5
check_mem_mget_lv = 5


table_record = {}
table_record_count = {}



def process_map(name, val):
    if table_record.has_key(name):
        if table_record[name] < val:
            table_record[name] = val
    else:
        table_record[name] = val


def process_map_count(name):
    if table_record_count.has_key(name):
        table_record_count[name] += 1
    else:
        table_record_count[name] = 0


# def process_line(line):
#   idx = line.find(redis_log)
#   idx_head = line.find(']')
#   if idx != -1:
#       head = line.find('=')
#       if head != -1:
#           val = int(line[head + 1: ])
#           if val > check_lv:
#               table_name = line[idx_head + 2 : idx]
#               process_map(table_name, val)
#               return line
#   return "" 


def get_head_str(line):
    # Pktsc_get_land_info
    head_begin = line.find(']') + 2
    head_end = line[head_begin : ].find(" ")
    return line[head_begin : head_begin + head_end]


def check_redis(line, key):
    head_str = get_head_str(line)
    val_key = 'cmd='
    head = line.find(val_key)
    if head != -1:
        val = int(line[head + len(val_key): ])
        if val > check_redis_lv:
            head_str += ':' + key + ':' + val_key
            process_map(head_str, val)
            return line
    return "" 

def filter_val(line, lstr, rstr):
    left = line.find(lstr)
    if left > 0:
        left += len(lstr)
        right = line[left : ].find(rstr)
        if right > 0:
            return line[left : left + right]
    return ""

def filter_date(line):
    pass



check_enter = "-------------------GameStatistics:---------------"
check_door = "\n"

check_line = ["process_one_event_type=", "Pktsc_"]

table_map = {}

class CData(object):
    def __init__(self, name):
        self.name = name
        self.calltimes = 0
    
    def Calltimes(self, val):
        self.calltimes = max(val, self.calltimes)

    def __repr__(self):
        return "%s:calltimes:%d" % (self.name, self.calltimes)


def store_data(key, val):
    if table_map.has_key(key):
        table_map[key].Calltimes(val)
    else:
        n = CData(key)
        n.calltimes = val
        table_map[key] = n


def process_data(line, key):
    name = key + filter_val(line, key, ":")
    val = int(filter_val(line, "calltimes=", ","))
    store_data(name, val)


def process_line(line):
    for k in check_line:
        # print(k)
        # print(line)
        if line.find(k) > 0:
            process_data(line, k)


def process_file(fname):
    b_in_zone = False
    f_tab = {}
    with open(fname, 'r') as f:
        line = f.readline()
        while line:
            if line.find(check_enter) > 0:
                b_in_zone = True
            elif line[0] == check_door:
                b_in_zone = False
                # break

            if b_in_zone:
                log = process_line(line)

            # break
            line = f.readline()


def relload(file):
    line = file.readline()
    while line:
        t = line.strip().split(":")
        store_data(t[0], int(t[2]))
        line = file.readline()


def main():
    with open(filter_name + '_all_filter.txt', 'r') as f:
        relload(f)

    with open(filter_name + '_all_filter.txt', 'w') as f_save:
        # print(file_dir)
        for parent, dirnames, filenames in os.walk(file_dir):
            for filename in filenames:
                if filename.find(filter_name) != -1:
                    fname = os.path.join(parent,filename)
                    process_file(fname)
                    # print(fname)
                    # break
                    # 
        for i in table_map:
            f_save.write(str(table_map[i]))
            f_save.write("\n")


if __name__ == '__main__':
    main()
