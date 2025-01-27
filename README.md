🌾 Crop Recommendation System

📖 Overview

This project presents a Crop Recommendation System leveraging a Random Forest Classifier to suggest the most suitable crop based on specific environmental and soil conditions. The system uses a machine learning pipeline to process the input features, predict the best crop, and provide results through a user-friendly web interface.

🚀 Features

Input multiple soil and environmental parameters such as Nitrogen (N), Phosphorus (P), Potassium (K), pH, Temperature, Humidity, and more.
Predicts the most suitable crop for the given conditions using a trained Random Forest Classifier.
Implements feature scaling and preprocessing with a Pipeline for streamlined operations.
Interactive web interface for user input and prediction visualization.

🛠️ Tech Stack

Programming Languages:
Python
HTML
CSS
JavaScript

Libraries and Frameworks:
Backend: Flask
Machine Learning: Scikit-learn, NumPy, Pandas
Frontend: Bootstrap, CSS

Tools:
Random Forest Classifier
StandardScaler (for feature scaling)

📂 Directory Structure

Crop-Recommendation-System/
├── app/
│   ├── static/
│   │   ├── style.css        # CSS file for frontend styling
│   ├── templates/
│   │   ├── index.html       # HTML file for user interface
│   ├── model/
│   │   ├── crop_model.pkl   # Trained machine learning model
│   ├── app.py               # Flask application
├── data/
│   ├── dataset.csv          # Dataset used for training
├── README.md                # Project documentation


⚙️ How to Run

Prerequisites:

Python 3.8 or above
Flask installed (pip install flask)
Scikit-learn installed (pip install scikit-learn)

Steps:

Clone this repository:
git clone https://github.com/your-username/crop-recommendation-system.git

Navigate to the project directory:
cd crop-recommendation-system

Install required Python libraries:
pip install -r requirements.txt

Run the Flask application:
python app.py

Open your browser and go to:
http://127.0.0.1:5000/

🔍 Example Inputs and Outputs

Input:
Nitrogen (N): 150
Phosphorus (P): 20
Potassium (K): 80
pH: 6.5
Temperature: 30°C
Humidity: 75%
Rainfall: 200mm

Output:
Recommended Crop: Wheat

📊 Dataset

The system is trained on a dataset comprising 102,200 records with 16 features, including soil nutrients, environmental conditions, and crop labels.

📝 Future Enhancements

Incorporate more advanced models like Gradient Boosting or Neural Networks.
Extend the dataset to include more crops and regions.
Add support for dynamic data inputs from IoT devices.

🤝 Contributions
Feel free to fork this repository, raise issues, or submit pull requests. Contributions are welcome!

📜 License
This project is licensed under the MIT License.

📧 Contact
For queries or feedback, please contact:

Your Name: jashwanthreddykolla@gmail.com
GitHub Profile: https://github.com/jashwanthreddy19
