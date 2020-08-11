#! /usr/bin/env python
#coding=utf-8


import os, sys, time

# config 
conf_keys = ['log-file-path'
    , 'alg_log_path'
    , 'server-serial-number']

val_table = {}
config_file = '../bin/loc.conf'

#
record_file = 'log_record.txt'
filter_name = '.log'

log_type = [
    'Err.',
    'Notice.',
    'Warning.',
]


def parse_file(fileName, keys):
    with open(fileName, 'r') as configFile:
        lines = configFile.readlines()
        val_table = {}
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

        return val_table


def filter_val(line, lstr, rstr):
    left = line.find(lstr)
    if left > 0:
        left += len(lstr)
        right = line[left : ].find(rstr)
        if right > 0:
            return line[left : left + right]
    return ""

class LogMom(object):
    """docstring for LogMom"""
    def __init__(self, paths, filter_name, log_type, del_after = False, record_file = "log_record.txt"):
        self.tab_files = {}
        for path in paths:
            for k in log_type:
                self.tab_files[path + k]  = {}
        self.log_type = log_type
        self.paths = paths
        self.filter_name = filter_name
        self.del_after = del_after
        self.record_file = record_file

    def Go(self): 
        self.filter_files()
        self.trim_files()
        self.file_merge()
        
    def make_time_key(self, stime):
        d = stime.split("-")
        h = d[2].split("_")
        time_key = int("%s%s%s%s" % (d[0], d[1], h[0], h[1]))
        return time_key

    def save_file_name(self, k, time_key, fname):
        if self.tab_files[k].has_key(time_key):
            self.tab_files[k][time_key].append(fname)
        else:
            self.tab_files[k][time_key] = []
            self.tab_files[k][time_key].append(fname)


    def filter_file_name(self, path, fname):
        for k in log_type:
            if fname.find(k) > 0:
                stime = filter_val(fname, k, '.')
                time_key = self.make_time_key(stime)
                self.save_file_name(path + k, time_key, fname)
                return


    def filter_files(self):
        for path in self.paths:
            for parent, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    if filename.find(filter_name) != -1:
                        fname = os.path.join(parent, filename)
                        self.filter_file_name(path, fname)
   

    def trim_files(self):
        for t in self.tab_files:
            self.tab_files[t] = sorted(self.tab_files[t].iteritems(), key = lambda x:x[0], reverse = False)
            self.tab_files[t].pop()


    def make_merger_name(self, type, key, path):
        s = str(key)
        idx = path[0].find(type) + len(type) - 1
        return "%s_merge.%s-%s-%s_%s.log" % (path[0][:idx], s[:4], s[4:6], s[6:8], s[8:])


    def re_save(self, fname, file_list):
        try:
            with open(fname, "w+") as f_save:
                for i in file_list:
                    slave = filter_val(i, 'svr_', '.')
                    f_save.write("-------------------------  svr_%s  -------------------------\n" % slave)
                    with open(i, "r") as f:
                        line = f.readline()
                        while line:
                            f_save.write(line)
                            line = f.readline()
                        f_save.write("\n\n")

                return True
        except Exception as e:
            raise e
            return False


    def file_merge(self):
        with open(self.record_file, "w+") as flog:
            now = time.strftime("%X-%m-%d %H:%M:%S", time.localtime())
            flog.write("-------------------------  %s  -------------------------\n" % now)
            for t in self.tab_files:
                for k in self.tab_files[t]:
                    if len(k[1]) <= 0:
                        continue
                    new_name = self.make_merger_name(t, k[0], k[1])
                    flog.write("merge_to : " + new_name + "\n")
                    if self.re_save(new_name, k[1]):
                        for x in k[1]:
                            flog.write("\t" + x + "\n")
                            if self.del_after:
                                if os.path.exists(x):
                                    os.remove(x)
                    flog.write("\n")
            end = time.strftime("%X-%m-%d %H:%M:%S", time.localtime())
            flog.write("-------------------------  %s  -------------------------\n\n\n" % end)




def main():
    val_table = parse_file(config_file, conf_keys)
    log_dirs = []
    _dir = val_table['log-file-path']
    if os.path.exists(_dir):
        log_dirs.append(_dir)
    _dir = val_table['alg_log_path']
    if os.path.exists(_dir):
        log_dirs.append(_dir)

    worker = LogMom(log_dirs
        , filter_name, log_type, True
        , val_table['server-serial-number'] + "_" + record_file)
    worker.Go()


if __name__ == '__main__':
    main()
