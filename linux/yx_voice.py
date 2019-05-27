#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from aip import AipSpeech
from pydub import AudioSegment


# yasm-1.3.0.tar.gz
# tar jxvf ffmpeg-4.1.3.tar.bz2
# ./configure --enable-shared --prefix=/monchickey/ffmpeg

# 
APP_ID = '16328862'
API_KEY = 'SiGGvPDQS0kwtAqbFq3pwYEh'
SECRET_KEY = 'c8PGZ9mGoAb67Cg4ofnp1tB6CZbZnrMH'


class yXVoice():
	def __init__(self):
		self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	def convert_fmt(self, file_path, frame_rate=16000):
		save_path = file_path.repalce(".mp3", ".pcm")
		mp3_version = AudioSegment.from_mp3(from_path)
		mono = mp3_version.set_frame_rate(frame_rate).set_channels(1)
		mono.export(save_path, format='wav', codec='pcm_s16le')
		return save_path


	def asr(self, file_path):
		# 
		file_path = convert_fmt(file_path)
		
		# 识别本地文件
		msg = self.client.asr(get_file_content(file_path), 'pcm', 16000, {
		    'dev_pid': 1536,
		})

		print(msg)
		print(msg.get("err_no"))
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
	translate('v.mp3')


if __name__ == "__main__":
	main()