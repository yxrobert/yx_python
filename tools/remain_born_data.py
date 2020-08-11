#! /usr/bin/env python
#coding=utf-8


import os, sys

keys = ['server_logic_redis_ip'
    , 'server_logic_redis_port'
    , 'server_logic_redis_password'
    , 'enable_active_code'
    , 'server-serial-number']

val_table = {}
config_file = './loc.conf'

out_file = 'born_data.loc'
code_file = 'active.code'
tmp_out_file = 'tmp_' + out_file

def parse_file(fileName):
    configFile = open(fileName, 'r')
    lines = configFile.readlines()
    keyValues = {}
    for line in lines:
        if line[0] == '#':
            continue
        
        line = line.replace("\t", " ")
        line = line.rstrip()
        linesplits = line.split(" ")
        key = linesplits[ 0 ].strip()
        if key in keys:
            value = linesplits[ len(linesplits) - 1 ].strip()
            val_table[key] = value

    configFile.close()



def check_born_data():
    s_id_key = val_table['server-serial-number'] + ":born"
    with open(out_file, 'r') as f:
        lines = f.readlines()
        with open(tmp_out_file, 'w') as fw:
            for line in lines:
                new_line = line.replace("born", s_id_key)
                fw.write(new_line)

map_map = {
    1 : [49, 56],
    2 : [1, 8],
    3 : [9, 16],
    4 : [17, 24],
    5 : [25, 32],
    6 : [33, 40],
    7 : [41, 48],
    8 : [62, 66],
    9 : [57, 61],
    10 : [67, 71],
    11 : [72, 75],
}

map_name = {
    1 : u"北欧",
    2 : u"东亚",
    3 : u"北美",
    4 : u"南美",
    5 : u"大洋洲",
    6 : u"西亚",
    7 : u"南欧",
    8 : u"王冠高原",
    9 : u"权杖谷底",
    10 : u"繁茂林地",
    11 : u"文明之王",
}

map_count = [0] * 12
#print(map_count)
def remain_born_data():
    for t in map_map:
        for i in range(map_map[t][0], map_map[t][1] + 1):
            cmd = 'echo scard %s:born_block:%d | redis-cli -h %s -p %s -a %s' % (val_table['server-serial-number'], i, val_table['server_logic_redis_ip'], val_table['server_logic_redis_port'], val_table['server_logic_redis_password'])
            val = int(os.popen(cmd).read())
            print("town:%d : remain:%d\n" % (i, val))
            map_count[t] += val

    for i in map_name:
        print(map_name[i] + " : " + str(map_count[i]) + "\n")



    
def main():
    parse_file(config_file)
    remain_born_data()

if __name__ == '__main__':
    main()
