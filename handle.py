# -*- coding: utf-8 -*-

import hashlib
import reply
import receive
import web
from basic import Basic


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "ilaoxiang"
            list = [token, timestamp, nonce]
            list.sort()
            a = ''.join(list)
            s1 = hashlib.sha1()
            s1.update(a.encode())
            # map(sha1.update, list)
            hashcode = s1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument

    def POST(self):
        try:
            token = Basic().get_access_token()
            print(token)
            webData = web.data()
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "欢迎光临!"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyImageMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyImageMsg.send()
                else:
                    return reply.Msg().send()

            else:
                print("暂且不处理")
                return reply.Msg().send()
        except  Exception as Argment:
            print(Argment)
            return Argment
