import math, time, numpy as np
from PIL import Image, ImageDraw
from math import floor
sz = 1000
it = 20
xmin = -5
xmax = 5
imin = -5
imax = 5
pxr = 1.1
x = np.linspace(xmin, xmax, sz)
i = np.linspace(imin, imax, sz)
canvas = Image.new("RGB", (int(sz/pxr), int(sz/pxr)), (0,0,0))
draw = ImageDraw.Draw(canvas)
aa = -1
time1 = time.time()
for a in x:
    print("\n" + str(time.time()-time1))
    time1 = time.time()
    aa += 1
    print(str(aa) + "/" + str(sz))
    for b in i:
        start = a + (b) * 1j
        c1 = 0
        for c in range(it):
            c1 = c
            start = a + (b) * 1j**start
            if start.real > math.e or start.imag > 1000:
                break
        c1 = (c1/it)
        if abs(start.real) > 1 or abs(start.imag) > 1:
            draw.point((floor((a+abs(xmin))*int(sz/(pxr*(abs(xmin)+xmax)))),floor((b+abs(imin))*int(sz/(pxr*(abs(imin)+imax))))), fill=(int(200/((c1+1)**2)),int(200/((c1+1)**3)),int(200/((c1+1)))))
canvas.save("blank_canvas.jpg")
