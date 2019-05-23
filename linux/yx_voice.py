#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from aip import AipSpeech

# 
APP_ID = '16328862'
API_KEY = 'SiGGvPDQS0kwtAqbFq3pwYEh'
SECRET_KEY = 'c8PGZ9mGoAb67Cg4ofnp1tB6CZbZnrMH'


class yXVoice():
	def __init__(self):
		self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

	def asr(self, file_path):
		# 识别本地文件
		msg = self.client.asr(get_file_content(file_path), 'pcm', 16000, {
		    'dev_pid': 1536,
		})

		if msg.get("err_no"):
			print(msg.get("result"))
			return msg.get("result")
		else:
			return ""


voice = yXVoice()

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def translate(file_path):
	voice.asr(file_path)


def main():
	pass


if __name__ == "__main__":
	main()