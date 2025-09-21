import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import joblib  # For loading trained model
from sklearn.linear_model import LogisticRegression

# Load trained model
# You must train your logistic regression model first and save it using joblib
# For now we are training a dummy model for demonstration
def train_dummy_model():
    from sklearn.datasets import load_heart_disease
    from sklearn.model_selection import train_test_split

    # Dummy dataset - Replace this with real heart dataset (like UCI Heart dataset)
    url=r'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
    data = pd.read_csv(url)  # Make sure this file exists
    X = data.drop('target', axis=1)
    y = data['target']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    joblib.dump(model, 'heart_model.pkl')
    return X.columns

# Uncomment this line if you're running the code for first time
# feature_names = train_dummy_model()

# Load model and features
model = joblib.load(r'E:\Muqadas\university\projects\ML\Heart Diseases Prediction\heart_diseases_model.pkl')
feature_names = ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs',
                 'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
                 'ca', 'thal']

# Create GUI window
root = tk.Tk()
root.title("Heart Disease Predictor")
root.geometry("900x600")

# Load and place background image
bg_image = Image.open(r"E:\Muqadas\university\projects\ML\Heart Diseases Prediction\backgorund_image.jpg")  # Use your own image path
bg_image = bg_image.resize((900, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Frame for input
frame = tk.Frame(root, bg="white", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.7, anchor='n')

entries = {}

def predict():
    try:
        # Get all input values
        values = [float(entries[feat].get()) for feat in feature_names]

        # Create DataFrame
        new_record = pd.DataFrame([values], columns=feature_names)
        prediction = model.predict(new_record)

        result_text = "Heart Disease Detected 💔" if prediction[0] == 1 else "No Heart Disease 💖"
        result_label.config(text=result_text, fg="red" if prediction[0] == 1 else "green")
    except Exception as e:
        messagebox.showerror("Input Error", f"Please check your inputs.\n{e}")

# Add input fields
for idx, feat in enumerate(feature_names):
    label = tk.Label(frame, text=feat, bg="white")
    label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")

    entry = tk.Entry(frame)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[feat] = entry

# Predict button
predict_btn = tk.Button(root, text="Predict", font=("Arial", 14), command=predict, bg="#5cb85c", fg="white")
predict_btn.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.07)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="white")
result_label.place(relx=0.3, rely=0.93, relwidth=0.4, relheight=0.05)

root.mainloop()
