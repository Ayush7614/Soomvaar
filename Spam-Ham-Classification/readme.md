# Spam-Ham-Classification

Opensource work done for my mentorship program Delta Winter of Code

![download (1)](https://user-images.githubusercontent.com/88154798/144704979-82add8f2-c817-4b3e-a786-293db7e1ecfe.jpg)


## Problem Statement:
<p>Given a text input by the user we have to classify whether the message is spam or ham.</p>

## Approach used
<p>The main goal of this project is to detect spam messages .</p>

->> Data Analysis        : I started Analysing dataset using pandas. 

->> Preprocessing        : Removed stopwords and converted all left words to root form.

->> Bag of Words         : Count VEctorizer used to genrate bag of words.

->> Model                : Naive Bayes model used and tested for different test/train split .


## Output:

![Screenshot (1656)](https://user-images.githubusercontent.com/88154798/144705254-16fefb04-abcd-4fc5-a383-50cd8e954cbb.png)


Accuracy Graph where Naive Bayes model having 6302 features and train/test split of 0.2 produced highest accuracy of 0.9847533632286996

Confusion Matrix for best case 

![Screenshot (1658)](https://user-images.githubusercontent.com/88154798/144705692-dc1ff5e0-2c6d-45ce-afb8-21b008e976fb.png)
