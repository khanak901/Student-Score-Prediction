# Student Score Prediction Using Linear Regression

## 📌 Project Overview

This project uses **Linear Regression** to predict a student's score based on the number of hours they studied.

The project also evaluates the model's performance using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

## 📂 Dataset

The dataset contains two main columns:

* **Hours** – Number of hours studied
* **Score** – Student's score

## ⚙️ How It Works

1. Load the student dataset using Pandas.
2. Select **Hours** as the input feature.
3. Select **Score** as the target variable.
4. Train a Linear Regression model.
5. Predict student scores.
6. Calculate MAE, MSE, and RMSE to evaluate the model.
7. Allow the user to enter study hours and receive a predicted score.

## ▶️ How to Run

Clone this repository and install the required libraries:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python student_score_prediction.py
```

Enter the number of study hours when prompted to get the predicted score.

## 📊 Example

**Input:**

```text
Enter an hour: 5
```

**Output:**

```text
Prediction for Studying 5.0 hours is score = [...]
```

## 📈 Model Evaluation

The model is evaluated using:

* **MAE:** Measures the average prediction error.
* **MSE:** Measures the average squared prediction error.
* **RMSE:** Measures the square root of the average squared error.

## 🚀 Future Improvements

* Add train-test split for better model evaluation.
* Visualize the relationship between study hours and scores.
* Use a larger dataset.
* Build a simple user interface for predictions.
