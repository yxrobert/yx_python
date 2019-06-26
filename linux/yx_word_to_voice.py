# coding=utf-8
import sys
import json
import random
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus


API_KEY = 'SiGGvPDQS0kwtAqbFq3pwYEh'
SECRET_KEY = 'c8PGZ9mGoAb67Cg4ofnp1tB6CZbZnrMH'

# API_KEY = '4E1BG9lTnlSeIf1NQFlrSq6h'
# SECRET_KEY = '544ca4657ba8002e3dea3ac2f5fdd241'


# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
PER = 4
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 6

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]

CUID = "123456PYTHON"
TTS_URL = 'http://tsn.baidu.com/text2audio'
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


class DemoError(Exception):
    pass


class yXWord(Exception):
    def __init__(self):
        self.token = self.fetch_token()

    def fetch_token(self):
        # print("fetch token begin")
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)

        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            print('token http response http code : ' + str(err.code))
            result_str = err.read()
            result_str = result_str.decode()
        result_str = result_str.decode()

        # print(result_str)
        result = json.loads(result_str)
        # print(result)
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not SCOPE in result['scope'].split(' '):
                raise DemoError('scope is not correct')
            # print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
            return result['access_token']
        else:
            raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

    def text_to_voice(self, content, save_name = "", PER = 3, PIT = 4, VOL = 7):
        tex = quote_plus(content)
        params = {'tok': self.token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
          'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

        data = urlencode(params)
        req = Request(TTS_URL, data.encode('utf-8'))

        has_error = False
        try:
            f = urlopen(req)
            result_str = f.read()
            headers = dict((name.lower(), value) for name, value in f.headers.items())
            has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
            
        except  URLError as err:
            print('asr http response http code : ' + str(err.code))
            result_str = err.read()
            has_error = True
        
        if save_name == "":
            # save_name = content[ : min(5, len(content))]
            save_name = str(random.randint(1000000, 10000000))

        save_file = "error.txt" if has_error else save_name + '.' + FORMAT
        with open(save_file, 'wb') as of:
            of.write(result_str)

        if has_error:
            return ""
        else:
            return save_file

word = yXWord()

contents = [
    "标准俯卧撑20次", 
    "半深蹲35次", 
    "平卧蛙举腿20次", 
    "短桥50次", 
    "直桥20次", 
]

def main():
    for i, v in enumerate(contents):
        word.text_to_voice(v, str(i))

if __name__ == '__main__':
    main()

