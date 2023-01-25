<a name="readme-top"></a>

<!-- PROJECT LOGO -->

<Banner Here>

<br />
<div align="center">

<h2 align="center">expenses-automation-script v1.0</h2>

  <p align="center">
    Python script to automate copy &amp; pasting expenses from unformatted bank statements for accounting.
    <br />
    <a href="https://github.com/nc1z/simple-bot-telegram"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://t.me/simple_v1_bot">View Demo</a>
    ·
    <a href="https://github.com/nc1z/simple-bot-telegram">Report Bug</a>
    ·
    <a href="https://github.com/nc1z/simple-bot-telegram">Request Feature</a>
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

- V1.0 - Work in progress
  - Able to copy text from badly formatted PDF files, and paste them onto excel or google sheets via mouse & keyboard actions.  
  - some actions are still manual (defining copy & paste coordinates with initial configuration). 
  - Food category is still manual (Prediction is not accurate for food related expenses, due to the vast variations of restaurants)
  
<!-- DEMO -->

## Usage Demo

[![image](https://user-images.githubusercontent.com/111836326/214488071-cea03180-4119-4246-a61f-bb43f0209631.png)](https://youtu.be/aTSZLJifGeU)

## Usage Guide

1. Clone Repository
2. Open project in your favorite IDE (i.e. VS Code)
3. Calibrate the line_spacing field in the Automation class (This represents the y-dist for the cursor to move between transactions in your PDF)
4. Update build_json with your own dataset and expenses, tailor it to fit your own use case
5. Run main.py in the terminal
6. dataset.json & keywords_food.json should be generated in the same directory
7. 1st prompt - select start point for copy script
8. 2nd prompt - select start point for paste script
9. Script executes successfully.

<!-- CONTACT -->

## Contact

- https://github.com/nc1z

Project Link: https://github.com/nc1z/expenses-automation-script

<p align="right">(<a href="#readme-top">back to top</a>)</p>
