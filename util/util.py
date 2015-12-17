#coding=utf8
import hashlib
import time,base64,psutil
import random, os, re
import Image, ImageDraw, ImageFont, ImageFilter


def getPasswordMd5(password, regDate):
    """
    获取MD5值 v0.1
    :param password: 用户密码
    :param regDate: 注册日期（盐）
    :return: MD5
    """
    m = hashlib.md5()
    m.update(password+regDate)
    return m.hexdigest()

def getTimeNow():
    """
    获取当前日期时间戳
    :return: 时间戳
    """
    return int(time.time())


def getRamdomString(strm):
    """
    生成一个唯一的字符串用于激活码
    str: 用户名
    :return:
    """
    m = hashlib.md5()
    m.update(str(time.time())+ strm)
    return base64.encodestring(m.digest())[:-3].replace('/', '$').encode('utf-8')


class getServerInfo():
    '''
    获取服务器相关的信息
    '''
    @staticmethod
    def getCPUuse():
        '''
        获取cpu的当前使用率
        :return: 当前使用率
        '''
        return str(psutil.cpu_percent()) + '%'

    @staticmethod
    def getMemuse():
        '''
        获取当前的内存占用率
        :return: 内存占用率
        '''
        virtualmem = psutil.virtual_memory()
        total = virtualmem.total
        free = virtualmem.free
        return str((total-float(free))/total) + '%'


def isEmailString(str):
    """
    判断是否是邮箱格式
    :param str:字符串
    :return:
    """
    s = r"^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$"
    patten = re.compile(s)
    if patten.match(str):
        return True
    else:
        return False


class ValidCode():
    """
    验证码
    """
    def __init__(self):
        self.width = 90
        self.height = 30

    def randomChar(self):
        return chr(random.randint(65, 90))

    def randomColor(self):
        return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))

    def randomColor2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def drawCode(self):
        str_return = ""#返回的随机字符
        img = Image.new("RGB", (self.width, self.height),(255, 255, 255))
        font = ImageFont.truetype(os.getcwd()+"/UbuntuMono-R.ttf", 18)
        draw = ImageDraw.Draw(img)
        #填充每个像素点
        for x in range(self.width):
            for y in range(self.height):
                draw.point((x, y), fill=self.randomColor())

        #输出文字
        for t in range(4):
            tmp = self.randomChar()
            str_return += tmp
        #font_width, font_height = font.getsize(str_return)
            draw.text((17 * t + 8, 5), tmp, font=font, fill=self.randomColor2())

        # 图形扭曲参数
        params = [1 - float(random.randint(1, 2)) / 100,
              0,
              0,
              0,
              1 - float(random.randint(1, 10)) / 100,
              float(random.randint(1, 2)) / 500,
              0.001,
              float(random.randint(1, 2)) / 500
              ]
        img = img.transform((self.width, self.height), Image.PERSPECTIVE, params) # 创建扭曲

        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) #模糊

        return img, str_return