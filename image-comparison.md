图像比较
=================
## 感知哈希 Perceptual Hash ##

* 缩小图像
* 灰度化处理
* 二值化处理
* 产生图像指纹


特点：速度快，算法简单，但无法匹配变换（如，旋转等）后的图像。


[感知哈希算法的详细描述](http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html)


[感知哈希开源库：pHash](http://phash.org/)


[感知哈希的另一种实现：dhash](http://www.hackerfactor.com/blog/index.php?/archives/529-Kind-of-Like-That.html)


## 基于特征点比较 Keypoint Matching ##


* 生成一系列特征区域
* 对特征区域进行处理产生特征点
* 对特征点进行比较，得出结果


特点：标准的图像配准算法，可用于图像匹配，健全性强，计算速度较慢，涉及很多数学知识（本人数学基础巨差，完全看不懂）

代表算法: **sirf**, **surf**


## 直方图匹配 Histogram method ##


* 生成多个直方图
* 比较直方图，得出图像近似度


特点：速度较快，健全性不强，可以通过产生特殊的直方图兼容图像变换


## 特征点匹配结合决策树 Keypoint and Decision Trees ##


特征匹配与机器学习相结合


特点：速度快，健全性强，但算法实现复杂


## 参考 ##
[感知哈希算法——找出相似的图片](http://www.cnblogs.com/technology/archive/2012/07/12/Perceptual-Hash-Algorithm.html)


[Dr. Neal Krawetz' Blog](http://www.hackerfactor.com/)


[Image comparison - fast algorithm - Stack Overflow](http://stackoverflow.com/questions/843972/image-comparison-fast-algorithm)


[Simple image comparison in .NET](http://www.codeproject.com/Articles/374386/Simple-image-comparison-in-NET)


[SIFT算法详解](http://blog.csdn.net/zddblog/article/details/7521424)


[SIFT 特征提取算法总结](http://www.cnblogs.com/cfantaisie/archive/2011/06/14/2080917.html)
[特征点检测学习_surf算法](http://www.cnblogs.com/tornadomeet/archive/2012/08/17/2644903.html)

