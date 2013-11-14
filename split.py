'''
输入图片根目录录复制出一个完整的文件夹及子文件夹
假定漫画的存储结构如下
学园默示录
    第一话
        一堆jpg
    第二话
        一堆jpg
这样不会有更多层的目录.这个假设暂时看来是合理的
如果图片本身height就大于width,那么就改变原图
需要注意图片排版是从左到右还是从右到左,默认为RIGHT2LEFT
'''
from PIL import Image
import os
import re
from glob import glob

global RIGHT2LEFT, LEFT2RIGHT   # 定义页面排版顺序,先左后有或先右后左
RIGHT2LEFT = 1
LEFT2RIGHT = 2


def getThreeDigit(num):
    #将漫画的页码规范为3位数显示，返回字符串，比'1'->'001','21'->'021'zz
    if len(str(num)) >= 3:
        return str(num)
    else:
        if num < 10: 
            return '00'+str(num)
        elif num > 9 and num < 100:
            return '0'+str(num)
        elif num > 99:
            return str(num)
        else:
            return False

def main(comicdir,mode=RIGHT2LEFT):
    '''入口函数'''
    (head,comicname) = os.path.split(comicdir)
    new_root = comicname + '_splitted'
    if not os.path.exists('%s\%s' % (head,new_root)):
        os.mkdir('%s\%s' % (head,new_root))
    
    #创建文件夹结构
    for _,subdirs,_ in os.walk(comicdir):
        for subdir in subdirs:
            if not os.path.exists('%s\%s\%s' % (head,new_root,subdir)):
                os.mkdir('%s\%s\%s' % (head,new_root,subdir))
    
    # 处理图片并保存到之前创建的文件夹结构
    types = ('*.jpg', '*.png',) # 支持的文件类型,可添加
    pics = []
    
    # glob会将[..]认为是匹配方括号中出现的字符,所以需要改为'['->'[[]',']'->'[]]'
    comicdir = re.sub(r'(?P<squarebracket>\[|\])', '[\g<squarebracket>]', comicdir)    
    for type in types:
        pics.extend(glob(r'%s\%s' % (comicdir, type)))  # 不再使用生成器,直接用List
        pics.extend(glob(r'%s\*\%s' % (comicdir, type)))
        
    num_all = len(pics)
    num_splitted = 0

    for pic in pics:
        # 找出图片的数字序号
        image = Image.open(pic)
        size = image.size   #size = (width,height)
        width = size[0]
        height = size[1]
        
        if width > height:  # do split
            result = re.finditer(r'\d+',pic)
            for number in result:
                pass
            p_ID = number.group()
            start = number.start()
            end = number.end()
            
            if mode == RIGHT2LEFT:
                p_ID_left = str(getThreeDigit(int(p_ID)*2))
                p_ID_right = str(getThreeDigit(int(p_ID)*2-1))
            else:
                p_ID_left = str(getThreeDigit(int(p_ID)*2-1))
                p_ID_right = str(getThreeDigit(int(p_ID)*2))
                
            save_left_dir = pic[:start] + p_ID_left + pic[end:]
            save_right_dir = pic[:start] + p_ID_right + pic[end:]
            save_left_dir = save_left_dir.replace(comicname, new_root, 1)
            save_right_dir = save_right_dir.replace(comicname, new_root, 1)
            
            left_image_box = (0, 0, int(width/2), height)
            right_image_box = (int(width/2), 0, width, height)
            left_image = image.crop(left_image_box)
            right_image = image.crop(right_image_box)
            left_image.convert('RGB').save(save_left_dir,'jpeg')
            right_image.convert('RGB').save(save_right_dir,'jpeg')
        else:# 直接保存进新的路径即可
            save_dir = pic.replace(comicname, new_root, 1)
            image.convert('RGB').save(save_dir,'jpeg')
        num_splitted += 1
        if not num_splitted % 100:
            print('进度%s/%s' % (num_splitted,num_all))
        
        
    
if __name__ == '__main__':
    mode = RIGHT2LEFT
    comicdir = r'C:\Users\dell\Desktop\赌博堕天录'
    main(comicdir, mode)
