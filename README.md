# 漫画图片分割

有时候，我们下载下来的漫画是两页并排扫描的，比如

![](https://github.com/laike9m/split_p/raw/master/original.jpg "original image")

阅读起来非常不方便。于是就有了这么一个把图片分开的工具。之后就变成两张图了。

### 使用

```bash   
$ split.py path_to_manga
```

若原来的漫画路径为 `~/Documents/manga`  
则分割后的漫画路径为 `~/Documents/manga_splitted`

# Image split for manga reading

Downloaded manga sometimes contains two pages in one image, which makes painful reading.This tool separate the original images.

### Usage  
```bash   
$ split.py path_to_manga
```

Assume the original path to manga is `~/Documents/manga`   
then splitted manga reside in `~/Documents/manga_splitted` 