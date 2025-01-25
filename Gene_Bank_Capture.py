import re
import urllib.request
import os
# 打开电脑中的文件
with open(r'C:\Users\dell\Desktop\prokaryotes.txt', 'rb') as f:
    content = f.read().decode('utf-8')
#查找 FTP 链接
ftp_links = re.findall(r'ftp://[^\s]+', content)#正则处理得到FTP链接

# 将 FTP 链接换为http，貌似无法直接运行ftp所以进行了替换
for link in ftp_links:
    http_path = link.replace('ftp://', 'http://')
    #print(http_path)
    a=http_path.split("/")[-1]
    filepath = "C:\\Users\\dell\\Desktop\\finished_list\\%s.fna.gz"%a
    b=a+'_genomic.fna.gz'
    new_url=http_path+'/'+b
    dsr_filepath="C:\\Users\\dell\\Desktop\\unfinished_list\\%s.fna.gz"%a
    #print(new_url)

# 代码块，可能会出现异常
    error_url_path = "C:\\Users\\dell\\Desktop\\unfinished_list\\error_url.txt"
    try:
        urllib.request.urlretrieve(new_url, filepath)
        file_size=os.path.getsize(filepath)
        if file_size < 100:
            os.rename(new_url,dsr_filepath)
            with open(error_url_path,"w",encoding="utf-8")as f:
                f.write(new_url+"\n")
        else:
            print("dowloading %s...:)" % a)
# 四种已知错误，第五种排除其他错误
    except ValueError as e:
        print("%s is the valueerror:"%a,e)
        with open(error_url_path, "w", encoding="utf-8") as f:
            f.write(new_url + "\n")
    except urllib.error.HTTPError as e:
        print("%s is the HTTPError:"%a, e)
        with open(error_url_path, "w", encoding="utf-8") as f:
            f.write(new_url + "\n")
    except urllib.error.URLError as e:
        print("%s is the URLError:"%a, e)
        with open(error_url_path, "w", encoding="utf-8") as f:
            f.write(new_url + "\n")
    except OSError as e:
        print("%s is the OSError:"%a, e)
        with open(error_url_path, "w", encoding="utf-8") as f:
            f.write(new_url + "\n")
    except Exception as e:
        print("%s is the Other error:"%a, e)
        with open(error_url_path, "w", encoding="utf-8") as f:
            f.write(new_url + "\n")
# 跳过错误继续运算
    continue

print("over!!!!!!")
