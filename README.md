# AI-Based Fraud Detection in Government Schemes

# Overview
This project presents an AI-based fraud detection system designed to identify suspicious activities in government welfare schemes. It uses machine learning to detect abnormal transaction patterns and flag potential fraudulent beneficiaries.

# Problem Statement
Government schemes often face issues such as:
- Fake beneficiaries  
- Duplicate identities  
- Unusual transaction patterns  

These lead to financial losses and lack of transparency.

# Solution
We use the **Isolation Forest algorithm** to detect anomalies in beneficiary data. The system analyzes transaction details and identifies suspicious users automatically.

# How It Works
1. Input data (CSV file with user details)
2. Data preprocessing using Pandas
3. Apply Isolation Forest model
4. Detect anomalies (fraud users)
5. Generate output file with results

# Algorithm Used
- Isolation Forest (Unsupervised Machine Learning)
- Detects abnormal patterns in data

# Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- VS Code  

# Output
- `0 → Normal User`  
- `1 → Fraud User`  

The results are stored in `output.csv`.
<img width="1133" height="451" alt="image" src="https://github.com/user-attachments/assets/1d6e0c83-1ffa-4fa0-a103-8a5a17c63b82" />


# Project Structure 
<img width="417" height="502" alt="image" src="https://github.com/user-attachments/assets/244a89d7-edd3-49c4-b83f-5b28d83d0f76" />
