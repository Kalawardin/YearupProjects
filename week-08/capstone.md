# Welcome to YearUp Capstone_2 Project!

Here's my video link : https://1drv.ms/p/c/2929fec8c2de0b8a/IQAgKU32YOhfTrsT6odmCGqBAc1DnoUnUY1xeyyv3j5fLSY

A four-year sales analysis for the Lana Ilana territory, covering the period from January 2022 to December 2025. This project looks at revenue trends, store performance, customer behavior, and product categories to find clear actions the territory can take to grow.

# Overview
The goal of this project is to answer four main questions:

- How has total revenue changed over the four years?
- Which stores perform best, and which need help?
- Who are the most valuable customers, and how does the rewards program affect spending?
- Which product categories drive the most revenue?
- The analysis ends with a list of recommendations based on the findings.

# Data Sources
The project uses five CSV files:
FileWhat it containsStoreSales.csvEvery transaction: date, store, product, customer, amountStoreDetail.csvStore information: city, state, territory managerProducts.csvProduct list with category linksProductCategories.csvCategory namescustomer_list.csvCustomer names and emails (separator: |)

The five files are joined together using shared keys: Store ID, Prod Num, CategoryID, and RewardsID (which matches cust_id in the customer file).

# Tools Used
Python 3
pandas — for data cleaning, merging, and grouping
matplotlib — for charts
Jupyter Notebook — for the analysis
PowerPoint — for the final presentation

# Key Findings
- Revenue grew by 150% over four years. Total revenue went from $598K in 2022 to $1.50M in 2025. Total revenue across the full period was $3.93M. The best single month was October 2025, with $188K.
- Growth was not steady. There was a big jump between 2022 and 2023 (+53%), then a flat year in 2024, and a sharp rise starting in late 2024 that continued through 2025 (+63%).
- Two stores drive 30% of revenue. Store 724 (Miami, Florida) and Store 728 (Tallahassee, Florida) outperform the other nine stores by a wide margin.
- The top 5 customers spend 5x more than the average. Top 5 customers spend about $4,217 each, compared to $844 for the average rewards customer.
- Only 10.6% of transactions use the rewards program. This means we have limited information about most of our customers, but it also shows there is room to grow the program.
- Two categories make 88% of revenue. Technology & Accessories is 62.7%, and Textbooks is 25.2%. The other three categories together make only 12%.
