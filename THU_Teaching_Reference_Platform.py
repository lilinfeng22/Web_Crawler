import urllib.request
from tqdm import tqdm
times = 322
pages = [15, 40, 33, 22, 42, 32, 47, 40, 42, 49]
z = 0
for i in tqdm(range(times)):
    for j in range(pages[i]):
        j += 1
        url = f'https://reserves.lib.tsinghua.edu.cn/book4//00013268/00013268002/files/mobile/{i}.jpg'
        file_diractory = 'C:\\Users\\dell\\Desktop\\教材\\'
        file_name = url.split('/')[-1]
        num = int(file_name.split('.')[0]) + 1
        z += 1
        file_path = file_diractory + str(z) + ".jpg"
        # print(url)
        try:
            urllib.request.urlretrieve(url, file_path)
            # print('图片保存到', file_path)
        except Exception as e:
            print('发生错误：', e)
        continue
print('over')
