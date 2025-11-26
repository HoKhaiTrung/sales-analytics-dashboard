import pandas as pd
from project import load_data, calculate_summary, top_products, monthly_trend, region_performance

def test_load_data():
    df = load_data("sales.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty #DataFrame is not empty
    assert "sales" in df.columns #Important columns exist
    assert df["sales"].isnull().sum() == 0 #No missing values
    assert df["order_date"].dtype.kind == "M" #date column is correctly converted

def test_calculate_summary():
    df = load_data("sales.csv")
    summary = calculate_summary(df)
    assert isinstance(summary, dict) #check if the summary is a dictionary
    expected = ["total_revenue", "total_units", "total_profit", "aov", "unique_product", "sales_std", "sales_95th_percentile"]
    for key in expected:
        assert key in summary
    #check all keys exist in the dictionary

def test_top_products():
    df = load_data("sales.csv")
    top = top_products(df)
    assert isinstance(top, pd.Series)
    assert  len(top) > 0 #check that is has results

def test_monthly_trend():
    df = load_data("sales.csv")
    trend = monthly_trend(df)
    assert isinstance(trend, pd.Series)
    assert len(trend) > 0
    assert trend.index.dtype.kind == "M"

def test_region_performance():
    df = load_data("sales.csv")
    region = region_performance(df)
    assert isinstance(region, pd.Series)
    assert len(region) > 0
    expected = ["South", "Central", "East", "West"]
    for key in expected:
        assert key in region.index

