from basic import Basic
import urllib.request as urllib
import requests


class Media(object):
    def __init__(self):
        pass

    def upload(self, accessToken, filePath, mediaType):
        try:
            openFile = open(filePath, "rb")
            param = {'media': openFile}
            postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
            #rulResp = requests.post(postUrl, files=files)
            request = requests.post(postUrl, files=param)
            print(request.content)
        except Exception as error:
            print(error)


if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = 'E:/1.jpg'
    mediaType = 'image'
    myMedia.upload(accessToken, filePath, mediaType)
