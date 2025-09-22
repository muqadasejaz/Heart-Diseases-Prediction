

# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# # Load the trained model
# model = joblib.load(r'E:\Muqadas\university\projects\ML\Heart Diseases Prediction\heart_diseases_model.pkl')

# @app.route('/', methods=['GET', 'POST'])
# def predict_heart_disease():
#     result = ""
#     form_data = {}
#     features = None
#     if request.method == 'POST':
#         try:
#             # Get form data
#             form_data = {
#                 'age': request.form['age'],
#                 'gender': request.form['gender'],
#                 'cp': request.form['cp'],
#                 'trestbps': request.form['trestbps'],
#                 'chol': request.form['chol'],
#                 'fbs': request.form['fbs'],
#                 'restecg': request.form['restecg'],
#                 'thalach': request.form['thalach'],
#                 'exang': request.form['exang'],
#                 'oldpeak': request.form['oldpeak'],
#                 'slope': request.form['slope'],
#                 'ca': request.form['ca'],
#                 'thal': request.form['thal']
#             }
#             # Convert to float for prediction
#             age = float(form_data['age'])
#             gender = float(form_data['gender'])
#             cp = float(form_data['cp'])
#             trestbps = float(form_data['trestbps'])
#             chol = float(form_data['chol'])
#             fbs = float(form_data['fbs'])
#             restecg = float(form_data['restecg'])
#             thalach = float(form_data['thalach'])
#             exang = float(form_data['exang'])
#             oldpeak = float(form_data['oldpeak'])
#             slope = float(form_data['slope'])
#             ca = float(form_data['ca'])
#             thal = float(form_data['thal'])

#             # Prepare input data for the model
#             input_data = [[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            
#             # Make prediction
#             prediction = model.predict(input_data)[0]
#             result = "Heart Disease Detected ❤️" if prediction == 1 else "No Heart Disease Detected"
            
#             # If heart disease is detected, store feature values for display
#             if prediction == 1:
#                 features = {
#                     'age': age,
#                     'gender': gender,
#                     'cp': cp,
#                     'trestbps': trestbps,
#                     'chol': chol,
#                     'fbs': fbs,
#                     'restecg': restecg,
#                     'thalach': thalach,
#                     'exang': exang,
#                     'oldpeak': oldpeak,
#                     'slope': slope,
#                     'ca': ca,
#                     'thal': thal
#                 }

#         except ValueError:
#             result = "Error: Please enter valid numerical values."
#         except Exception as e:
#             result = f"Error: An unexpected error occurred - {str(e)}"

#     return render_template('index.html', result=result, form_data=form_data, features=features)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'E:\Muqadas\university\projects\ML\Heart Diseases Prediction\heart_diseases_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict_heart_disease():
    result = ""
    form_data = {}
    features = None
    if request.method == 'POST':
        try:
            # Get form data
            form_data = {
                'age': request.form['age'],
                'gender': request.form['gender'],
                'cp': request.form['cp'],
                'trestbps': request.form['trestbps'],
                'chol': request.form['chol'],
                'fbs': request.form['fbs'],
                'restecg': request.form['restecg'],
                'thalach': request.form['thalach'],
                'exang': request.form['exang'],
                'oldpeak': request.form['oldpeak'],
                'slope': request.form['slope'],
                'ca': request.form['ca'],
                'thal': request.form['thal']
            }
            # Convert to float for prediction
            age = float(form_data['age'])
            gender = float(form_data['gender'])
            cp = float(form_data['cp'])
            trestbps = float(form_data['trestbps'])
            chol = float(form_data['chol'])
            fbs = float(form_data['fbs'])
            restecg = float(form_data['restecg'])
            thalach = float(form_data['thalach'])
            exang = float(form_data['exang'])
            oldpeak = float(form_data['oldpeak'])
            slope = float(form_data['slope'])
            ca = float(form_data['ca'])
            thal = float(form_data['thal'])

            # Prepare input data for the model
            input_data = [[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            result = "Heart Disease Detected ❤️" if prediction == 1 else "No Heart Disease Detected"
            
            # If heart disease is detected, store feature values for display
            if prediction == 1:
                features = {
                    'age': age,
                    'gender': gender,
                    'cp': cp,
                    'trestbps': trestbps,
                    'chol': chol,
                    'fbs': fbs,
                    'restecg': restecg,
                    'thalach': thalach,
                    'exang': exang,
                    'oldpeak': oldpeak,
                    'slope': slope,
                    'ca': ca,
                    'thal': thal
                }

        except ValueError:
            result = "Error: Please enter valid numerical values."
        except Exception as e:
            result = f"Error: An unexpected error occurred - {str(e)}"

    return render_template('index.html', result=result, form_data=form_data, features=features)

if __name__ == '__main__':
    app.run(debug=True)