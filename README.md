![[banner.png]]
# thermaPy: Thermal Image Processing for Temperature Extraction

**thermaPy** is a Python library designed for efficient extraction of temperature information from RGB thermal images. It provides a single, user-friendly function (`imgtotempmat`) to convert an RGB thermal image into a corresponding temperature matrix. This matrix offers pixel-wise temperature data, enabling further analysis and visualization of thermal features within the image.

**Key Features:**

- **Simple and Intuitive API:** The `imgtotempmat` function requires only the image path, minimum temperature, and maximum temperature for operation.
- **Temperature Matrix Generation:** Creates a NumPy array representing the temperature distribution across the image.
- **Flexibility with Temperature Units:** Supports temperature values in degrees Celsius, Fahrenheit, or Kelvin (as defined by the user).

**Installation**

**Method 1: Using pip**

Bash

```
pip install thermaPy
```

**Method 2: Manual Installation**

1. Clone this repository.
2. Navigate to the project directory.
3. Run:

Bash

```
python setup.py install
```

**Usage**

1. **Import the library:**
    
    Python
    
    ```
    import thermaPy
    ```
    
2. **Utilize the `imgtotempmat` function:**
    
    Python
    
    ```
    temperature_matrix = thermaPy.imgtotempmat(image_path, min_temperature, max_temperature)
    ```
    

**Parameters:**

- `image_path` (str): The file path to the RGB thermal image (supports common formats like PNG, JPG, BMP, etc.).
- `min_temperature` (float): The minimum temperature value represented in the image (unit depends on user convention).
- `max_temperature` (float): The maximum temperature value represented in the image (same unit as `min_temperature`).

**Return Value:**

The function returns a NumPy array representing the temperature matrix, where each element corresponds to the temperature of the corresponding pixel in the original image.

**Example:**

Python

```
import thermaPy

# Replace with your actual image path and temperature range
image_path = "path/to/your/thermal_image.jpg"
min_temperature = 20.0  # Degrees Celsius (or your preferred unit)
max_temperature = 40.0  # Degrees Celsius (or your preferred unit)

temperature_matrix = thermaPy.imgtotempmat(image_path, min_temperature, max_temperature)

# Access individual temperature values via matrix indexing
temperature = temperature_matrix[100, 200]

print("Temperature at (100, 200):", temperature, "°C")

# Further Processing (Optional):
# The temperature matrix can be used for visualization, data analysis, and other applications.
```

**Additional Notes:**

- The library assumes a linear relationship between grayscale intensity and temperature within the specified minimum and maximum values. If your image employs a different calibration, the calculation in the `imgtotempmat` function might require adjustment.

By leveraging `thermaPy`, you can streamline the process of extracting temperature data from thermal images, enabling more efficient analysis and exploration of thermal features within your research or engineering projects. 
