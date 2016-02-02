ffmpeg usage ffmpeg用法
========================
2014-11-10


# 提取音频 #
<pre>
ffmpeg -i input -vn output.mp3
</pre>
-vn 不需要视频 no video
# 压缩 #
<pre>
ffmpeg -i input -acodec copy -vcodec copy -s 800x600 output
</pre>
-s scale 压缩后大小
