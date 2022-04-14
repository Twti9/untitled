#开发者：罗地观生
#开发时间：2021/4/27 23:37
#@File:chatbot.py
#@Author:Joshua
#@Contact:froginwell@163.com
import itchat
import requests
#from itchat import itchat
#@retry(tries=3)
def robot_chat(text):
    url="http://www.tuiling123.com/robot-chat/robot/chat/759052/CUZW?geetest_challenge=&geetest_validate=&geetest_seccode="
    return requests.post(url,json={"perception":{"inputText":{"text":text}},
                                   "userInfo":{"userId":"demo"}}).json()['data']['results'][0]['value'][text]
@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def auto_reply(msg):
    reply="excuse me?"
    try:
        reply=robot_chat(msg.text)
    except:
        pass
    finally:
        print(f'[In]{msg.tsxt}\t[Out]{reply}')
        return reply
itchat.auto_login(hotReload=True)
itchat.run()