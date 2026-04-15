# Exploratory Data Analysis on Superstore Dataset

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Superstore dataset to uncover business insights related to sales, profit, discounts, product categories, and regional performance.

The objective is to identify patterns, trends, and problem areas that can help improve business decision-making.

---

## Dataset Information

* **Dataset Name:** Sample Superstore
* **Total Records:** 9,977
* **Total Features:** 13

### Features Used

* Ship Mode
* Segment
* Country
* City
* State
* Postal Code
* Region
* Category
* Sub-Category
* Sales
* Quantity
* Discount
* Profit

---

## Project Objectives

* Understand sales and profit distribution
* Identify top-performing and loss-making product categories
* Analyze discount impact on profitability
* Evaluate sub-category performance
* Explore relationships among numerical variables

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Exploratory Data Analysis Performed

### Data Cleaning

* Checked for missing values
* Removed duplicate records
* Validated data types

### Analysis Conducted

* Sales Distribution Analysis
* Profit Distribution Analysis
* Category-wise Sales Analysis
* Sub-Category Profit Analysis
* Discount vs Profit Analysis
* Correlation Heatmap

---

## Key Insights

### Sales Insights

* Sales distribution is positively skewed with presence of high-value outliers.
* Most transactions are low-to-medium value orders.

### Profit Insights

* Profit distribution shows large variability with several loss-making transactions.
* Certain orders incur significant losses.

### Category Performance

* Technology generates the highest sales among all categories.
* Office Supplies has the lowest sales contribution.

### Sub-Category Performance

* Copiers are the most profitable sub-category.
* Tables generate the highest losses.

### Discount Analysis

* Higher discounts strongly reduce profitability.
* Discounts above 50% frequently lead to negative profit.

### Correlation Findings

* Sales and Profit have moderate positive correlation (0.48).
* Discount and Profit have negative correlation (-0.22).

---

## Business Recommendations

* Reassess discount strategy to avoid excessive profit erosion.
* Investigate loss-making sub-categories such as Tables and Bookcases.
* Focus marketing and inventory efforts on high-performing products like Copiers and Technology.
* Optimize pricing for low-margin products.

---

## Project Structure

```bash
Sample-Superstore-EDA/
│
├── SampleSuperstore.csv
├── EDA_Superstore.ipynb
├── README.md
└── visualizations/
```

---

## Conclusion

The analysis reveals that while the business generates strong revenue through Technology and high-performing sub-categories, profitability is significantly affected by aggressive discounting and loss-making products. Strategic pricing and discount optimization can improve overall business performance.

---

## Author

**Aryan Gupta**

---

## Connect With Me

* LinkedIn:www.linkedin.com/in/aryan-gupta-3594183a8
* GitHub:(https://github.com/Aryanplz)
