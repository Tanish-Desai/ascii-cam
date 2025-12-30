import cv2
import numpy as np

# Ñ@#W$9876543210?!abc;:+=-,._
# table = "Ñ@#W$9876543210?!abc;:+=-,._"
table = "@%#*+=-:,. "

# image_path = "img.jpg"
image_path = input("Enter image path: ").strip('"')

img = cv2.imread(image_path)
if img is None:
    print("Error: Image not found")
    exit()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize to a reasonable width (e.g. 100 chars) that fits on a screen
width = int(input("image size? "))
height = int(img.shape[0] * (width / img.shape[1]) * 0.55)
img_gray = cv2.resize(img_gray, (width, height))

img_ascii = ""
for i in range(img_gray.shape[0]):
    for j in range(img_gray.shape[1]):
        img_ascii += table[int(img_gray[i][j] / 255 * (len(table)-1))]
    img_ascii += "\n"

with open("img_ascii.txt", "w") as f:
    f.write(img_ascii)

# cv2.imshow("image_gray", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()