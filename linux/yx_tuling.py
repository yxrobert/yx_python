#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import urllib.request

# tuling = "ee393500451b4a13900a5242ae1680d2"
tuling = "66789b6821894beebeb875ecdb41918f"
api_url = "http://openapi.tuling123.com/openapi/api/v2"


class yXTuling():
    def __init__(self):
        self.info = {
        "perception":
        {
            "inputText":
            {
                "text": ""
            },

            "selfInfo":
            {
                "location":
                {
                    "city": "北京",
                    "province": "北京",
                    "street": "北苑路"
                }
            }
        },
        "userInfo": 
        {
            "apiKey": tuling,
            "userId": ""
        }
    }

    def do_respons(self, message, userid):
        self.info["userInfo"]["userId"] = userid
        self.info["perception"]["inputText"]["text"] = message

        req = json.dumps(self.info).encode('utf8')
        http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(http_post)
        response_str = response.read().decode('utf8')
        response_dic = json.loads(response_str)

        # if 
        print(str(response_dic['intent']['code']))
        results_text = response_dic['results'][0]['values']['text']
        print(response_dic)
        return results_text


tuling = yXTuling()


def main():
    message = "没有次数了?"
    user_id = 13552001103
    resp = tuling.do_respons(message, user_id)
    print(resp)

if __name__ == "__main__":
    main()