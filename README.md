# PyPoll & PyBank Analysis

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)](https://www.python.org/downloads/)  
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/license/mit)

## 📌 Project Overview
This repository contains two Python scripts for financial and election data analysis:
- **PyPoll**: Analyzes election results from a CSV file and determines the winner based on vote counts.
- **PyBank**: Analyzes financial records to calculate total profits/losses, the greatest increase and decrease in profits, and the average change in profit over time.

## 📂 Directory Structure
```
project-directory/
│── PyBank/
│   │── resources/  # Folder for input CSV files
│   │── analysis/   # Folder for output TXT reports
│   │── main.py  # Financial analysis script
│
│── PyPoll/
│   │── resources/  # Folder for input CSV files
│   │── analysis/   # Folder for output TXT reports
│   │── main.py  # Election analysis script
│
│── Screenshots/  # Folder containing screenshots
│── README.md  # Project documentation
```

## 🚀 Features
### PyPoll:
✅ Reads election data from a CSV file.  
✅ Computes the total number of votes cast.  
✅ Determines each candidate’s vote count and percentage.  
✅ Declares the election winner.  
✅ Outputs the results to the console and a text file.

### PyBank:
✅ Reads financial data from a CSV file.  
✅ Computes the total number of months in the dataset.  
✅ Calculates the total profit/loss over the period.  
✅ Determines the average change in profit/loss.  
✅ Identifies the greatest increase and decrease in profits.  
✅ Outputs the results to the console and a text file.

## 📥 Installation & Usage
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Clone the Repository
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Run PyPoll
```sh
python PyPoll/main.py
```

### Run PyBank
```sh
python PyBank/main.py
```

## 📌 Example Output
### PyPoll Output (Console)
![image](https://github.com/user-attachments/assets/af064b01-7989-4b68-9488-9c7761e03488)

### PyPoll Output (election_analysis)
![image](https://github.com/user-attachments/assets/6b81ba8b-3c4d-4a45-8e2c-1250e6fb2922)

### PyBank Output (Console & budget_analysis)
![image](https://github.com/user-attachments/assets/d036add4-d2ee-4399-bed6-16197e71b373)

```

## 🛠️ Technologies Used
- Python
- CSV Module
- OS Module
- Time Module (for PyPoll loading indicator)

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## 📞 Contact
For any questions, reach out via GitHub or email: [your-email@example.com](mailto:your-email@example.com)

## Acknowledgments

This project was developed with the assistance of the following resources:

- **"U of T" (Turtoring Session - Xpert Learning Assistant - GitLab Activites)** – Provided guidance on code and explanations.
- **ChatGPT** – Assisted with code, explanations, and README formatting. 
