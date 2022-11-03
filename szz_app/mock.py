import requests
import json

headers = {
        'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NTg0MDU3LCJpYXQiOjE2NjU1ODIyNTcsImp0aSI6IjhjN2RlODljNjg0MDQ3YzVhYWZhZmJkNGY3MDc0Y2IxIiwidXNlcl9pZCI6NH0.nKoM63V5rKMIu87TRypCM-dCO-eUYmL0IhxcZbqlksY',
        'Content-Type': 'application/json',
    }


def add_answer(count):
    data = {
        "takepoints": [
            {
                "order": 1,
                "point": "论点1",
                "evidences": [
                    {
                        "data": "论点1.1",
                        "order": 1
                    },
                    {
                        "data": "论点1.2",
                        "order": 2
                    }
                ]
            },
            {
                 "order": 2,
                 "point": "论点2",
                 "evidences": [
                    {
                        "data": "论点2.1",
                        "order": 1
                    },
                    {
                        "data": "论点2.2",
                        "order": 2
                    }
                ]
            }

        ],
        "body": "我的回答一",
        "user": 1,
        "state": 0,
        "question": 3
    }
    for i in range(count):
        data["body"] = '我的回答' + str(i)
        response = requests.post('http://172.30.240.241:8000/api/answer', headers=headers, data=json.dumps(data))


def add_questionnaire(count):
    data = {
        "title": "创建时间较晚gai",
        "description": "描述",
        "user": 1,
        "topics": [
            {
                "title": "题目1",
                "order": "1",
                "description": "描述2",
                "type": 1,
                "required": True,
                "options": [
                    {
                        "label": "0",
                        "content": "选择A"
                    },
                    {
                        "label": "1",
                        "content": "选择B"
                    }
                ]
            },
            {
                "title": "题目2",
                "order": "2",
                "required": False,
                "description": "描述",
                "type": 2
            }
        ],
        "fill_time": "{'h':1}",
        "create_time": "2022-03-21T18:55:45",
        "end_time": "2022-11-28T18:55:45"
    }
    for i in range(count):
        data["title"] = '我的问卷' + str(i)
        response = requests.post('http://172.30.240.241:8000/api/questionnaire', headers=headers, data=json.dumps(data))
        response.encoding = "utf-8"
        print(response.text)


if __name__ == '__main__':
    add_questionnaire(100)
