import cv2
import matplotlib.pyplot as plt

def imgtotempmat(image_path, min_temperature, max_temperature):
    # Read the thermal RGB image
    image = cv2.imread(image_path)

    # Convert the RGB image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the temperature matrix
    temperature_matrix = (gray_image / 255.0) * (max_temperature - min_temperature) + min_temperature

    # Display the original image and the temperature matrix
    plt.figure(figsize=(10, 10))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(temperature_matrix, cmap='jet', vmin=min_temperature, vmax=max_temperature)
    plt.colorbar()
    plt.title('Temperature Matrix')

    # Print the temperature matrix
    print('Temperature Matrix:')
    print(temperature_matrix)

    plt.show()
