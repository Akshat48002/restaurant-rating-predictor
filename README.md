# 🍽️ Restaurant Rating Predictor

A simple **Streamlit web application** that predicts the rating of a restaurant based on several input features such as average cost, table booking availability, online delivery availability, and price range.

---

## 📌 Features
- Predicts restaurant ratings using a pre-trained **machine learning model**.
- Takes the following inputs:
  - Average cost for two people
  - Table booking availability
  - Online delivery availability
  - Price range
- Displays:
  - Predicted rating (numeric)
  - Qualitative label (`Poor`, `Average`, `Good`, `Very Good`, `Excellent`)

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** for the web interface
- **scikit-learn** for the machine learning model
- **NumPy** for numerical computations
- **Joblib** for loading the saved scaler and ML model

---

## 📂 Project Structure
├── app.py               # Main Streamlit application 
├── scaler.pkl           # StandardScaler object 
├── mlmodel.pkl          # Trained Machine Learning model
├── requirements.txt     # Python dependencies 
└── README.md            # Project documentation


---

## 🚀 How to Run Locally
1. **Clone this repository**
git clone https://github.com/your-username/restaurant-rating-predictor.git
cd restaurant-rating-predictor


2. **Create a virtual environment**
python3 -m venv venv


3. **Activate the virtual environment**
* **Mac/Linux:**
  ```
  source venv/bin/activate
  ```
* **Windows:**
  ```
  venv\Scripts\activate
  ```

4. **Install dependencies**
pip install -r requirements.txt


5. **Run the Streamlit app**
streamlit run app.py



---

## 📊 How It Works

1. **User inputs**:
* Average Cost for two people
* Table Booking availability
* Online Delivery availability
* Price Range
2. Inputs are preprocessed using the saved **StandardScaler** (`scaler.pkl`).
3. The preprocessed data is fed into the trained ML model (`mlmodel.pkl`).
4. The model predicts the restaurant rating (numeric) and assigns a qualitative label.

---

## 📸 Example

![App Screenshot](screenshot.png)
*Example prediction page*

---

## 📄 License

This project is licensed under the MIT License. You can freely use, modify, and distribute it.

---

**Made with ❤️ using Python & Streamlit**

