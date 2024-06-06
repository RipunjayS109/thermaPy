
![v002banner](https://github.com/RipunjayS109/thermaPy/assets/145184045/c282dd9c-87da-4e9b-88e3-55542be87870)
# thermaPy: Thermal Image Processing for Python

## What's New in thermaPy v0.0.2

We are pleased to announce the release of thermaPy v0.0.2, introducing a significant enhancement to streamline thermal image analysis workflows.

**Introducing `detect_temperature_regions` Function:**

thermaPy v0.0.2 introduces the powerful `detect_temperature_regions` function, designed to expedite the identification and analysis of specific temperature zones within your thermal images. This function offers the following functionalities:

* **Efficient Temperature Region Detection:** Accurately pinpoint areas exceeding a user-defined detection temperature threshold.
* **Informative Bounding Box Generation:** Create bounding boxes around the detected temperature regions, providing valuable visual context for further analysis.
* **Convenient Excel Output:** Effortlessly export the temperature matrix as an Excel file for seamless data manipulation and exploration within spreadsheet software.

**Enhanced Workflow Efficiency:**

The `detect_temperature_regions` function empowers you to:

1. **Define a Detection Temperature:** Specify the temperature of interest for region identification.
2. **Locate Target Regions:** Efficiently identify image areas exceeding the defined detection temperature.
3. **Visualize Results:** Generate bounding boxes around the detected regions for clear visualization and improved understanding.
4. **Export Temperature Data:** Effortlessly export the temperature matrix to an Excel file, facilitating further analysis and data manipulation.

This innovative functionality streamlines temperature-based object detection and analysis, significantly enhancing the efficiency of your thermal image processing workflows.


**Example Usage:**

The following code snippet demonstrates how to effectively utilize the `detect_temperature_regions` function:

```python
import thermaPy

# Replace placeholders with your specific data
image_path = "path/to/your/thermal_image.jpg"
min_temperature = 20.0  # Degrees Celsius (or your preferred unit)
max_temperature = 40.0  # Degrees Celsius (or your preferred unit)
detection_temperature = 30.0  # Degrees Celsius (temperature threshold)
output_excel_path = "temperature_data.xlsx"  # Output file path

thermaPy.detect_temperature_regions(image_path, min_temperature, max_temperature, detection_temperature, output_excel_path)

print("Temperature regions identified and results saved!")
```

This code effectively:

1. Loads the specified thermal image.
2. Defines the minimum, maximum, and detection temperature values.
3. Invokes the `detect_temperature_regions` function to identify regions exceeding the detection temperature threshold.
4. Generates bounding boxes around the identified regions and displays the original image with the boxes superimposed for visualization.
5. Saves the temperature matrix as an Excel file for further analysis and data manipulation.

We encourage you to explore the `detect_temperature_regions` function and leverage its capabilities to enhance your thermal image processing workflows.

## User Guide

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
