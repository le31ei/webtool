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


def getRamdomString(str):
    """
    生成一个唯一的字符串用于激活码及注册功能,以及用户的userid
    str: 用户名
    :return:
    """
    m = hashlib.md5()
    m.update(str(time.time())+ str)
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


"""
验证码
"""

numbers = ''.join(map(str, range(10)))
chars = ''.join((numbers))
path = os.getcwd()+"/UbuntuMono-R.ttf"
def create_validate_code(size=(90, 30),
                         chars=chars,
                         mode="RGB",
                         font_type=path,
                         bg_color=(255, 255, 255),
                         fg_color=(255, 0, 0),
                         font_size=18,
                         length=4,
                         draw_points=True,
                         point_chance = 2):

    width,height = size
    img = Image.new(mode, size, bg_color) # 创建图形
    draw = ImageDraw.Draw(img) # 创建画笔

    def get_chars():
        '''''生成给定长度的字符串，返回列表格式'''
        return random.sample(chars, length)

    def create_points():
        '''''绘制干扰点'''
        chance = min(50, max(0, int(point_chance))) # 大小限制在[0, 50]

        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 50)
                if tmp > 50 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        '''''绘制验证码字符'''
        c_chars = get_chars()
        strs = '%s' % ''.join(c_chars)

        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)

        draw.text(((width - font_width) / 3, (height - font_height) / 4),
            strs, font=font, fill=fg_color)

        return strs

    if draw_points:
        create_points()
    strs = create_strs()

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
    img = img.transform(size, Image.PERSPECTIVE, params) # 创建扭曲

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # 滤镜，边界加强（阈值更大）

    return img,strs


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