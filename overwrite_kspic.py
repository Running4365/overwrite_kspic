'''
定期向WPS office的看图程序写入文本覆盖，防止其设置为默认的看图软件。

直接在安装目录（一般在C盘）搜索photolaunch.exe（wps图片的应用程序名字），搜索出来，建立一个名字为photolaunch.exe的文本文档代替他就可以了~
'''

import time 
from time import strftime, localtime
import logging
import os 

DEST_FILE = 'photolaunch.exe'
LOG_FILENAME = f'{__file__}.log'
SEARCH_DIR = r'C:\Users\zeng3\AppData\Local\Kingsoft\WPS Office'


def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def print_to_console_and_file(stra):
    print(stra)
    logging.info(f'{stra}')

def some_init(f):
    """装饰器"""
    def inner(*arg,**kwarg):
        s_time =  time.time() 
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
        logging.basicConfig(filename=LOG_FILENAME, filemode='a', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
        print_to_console_and_file('start logging...')
        res = f(*arg,**kwarg)
        e_time =  time.time() 
        runtime = e_time - s_time
        runtime_str = '{} hour {} minute {} second'.format(int(runtime//3600), int((runtime%3600)//60), int((runtime%3600)%60))
        print_to_console_and_file(f'\n[start time] {strftime("%H:%M:%S", localtime(s_time))}\n[end time] {strftime("%H:%M:%S", localtime(e_time))}\n[runtime] {runtime_str}\n\n')
        return res
    return inner

@some_init
def main():
    for i in findAllFile(SEARCH_DIR):
        if DEST_FILE in i:
            with open(i, 'w+') as f:   # ‘w+’ == w+r（可读可写，文件若不存在就创建）
                f.write('nooooooo')
            print_to_console_and_file(f'该文件被覆盖为文本文件：{i}')

if __name__ == '__main__':
    main()
