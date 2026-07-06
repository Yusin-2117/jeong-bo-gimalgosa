
# 픽셀 아트 그리기

import matplotlib.pyplot as plt
from RGB import hex_to_rgb

rgb = hex_to_rgb('#E2C9A1')
print(rgb)

a = [[255,0,0,255,0,0,255],
     [0,128,128,0,255,255,0],
     [0,128,128,128,128,255,0],
     [0,128,128,128,128,255,0],
     [255,0,128,128,255,0,255],
     [255,255,0,255,0,255,255],
     [255,255,255,0,255,255,255]] #2차원 리스트

plt.imshow(a, cmap='gray')
plt.show()

r = [255,0,0]
g = [0,255,0]
c = [0,255,255]
y = [255,255,0]
m = [255,0,255]
b = [0,0,255]
w = [255,255,255]
d = [0,0,0]

art = [[g,d,d,g,d,d,g],
       [d,r,r,d,w,w,d],
       [d,r,r,rgb,r,w,d],
       [d,r,r,r,r,w,d],
       [g,d,r,r,w,d,g],
       [g,g,d,w,d,g,g],
       [g,g,g,d,g,g,g]
       ]#3차원 리스트

plt.imshow(art)
plt.show()