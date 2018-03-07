import ctypes
import datetime
import json
import os.path
import urllib.request

from PIL import Image, ImageDraw, ImageFont

img_desc = ""


def get_img_url(raw_img_url="http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&pid=hp"):
    # 读取bing壁纸url
    req = urllib.request.urlopen(raw_img_url).read()
    # 解析返回数据
    data = json.loads(req.decode("utf-8"))
    global img_desc
    img_desc = data["images"][0]["copyright"]
    # 获取图片地址
    url = "https://cn.bing.com" + data["images"][0]["url"]
    print("图片地址:", url)
    # print("图片描述:", img_desc)
    return url


def save_img_local(url, path):
    # 文件夹是否存在
    # print(path, os.path.exists(path))
    # 图片的名称（url后缀）
    # print(os.path.basename(url))
    # 保存图片路径
    # print(os.path.join(path, os.path.basename(url)))
    file_path = os.path.join(path, datetime.date.today().strftime("%Y-%m-%d") + "_" + os.path.basename(url))
    # 保存图片url到指定目录
    urllib.request.urlretrieve(url, file_path)
    # 返回图片路径
    print("下载图片:", file_path)
    return file_path


# 增加水印
def img_add_desc(file_path):
    img = Image.open(file_path).convert("RGBA")
    img_txt = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ft = ImageFont.truetype("c:/windows/fonts/msyhbd.ttc", 16)
    d = ImageDraw.Draw(img_txt)
    # 调整描述位置
    d.text((img_txt.size[0] / 2 - len(img_desc) * 5, img_txt.size[1] - 70), img_desc, font=ft,
           fill=(255, 255, 255, 255))
    out = Image.alpha_composite(img, img_txt)
    out.save(file_path, 'PNG')


def set_img(filePath):
    # windows设置壁纸命令
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0)
    print("设置壁纸完成")


def main():
    url = get_img_url()
    filePath = save_img_local(url, "D:/bmp/bing")
    img_add_desc(filePath)
    set_img(filePath)


main()
