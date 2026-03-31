# Life-Pattern-Predictor
# Life Pattern Predictor

## Overview
The Life Pattern Predictor is a Python-based application developed as part of the Python Essentials BYOP (Bring Your Own Project). The project focuses on analyzing human behavioral patterns related to forgetfulness and uses historical data to predict future actions.

In daily life, individuals often forget essential items such as keys, wallets, chargers, or important documents. This project introduces a simple predictive system that learns from past patterns and helps identify items that are likely to be forgotten.

---

## Objectives
- Record daily items carried by the user  
- Track frequently forgotten items  
- Analyze patterns in user behavior  
- Predict items likely to be forgotten  

---

## Features
- Log daily items  
- Track forgotten items  
- Predict likely forgotten items  
- Store data using JSON  
- Simple command-line interface  

---

## Technologies Used
- Python 3  
- JSON for data storage  
- IDLE (Python IDE)  

---

## Project Structure

Life-Pattern-Predictor/
│
├── main.py  
├── activity_log.json  
└── README.md  

---

## How to Run

1. Open terminal or IDLE  
2. Navigate to the project folder  
3. Run the program:

python3 main.py

---

## Usage

1. Select option to log items  
2. Enter items you plan to carry  
3. Enter items you forgot  
4. Select prediction option to view results  

---

## Working Principle

The program calculates a forgetfulness score:

Score = Times Forgotten / Times Carried

Items with higher scores are more likely to be forgotten.

---

## Limitations
- Requires manual input  
- Uses basic statistical logic  
- Accuracy improves with more data  

---

## Future Improvements
- Add graphical interface  
- Use machine learning  
- Add reminders  

---

## Author
Python Essentials BYOP Project  

---

## Conclusion
This project demonstrates how simple data tracking and analysis can help identify behavioral patterns and improve daily productivity.
