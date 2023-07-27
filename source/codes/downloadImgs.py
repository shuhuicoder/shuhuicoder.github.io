import requests
import re
import random
import imghdr

# 二、构建代理池，可随机获取UA
ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           ]


def download(title1, title2, url1, url2):

    image1 = requests.get(url=url1)
    image2 = requests.get(url=url2)
    if imghdr.what(None, image1.content) == "jpeg":
        image = image1
        path = 'imgs3\\' + title1
    else:
        image = image2
        path = 'imgs3\\' + title2
    with open(path, mode='wb') as f:
        f.write(image.content)
    print(path + " is download.")


# for page in range(1, 126):
#     url = 'https://wallhaven.cc/toplist?page={}'.format(page)
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers)

# urls = re.findall('<a class="preview" href="(.*?)"', response.text)
# for i in urls:
#     response_2 = requests.get(url=i, headers=headers)
#     img_url = re.findall('<img id="wallpaper" src="(.*?)"', response_2.text)[0]
#     title = img_url.split('-')[-1]
#     download(title, img_url)
#     print(img_url)

for page in range(1, 154):
    url = 'https://wallhaven.cc/toplist?page={}'.format(page)
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    # }
    headers = {
        'user-agent': random.choice(ua_list)
    }
    response = requests.get(url=url, headers=headers)

    # print(response.text)
    urls = re.findall('<a class="preview" href="(.*?)"', response.text)
    # print(urls[0])
    # break
    for url in urls:
        strs = url.split("/")
        # print(strs)
        name = strs[-1]
        # print(name)
        pre = name[:2]
        # print(pre)

        imgUrl1 = "https://w.wallhaven.cc/full/" + pre + "/wallhaven-" + name + ".jpg"
        imgUrl2 = "https://w.wallhaven.cc/full/" + pre + "/wallhaven-" + name + ".png"
        # print(imgUrl)
        imgName1 = str(page) + '-' + name + ".jpg"
        imgName2 = str(page) + '-' + name + ".png"
        download(imgName1, imgName2, imgUrl1, imgUrl2)
print("done.")

