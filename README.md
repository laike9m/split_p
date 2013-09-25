# 漫画图片分割

一般而言，我们下载下来的漫画都是两页并排扫描的，比如

![whaever](/raw/master/original.jpg "original image")

阅读起来非常不方便。于是就有了这么一个把图片分开的工具。之后就变成两张图了:

![whatever](/raw/master/splitted_1.jpg  "splitted image 1")

![whatever](/raw/master/splitted_2.jpg "splitted image 1")

### 使用
脚本的最后两行如下。自己把comicdir替换成本地漫画的根目录路径即可。
如果漫画阅读方式是从左向右，改为`mode=LEFT2RIGHT`

	comicdir = ''
    main(comicdir, mode)

# Image split for manga reading

Downloaded manga usually contains two pages in one image,which makes painful reading.This tool separate the original images.

### How to use
Open the `split.py` file, custom the last two lines.

You should fill `comicdir` with your own comic directory.Note that if left part of the original image precedes the right part, you should change `mode` to `LEFT2RIGHT`.