# Color_Detection_System
A Python-based application that detects and identifies colors from any image using OpenCV, Pandas, and NumPy. The system allows users to upload an image, click on any pixel, and instantly get the color name along with its RGB values.

📌 Features

Upload an image through a simple GUI (PyQt5).

Double-click on any pixel to detect its color.

Displays the color name and corresponding RGB values.

Visualizes the detected color in a bar overlay on the image.

Dataset of 865+ colors (with RGB and HEX codes).

🛠️ Tech Stack

Python 3.x

OpenCV – Image processing

NumPy – Numerical operations

Pandas – Handling color dataset

PyQt5 – User interface

📂 Project Structure
├── color_detection.py     # Core logic for color detection
├── gui.py                 # GUI for image selection
├── colors.csv             # Dataset of color names & RGB values
├── README.md              # Project documentation

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/color-detection-system.git
cd color-detection-system


Install dependencies:

pip install -r requirements.txt


Run the application:

python gui.py


Select an image → Double-click on any pixel → See color name + RGB values.


🔮 Future Enhancements

Implement image clustering based on dominant colors using K-Means.

Extend support to live video feeds for real-time color detection.

Build an image filtering tool for photographers and designers.

👨‍💻 Contributors

Nehil Kishor Joshi

Shivam Divyesh Joshi

Smit Samir Panchal

Dharmendra Jayesh Pancholi

📖 References

Color Dataset

OpenCV, Pandas, NumPy, PyQt5 Documentation
