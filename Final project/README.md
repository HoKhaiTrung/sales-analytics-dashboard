# MYPROJECT TITLE: Sales Analytics Dashboard
#### Video Demo:  https://www.youtube.com/watch?v=TIv35Ebm1WE
## Description:
    This Python project is a command-line sales analytics dashboard built for the CS50P final project. It reads a dataset of retail transactions, cleans and prepares the data, and provides several useful business insights through a simple menu-based interface.

    The program calculates key performance indicators such as total revenue, total units sold, total profit, average order value, number of unique products, and basic NumPy-based statistics. It also identifies the top-selling products, computes month-by-month revenue trends, and evaluates sales performance across regions. Each of these outputs can be viewed as text or visualized using matplotlib charts.

    The goal of the project is to demonstrate practical data-analysis skills using Python, including data cleaning with pandas, numerical analysis with NumPy, and basic visualization with matplotlib. The tool is designed for learners or analysts who want a lightweight way to explore sales data directly from the terminal

## Features:
    Data Loading & Cleaning: Reads a sales CSV file, sanitizes column names, converts dates, and handles missing or invalid values.

    Summary KPIs: Computes total revenue, total units sold, total profit, average order value (AOV), unique product count, sales standard deviation, and 95th percentile of sales.

    Top Products Analysis: Identifies the best-performing products based on total revenue and displays the top N items.

    Monthly Revenue Trend: Aggregates revenue by month to show seasonality and sales patterns over time.

    Regional Performance: Groups sales by region to show which geographic areas generate the most revenue.

    Data Visualization: Uses matplotlib to render bar charts, line charts, and horizontal bar charts directly from the menu.

    Interactive Menu: A simple command-line interface that lets users select which analysis they want to view

## How to run:
    1.Install the required libraries: Before running the program, install the project dependencies
        pip install -r requirements.txt

    2.Make sure the dataset is in the same folder: In the same directory as project.py.
        sales.csv

    3.Run the dashboard
        python project.py

    4.Choose an option from the menu: After starting the program, you will see a menu
        1. View summary KPIs
        2. View top products
        3. View monthly revenue trend
        4. View region performance
        5. Exit

    5.Type the number of the analysis you want to run and press Enter.

## Technologies Used:
    Python: core programming language used for the project

    Pandas: for loading, cleaning, grouping, and aggregating sales data

    NumPy: for numerical calculations such as standard deviation and percentiles

    Matplotlib: for generating visualizations, including bar charts and line charts

    CSV dataset: “sales.csv”, containing retail transaction records used for analysis

## File Structure:
    project.py: Main application containing all functions and the menu interface

    test_project.py: Unit tests for the main functions

    requirements.txt: List of external Python libraries used

    README.md: Project documentation

    sales.csv: Dataset used for analysis (Superstore sample data)




