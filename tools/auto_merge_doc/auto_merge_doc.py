#! /usr/bin/env python
#coding=utf-8

#
conf_name = "merge.conf"
table_conf = {}
keys = [
	'src_svr',
	'tar_svr',
	'svr_name',
	'svr_date',
	'svr_time',
	'mysql_ip',
]

doc_name = "[{src_svr}]_merge_to_[{tar_svr}].txt"
doc_content = """[{src_svr}]合服到{tar_svr}
数据迁移

1.[{tar_svr}]服务器合服准备
	完整停服(等待数据落地, 清memcache...)
	修证时间为当前时间
	清库(保留表结构, 清除数据库, 清除logic-redis, db-redis数据, {tar_svr}:*)
	修改开服时间以及赛季类型, 在global-redis中
		hset 1:seasonlist {tar_svr} "2|{svr_name}{tar_svr}|2021-04-09 01:00:00|2021-04-09 03:00:00|{svr_date} {svr_time}|20000"
		hset 2:seasonlist {tar_svr} "2|{svr_name}{tar_svr}|2021-04-09 01:00:00|2021-04-09 03:00:00|{svr_date} {svr_time}|20000"


2.[{src_svr}]合服准备(所有服务器均要执行以下操作)
	赛季结算(idip或gm指令)
	完整停服流程(等待数据落地, 清memcache...)
	清理合服脚本脏数据
		rm merge/data/*
	修改合服脚本配置
		merge/config.py
			dst_dbs = {{
				# tar mysql
				\'mysql_ip\':\'{mysql_ip}\',
				\'mysql_user\':\'woc\',
				\'mysql_port\':25000,
				\'mysql_password':\'WOC#@2020\',
				\'mysql_dbname':\'db_woc_loc_{tar_svr}\',
				\'server-serial-number\':{tar_svr},
			}}

3.[{src_svr}]依次执行数据迁库
	python dump_season_sql.py
	python import_season_sql.py
	python modify_redis.py


4.启动[{tar_svr}]服务器
	品管验证
"""

#
def parse_file(fileName, keys, conf_table):
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
			conf_table[key] = value
	
	configFile.close()


def main():
    parse_file(conf_name, keys, table_conf)
    file = doc_name.format(**table_conf)
    content = doc_content.format(**table_conf)
    if '800' == table_conf['tar_svr']:
    	content = content.replace("_800", "")
    with open(file, "w") as f:
    	f.write(content)

if __name__ == '__main__':
    main()
