import requests
from bs4 import BeautifulSoup
import urllib.request


url = 'https://cydmyz.com/'
file_directory = 'C:\\Users\\dell\\Desktop\\scr_grab\\'

# 发送HTTP请求获取HTML内容并解析
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

# 提取所有图片标签的src属性值，并下载图片
all_a_tags = soup.find_all("a")
for a_tag in all_a_tags:
    href_value = a_tag.get("href")
    #print(href_value)
    if href_value.endswith("html"):
#        #print(href_value)
        content2=requests.get(href_value).text
        child_page_soup=BeautifulSoup(content2,"html.parser")
        #child_page_soup = child_page_soup.text
        # print(child_page_soup)
        hrefs=child_page_soup.find_all("img")
        for i in hrefs:
            dowloading_url = i.get("src")
            # 排除空的url
            if not dowloading_url:
                continue
            # 判断是否包含指定关键字
            if "images" in dowloading_url or "wp-content" in dowloading_url:
                # 判断图片格式是否为jpg
                if dowloading_url.endswith(".jpg"):
                    file_name=dowloading_url.split("/")[-1]
                    file_path=file_directory+file_name
                    try:
                        # 下载图片并保存到本地文件
                        urllib.request.urlretrieve(dowloading_url, file_path)
                        print('图片已保存到', file_path)
                    except Exception as e:
                        print('发生错误：', e)

print("over!!!!")


