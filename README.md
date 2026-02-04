# XSS Detection Using CNN (Deep Learning)

This project demonstrates how to detect Cross-Site Scripting (XSS) attacks in HTML using a Convolutional Neural Network (CNN). It converts HTML content into ASCII matrices and feeds them to a CNN for binary classification (malicious vs. benign).

## 🔍 Features
- Converts HTML code into normalized ASCII matrices (image-like format)
- Classifies input as XSS or benign using a trained CNN model
- Preprocessing pipeline with BeautifulSoup and OpenCV
- Model trained on labeled dataset from Kaggle

## 📁 Project Structure
```txt
 - XSS-Detection/
     -     ├── model/ # Trained model
     -     ├── data/ # Dataset
     -     ├── test_html/ # Sample HTML files
     -     ├── src/ # Source code
     -     ├── README.md # This File
     -     ├── ProjectReport.pdf # Detailed report of project

```

---

## 🚀 How It Works

1. **HTML Preprocessing**:
   - HTML is cleaned using `BeautifulSoup`
   - Each character is converted to an ASCII value
   - The ASCII array is padded and reshaped to a `100x100` matrix
   - Matrix is normalized to values between 0 and 1

2. **CNN Architecture**:
   - 3 Convolutional layers with ReLU + MaxPooling
   - Dense layers for decision-making
   - Sigmoid output for binary classification

3. **Prediction**:
   - Model outputs a probability between 0 and 1
   - Threshold > 0.5 → XSS detected

---

## 🔍 Example Predictions

| HTML Snippet                                      | Prediction       | Confidence |
|--------------------------------------------------|------------------|------------|
| `<a href="http://example.com">Click</a>`         | ✅ Safe           | 0.04       |
| `<script>alert('XSS')</script>`                  | ❌ XSS Detected   | 0.98       |
| `<img src="x" onerror="alert('XSS')">`           | ❌ XSS Detected   | 0.92       |
| `<div onclick="console.log('safe')">Click</div>` | ✅ Safe           | 0.12       |

---

## 🧪 How to Test
---

1. Clone the repo:
```bash
git clone https://github.com/IJBaig/XSS-Detection.git
cd xss-detection
```


2. Place your HTML file in the `test/` directory.

3. Run the Python test script:

```bash
python src/test_xss_detection.py
```
---

## 📝 Jupyter Notebook

The training process is implemented entirely in a Jupyter Notebook:  
📁 `src/train_model.ipynb`

### 🧰 Libraries Used

- TensorFlow / Keras  
- OpenCV  
- NumPy / Pandas  
- Matplotlib  

### 📌 Notebook Includes

- Data preprocessing  
- Model architecture definition  
- Training and validation visualization  
- Model saving

---

## 📄 Report

For a detailed explanation of the project's methodology, implementation, and results, refer to:  
📁 📄 [Full Project Report](ProjectReport.pdf)

