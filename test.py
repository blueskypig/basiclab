import video

fp=open('test.jpg','rb');
img=fp.read()
res=video.baiduface(img)
print(res)