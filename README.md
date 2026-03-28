# vityarthi-project-credit-card-fraud-detection


## INTRODUCTION

This project is a simple and straightforward Python tool for credit card fraud detection based on a set of rules. It demonstrates how a system can be designed easily to check and flag potential fraud based on logical indicators. It is a learning tool which can demonstrates the basics of how a fraud detection system works and to solve real life problem.

## WHAT THIS PROJECT DOES

- It processes credit card transactions based on a set of rules
- It provides a risk score for each transaction
- It classifies each transaction into Normal, Suspicious, or Fraudulent
- It is intended to help users understand the logic of fraud detection
- It offers a simple and clear implementation of a Python tool that can be customized and used appropriately.

## HOW THE SYSTEM WORKS

The system takes transaction details on:
- Amount
- Location
- Normal location
- Time
- Frequency

### How it determines the level of risk:
- If the amount is higher than 50,000
- If the location is not the normal location
- If there are more than five transactions within the last hour
- If the transaction is made during odd hours (before 6 am or after 10 pm)


### Classification of the level of risk:
- Normal (low risk)
- Suspicious (medium risk)
- Fraudulent (high risk)


 ## HOW TO SET IT UP

### Step 1: Confirm Python is installed in your system

To ensure that Python 3.x is installed on your device, type the following command:
```bash
python --version
```
If Python is not installed on your device, please download it from:
https://www.python.org/

### Step 2: Clone the code and run the program

To clone the code repository:
```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```
Alternatively, you can also download a ZIP file from the repository.
Then run the program.


## CUSTOMIZING THE PROJECT

The system also offers several choices for customization:
### Change the risky rules
  - Change the check_fraud function by adding new conditions or modifying existing ones.

### Add more transactions
  - Just add more dictionaries to the transactions list.

### Integrate real data
  - Replace the dummy data with real data from users, CSV files, or databases.

### Future enhancements
  - There are a number of ways this project can be extended to a more sophisticated system:
    - Machine Learning Model
    - Web Application
    - Database
    - Real-time Fraud Alerts
    - Visualization Tool


## LIMITATIONS
- The system is based on a non-adaptive and simple rule-based system.
- The system is not suitable for real-time processing.
- The system cannot learn from past experiences.
  

## LEARNING OUTCOMES

By working on this project, you will gain a clear and proper understanding of how fraud detection systems can be built using basic programming concepts. You will also learn about conditional logic, risk scoring, and how different factors influence decision-making in real-world systems and problem solving.

## CONTRIBUTING

Here's how you can contribute:

-Improve the detection logic

-Add new features

-Optimize the code

### Steps:

-Fork the repository

-Create a new branch

-Make your changes

-Submit a pull request


