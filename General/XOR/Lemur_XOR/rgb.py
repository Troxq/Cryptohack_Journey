from PIL import Image, ImageChops

lemur = "General/XOR/Lemur_XOR/flag.png"  # Change this to your image path
flag = "General/XOR/Lemur_XOR/lemur.png"

im1 = Image.open(lemur)
im2 = Image.open(flag)

pix1 = im1.load()
pix2 = im2.load()

w, h = im1.size #im1 and im2 have the same size

im3 = Image.new("RGB", (w, h))
pix3 = im3.load()

for i in range(w):
    for j in range(h):
        
        r1, g1, b1 = pix1[i, j]
        r2, g2, b2 = pix2[i, j]
        
        rn = r1 ^ r2
        gn = g1 ^ g2
        bn = b1 ^ b2
        
        pix3[i, j] = (rn, gn, bn)

im3.save("General/XOR/Lemur_XOR/xor_image.png")



















