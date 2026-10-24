# Email Spam Detection with Machine Learning

## Project Overview
This project uses machine learning to classify SMS messages as **Spam** or **Ham (Not Spam)**. It uses text preprocessing and TF-IDF to convert messages into numerical features.

## Dataset
The project uses an SMS Spam Collection dataset containing 5,572 messages:
- Ham messages: 4,825
- Spam messages: 747

## Technologies Used
- Python
- Google Colab
- Pandas
- NLTK
- Scikit-learn

## Project Workflow
1. Load the SMS dataset.
2. Check missing values and class distribution.
3. Convert messages to lowercase and remove punctuation and stopwords.
4. Convert text into numerical features using TF-IDF.
5. Split the dataset into training and testing sets.
6. Train Multinomial Naive Bayes and Logistic Regression models.
7. Evaluate both models using accuracy, precision, recall, F1-score, and confusion matrices.
8. Test the model with a new message.

## Results

| Metric | Naive Bayes | Logistic Regression |
|---|---:|---:|
| Accuracy | 96.32% | 95.87% |
| Precision | 100% | 100% |
| Recall | 72.48% | 69.13% |
| F1-score | 84.05% | 81.75% |

Naive Bayes performed slightly better than Logistic Regression on the test dataset.

## Conclusion
This project demonstrates how machine learning can identify spam messages using text processing and classification algorithms. The results show that both models perform well, although some spam messages are still missed.

## Project File
`Email_Spam_Detection.ipynb` contains the Python code, explanations, model training, evaluation, and message prediction.

