# Topsis Score Calculator

The TOPSIS Score Calculator is a Django-based web application designed to facilitate informed decision-making by leveraging the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. This powerful multi-criteria decision analysis tool enables users to make complex choices by assessing alternatives based on multiple criteria, providing an objective and systematic approach to decision-making.

TOPSIS is a widely-recognized decision-making method, employed across various fields such as engineering, economics, and management. By evaluating the proximity of alternatives to an ideal solution, TOPSIS empowers users to make data-driven decisions that consider multiple dimensions.

With the TOPSIS Score Calculator, users can harness the power of this technique through an intuitive, easy-to-use interface that streamlines the process of scoring and ranking alternatives.

## Live Link

Project Link: http://rohan7grover.pythonanywhere.com/

PyPI Package Link: https://pypi.org/project/Topsis-Rohan-102003029/1.0.0/

## Installation

Clone the project

```bash
  git clone https://github.com/rohan7grover/Topsis-Score-Calculator.git
```

Go to the project directory

```bash
  cd Topsis-Score-Calculator
```

Create a Virtual Environment

```bash
  python -m venv myenv
```

Activate the Virtual Environment (Linux/macOS)

```bash
  source myenv/bin/activate
```

Activate the Virtual Environment (Windows)

```bash
  myenv\Scripts\activate.bat
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Email Configuration

To enable the email functionality in this application, you need to configure the email settings in the `topsis_web_app/settings.py` file. Follow these steps:

Locate the following lines:

```bash
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
```

Replace the empty strings with your email credentials:

```bash
  EMAIL_HOST_USER = 'your_email@example.com'
  EMAIL_HOST_PASSWORD = '*********'
```

Save the changes to the `settings.py` file.

## Run Locally

Execute the following command in the terminal:

```bash
python manage.py runserver
```

## Example

Upload the csv file, enter the _weights_ with values separated by commas, followed by the _impacts_ with comma separated signs _(+,-)_.
Enter your email and click on `Calculate` button to recive your result.

### Input:

#### sample.csv

A csv file showing data for different mobile handsets having varying features.

| Model  | Storage space(in gb) | Camera(in MP)| Price(in $)  | Looks(out of 5) |
| :----: |:--------------------:|:------------:|:------------:|:---------------:|
| M1 | 16 | 12 | 250 | 5 |
| M2 | 16 | 8  | 200 | 3 |
| M3 | 32 | 16 | 300 | 4 |
| M4 | 32 | 8  | 275 | 4 |
| M5 | 16 | 16 | 225 | 2 |

weights vector = [ 0.25 , 0.25 , 0.25 , 0.25 ]

impacts vector = [ + , + , - , + ]

### Output:

| Model  | Storage space(in gb) | Camera(in MP)| Price(in $)  | Looks(out of 5) | Topsis Score | Rank |
| :----: |:--------------------:|:------------:|:------------:|:---------------:| :---: | :---: |
| M1 | 16 | 12 | 250 | 5 | 0.534277 | 3
| M2 | 16 | 8  | 200 | 3 | 0.308368 | 5
| M3 | 32 | 16 | 300 | 4 | 0.691632 | 1
| M4 | 32 | 8  | 275 | 4 | 0.534737 | 2
| M5 | 16 | 16 | 225 | 2 | 0.401046 | 4

## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/85683864/227775815-0c375a6b-1f27-4570-b297-7a158d8d5bb6.png)

