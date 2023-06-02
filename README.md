# Ads Click Prediction

This project aims to predict whether a user will click on a particular ad based on their demographic and behavioral information. It utilizes machine learning algorithms, specifically Logistic regression and Naive Bayes, to train and test the predictive model.

## Dataset

The dataset used for this project is sourced from Kaggle and consists of various features related to advertising and user behavior. The features include:

- Age: The age of the user.
- Average Area Income: The average income of the user's area.
- Daily Time Spent on Website: The amount of time (in minutes) the user spends on the website.
- Gender: The gender of the user (male or female).

The target variable is:

- Clicked on Ad: Whether the user clicked on the ad (1) or not (0).

## Machine Learning Algorithms

Two machine learning algorithms are employed to train and evaluate the predictive model:

1. Logistic Regression: A binary classification algorithm that models the relationship between the features and the likelihood of the user clicking on the ad.
2. Naive Bayes: A probabilistic classifier that calculates the conditional probabilities of the features given the class and predicts the likelihood of the user clicking on the ad.

The dataset is split into training and testing sets, and the models are trained on the training set. The performance of the models is then evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1 score.

## Frontend

The project includes a simple frontend interface created using the Python Flask framework. The frontend allows users to input their details, including age, average area income, daily time spent on the website, and gender. Upon clicking the submit button, the model predicts whether the user will click on the ad or not.

## Usage

To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/Shreeyash01/Ads-Click-Prediction.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Navigate to the project directory: `cd Ads-Click-Prediction`
4. Run the Flask application: `python app.py`
5. Access the application in your web browser at `http://localhost:5000`

Make sure to have Python and Flask installed on your system before running the application.

## Conclusion

This project demonstrates the application of machine learning algorithms, logistic regression, and Naive Bayes, to predict whether a user will click on a specific ad. By utilizing demographic and behavioral information, the models can provide valuable insights for ad campaign optimization and targeting strategies.

Feel free to explore the code and dataset to gain a deeper understanding of the project. If you have any questions or suggestions, please don't hesitate to contact me.

Happy predicting!
