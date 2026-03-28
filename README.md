# vityarthi-project-credit-card-fraud-detection


## Introduction

This project is a simple and straightforward Python tool for credit card fraud detection based on a set of rules. It demonstrates how a system can be designed to check and flag potential fraud based on logical indicators. It is a learning tool and demonstrates the basics of how a fraud detection system works.

## What this project does

- It processes credit card transactions based on a set of rules
- It provides a risk score for each transaction
- It classifies each transaction into Normal, Suspicious, or Fraudulent
- It is intended to help users understand the logic of fraud detection
- It offers a simple and clear implementation of a Python tool that can be customized

## How the system works

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
