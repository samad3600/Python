import cv2

# Read an image from file
image = cv2.imread('path/to/your/image.jpg')

# Display the image
cv2.imshow('My Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize an image
resized_image = cv2.resize(image, (new_width, new_height))

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
