import os
import time
import cv2
import numpy as np

# table = "Ñ@#W$9876543210?!abc;:+=-,._"
#table = "@%#*+=-:,. "
# table = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^'. `"
# table = "█▓▒░"
table = "⠿⠽⠻⠟⠯⠭⠋⠙⠓⠒⠂"
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Couldn't open camera")
    exit()

while True:
    os.system('cls')
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame, exiting....")
        break

    cv2.imshow("Live Cam Feed", frame)
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Target width in characters
    width = 250
    # Calculate target height preserving aspect ratio
    # 0.5 factor accounts for terminal character aspect ratio (approx 1:2)
    # Braille blocks are 2x4 dots, so we want the resulting grid of characters 
    # to roughly maintain the image aspect ratio.
    char_height = int(frame.shape[0] * (width / frame.shape[1]) * 0.5)
    
    # Ensure at least 1x1
    width = max(1, width)
    char_height = max(1, char_height)

    # Braille logic: 2x4 dots per character
    # Resize image to full dot resolution
    dot_width = width * 2
    dot_height = char_height * 4
    
    # Resize (linear for smoothness before threshold)
    frame_resized = cv2.resize(frame_gray, (dot_width, dot_height), interpolation=cv2.INTER_LINEAR)
    
    # Add uniform noise to simulate dithering
    # This effectively decreases the "hard" contrast of the binary threshold
    # allowing for mid-tones to appear as scattered dots.
    noise = np.random.randint(-50, 50, frame_resized.shape)
    frame_resized = np.clip(frame_resized.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    
    # Binary threshold (127 midpoint). Returns 0 or 1.
    _, binary = cv2.threshold(frame_resized, 127, 1, cv2.THRESH_BINARY)
    
    # Reshape to (rows, cols, 4, 2) block grid
    # binary shape: (char_height*4, width*2)
    # View as: (char_height, 4, width, 2)
    # Then swap axes to get: (char_height, width, 4, 2)
    blocks = binary.reshape(char_height, 4, width, 2).transpose(0, 2, 1, 3)
    
    # Weights for the Braille dots (Unicode standard U+2800 ordering)
    # 1 4  ->  1   8
    # 2 5  ->  2   16
    # 3 6  ->  4   32
    # 7 8  ->  64  128
    weights = np.array([
        [1, 8],
        [2, 16],
        [4, 32],
        [64, 128]
    ], dtype=np.int32)
    
    # Vectorized calculation of dot sums for each character
    code_offsets = np.sum(blocks * weights, axis=(2, 3))
    
    # Convert to Unicode characters (Base U+2800)
    # We construct the list of strings
    braille_rows = []
    for row in code_offsets:
        braille_rows.append("".join(chr(0x2800 + c) for c in row))
    
    img_ascii = "\n".join(braille_rows)
    
    print(img_ascii)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()