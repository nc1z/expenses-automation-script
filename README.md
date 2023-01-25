<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<div align="start">

# 📃expenses-automation-script v1.0
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge) ![Google Sheets Badge](https://img.shields.io/badge/Google%20Sheets-34A853?logo=googlesheets&logoColor=fff&style=for-the-badge) ![Microsoft Excel Badge](https://img.shields.io/badge/Microsoft%20Excel-217346?logo=microsoftexcel&logoColor=fff&style=for-the-badge)
  <p align="start">
    Python script to automate copy &amp; pasting expenses from unformatted bank statements for accounting.
    <br />
    <a href="#about-the-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/aTSZLJifGeU" target="_blank">View Demo</a>
    ·
    <a href="https://github.com/nc1z/expenses-automation-script">Report Bug</a>
    ·
    <a href="https://github.com/nc1z/expenses-automation-script">Request Feature</a>
  </p>
</div>

<hr/>

<!-- ABOUT THE PROJECT -->

## About The Project

Script to automate copy &amp; pasting expenses from unformatted bank statements for accounting purposes.

This automation project was inspired by the lack of proper xls/csv exporting options from certain banks (e.g. CITI), where we only have a CITI mobile app that provides billing statements in PDF. This was a tedious format to clean and transfer onto spreadsheet programs.

With this script, we can automate the copy & pasting, as well as formating/categorizing of our expenses with ease. This script can be tweaked to serve any other copy/pasting purposes as well.

Written with PyAutoGUI, Pynput, Pyperclip and Natural Language Toolkit (NLTK).

**Libraries Used:**

- PyAutoGUI - Automating mouse and keyboard actions such as clicking and typing
- Pynput - Event listeners to store variables
- Pyperclip - Clipboard for pasting data
- NLTK - Provides tools to work with human language data. Specifically this script uses a class in the NLTK.classify module, NaiveBayesClassifier, that provides an implementation of the Naive Bayes algorithm for text classification. This machine learning techniques help to predict & classify our expenses category

<!-- RELEASE -->

## Release & Updates
- V1.1 - Work in progress
  - Text recognition, planning to remove some of V1.0 's manual tasks
- V1.0 
  - Able to copy text from badly formatted PDF files, and paste them onto excel or google sheets via mouse & keyboard actions.  
  - some actions are still manual (defining copy & paste coordinates with initial configuration). 
  - Food category is still manual (Prediction is not accurate for food related expenses, due to the vast variations of restaurants)
  
<!-- DEMO -->

## Usage Demo

[![image](https://user-images.githubusercontent.com/111836326/214488071-cea03180-4119-4246-a61f-bb43f0209631.png)](https://youtu.be/aTSZLJifGeU)

## Usage Guide

1. Clone Repository
2. Open project in your favorite IDE (i.e. VS Code)
3. Install dependencies (libraries)
4. Calibrate the line_spacing field in the Automation class (This represents the y-dist for the cursor to move between transactions in your PDF)
5. Update build_json with your own dataset and expenses, tailor it to fit your own use case
6. Run main.py in the terminal
7. dataset.json & keywords_food.json should be generated in the same directory
8. 1st prompt - select start point for copy script
9. 2nd prompt - select start point for paste script
10. Script executes successfully.

<!-- CONTACT -->

## Contact

- https://github.com/nc1z

Project Link: https://github.com/nc1z/expenses-automation-script

<p align="right">(<a href="#readme-top">back to top</a>)</p>
