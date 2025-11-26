import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(sales):
    #read the data
    df = pd.read_csv(sales)

    #Trim and sanitize column names
    df.columns = [column.strip().lower().replace(' ', '_') for column in df.columns]

    #convert to date time
    df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')

    #drop the missing values for specific columns
    df.dropna(subset=["order_date", "product_name", "sales", "quantity"], inplace=True)

    #converting numeric columns into real numeric types
    numeric_columns = ["sales", "quantity", "profit"]
    for numeric_column in numeric_columns:
        df[numeric_column] = pd.to_numeric(df[numeric_column], errors='coerce')
    df.dropna(subset=numeric_columns, inplace=True)

    return df

def calculate_summary(df):
    total_revenue = df["sales"].sum()
    total_units = df["quantity"].sum()
    total_profit = df["profit"].sum()

    #Average order value (AOV)
    aov = total_revenue / df.shape[0]

    #unique product count
    unique_product = df["product_name"].nunique()

    #Standard deviation of sales
    sales_std = np.std(df["sales"].values)

    # 95th percentile of sales
    percentile_95 = np.percentile(df["sales"].values, 95)

    return {
        "total_revenue": float(total_revenue),
        "total_units": int(total_units),
        "total_profit": float(total_profit),
        "aov": float(aov),
        "unique_product": int(unique_product),
        "sales_std": sales_std,
        "sales_95th_percentile": percentile_95
    }


#Identify the top-selling products based on total revenue
def top_products(df, n =5):
    top_product = df.groupby(["product_name"])["sales"].sum()
    top_product_sorted = top_product.sort_values(ascending=False)
    return top_product_sorted.head(n)

#How does revenue change month by month
def monthly_trend(df):
    df = df.set_index("order_date")
    monthly_sales = df.resample("M")["sales"].sum() #Group the data by month
    return monthly_sales

#Which regions generate the most revenue?
def region_performance(df):
    region_performance = df.groupby("region")["sales"].sum()
    region_performance_sorted = region_performance.sort_values(ascending=False)
    return region_performance_sorted

def main():
    df = load_data("sales.csv")
    print("""
            --- SALES DASHBOARD ---
            1. View summary KPIs
            2. View top products
            3. View monthly revenue trend
            4. View region performance
            5. Exit
            """)
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            summary = calculate_summary(df)
            for key, value in summary.items():
                print(f"{key}: {value:,.2f}" if isinstance(value, float) else f"{key}: {value}")

        elif user_choice == "2":
            top = top_products(df)
            print(top)

            top.plot.bar()
            plt.ylabel("Revenue")
            plt.xlabel("Product Name")
            plt.title("Top Products by Revenue")
            plt.show()
        elif user_choice == "3":
            monthly = monthly_trend(df)
            print(monthly)

            monthly.plot()
            plt.title("Monthly Sales Revenue")
            plt.ylabel("Revenue")
            plt.tight_layout()
            plt.show()
        elif user_choice == "4":
            region = region_performance(df)
            print(region)

            region.plot.barh()
            plt.title("Revenue by Region")
            plt.ylabel("Region")
            plt.xlabel("Revenue")
            plt.tight_layout()
            plt.show()
        elif user_choice == "5":
            break


if __name__ == "__main__":
    main()