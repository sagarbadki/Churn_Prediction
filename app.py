# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
# from sklearn.ensemble import RandomForestClassifier

# Load the Random Forest CLassifier model
filename = 'churn_rfc.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        senior_citizen = int(request.form['SeniorCitizen'])
        partner = int(request.form['Partner'])
        dependents = int(request.form['Dependents'])
        phone_service = int(request.form['PhoneService'])
        mutliple_lines = float(request.form['MultipleLines'])
        internet_service = float(request.form['InternetService'])
        online_security = int(request.form['OnlineSecurity'])
        online_backup = int(request.form['OnlineBackup'])
        device_protection = int(request.form['DeviceProtection'])
        tech_support = int(request.form['TechSupport'])
        streaming_tv = int(request.form['StreamingTV'])
        streaming_movies= int(request.form['StreamingMovies'])
        contract = int(request.form['Contract'])
        paperless_billing = int(request.form['PaperlessBilling'])
        payment_method = int(request.form['PaymentMethod'])
        monthly_charges = float(request.form['MonthlyCharges'])
        total_charges = float(request.form['TotalCharges'])
                
        
        data = np.array([[gender, senior_citizen, partner,dependents, phone_service, mutliple_lines, internet_service, online_security,
                    online_backup,device_protection,tech_support,streaming_tv,streaming_movies,contract,paperless_billing,payment_method,                       monthly_charges,total_charges]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)