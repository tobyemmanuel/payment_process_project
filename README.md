# PAYMENT PROCESSOR

## Overview

We are trying to build a payment processor. Our features include authentication, transactions, transaction, transfer with three daily sends, bill payments, data purchase, airtime, AI analysis of spending, loans, recurring bills, etc.

## Features

- Transactions.
- Recurring bills
- Loans.

## Folder structure (to improve later)

app
|
|_____config.py (configuration)
|_____models.py
|_____app.py (entry file)
|
|____routes
|       |_____ auth
|       |_____loans
|       |_____transactions
|       |_____profile
|       |_____...
|
|____templates
|       |_____ index
|       |_____ ...
|
|

## Requirements

This already exists in the requirements.txt file.
This was used to save the package requirement into the file "pip freeze > requirements.txt"

After downloading project to your PC, use this command below to setup the project.

- python -m venv venv
- Venv\Scripts\Activate (on windows only)
- source venv/bin/activate (on mac only)
- pip install -r requirements.txt
