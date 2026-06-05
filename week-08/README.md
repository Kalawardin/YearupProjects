# Author
Fuat Berk Baslar

## Here's my video link : https://1drv.ms/p/c/2929fec8c2de0b8a/IQAgKU32YOhfTrsT6odmCGqBAc1DnoUnUY1xeyyv3j5fLSY


# Lana Ilana Territory: Sales Performance Analysis

A four-year sales analysis for the Lana Ilana territory, covering the period from January 2022 to December 2025. This project looks at revenue trends, store performance, customer behavior, and product categories to find clear actions the territory can take to grow.

## Overview

The goal of this project is to answer four main questions:

1. How has total revenue changed over the four years?
2. Which stores perform best, and which need help?
3. Who are the most valuable customers, and how does the rewards program affect spending?
4. Which product categories drive the most revenue?

The analysis ends with a list of recommendations based on the findings.

## Data Sources

The project uses five CSV files:

| File | What it contains |
|---|---|
| `StoreSales.csv` | Every transaction: date, store, product, customer, amount |
| `StoreDetail.csv` | Store information: city, state, territory manager |
| `Products.csv` | Product list with category links |
| `ProductCategories.csv` | Category names |
| `customer_list.csv` | Customer names and emails (separator: `\|`) |

The five files are joined together using shared keys: `Store ID`, `Prod Num`, `CategoryID`, and `RewardsID` (which matches `cust_id` in the customer file).

## Tools Used

- **Python 3**
- **pandas** — for data cleaning, merging, and grouping
- **matplotlib** — for charts
- **Jupyter Notebook** — for the analysis
- **PowerPoint** — for the final presentation

## How to Run

1. Clone or download this repository.
2. Make sure all five CSV files are in the same folder as the notebook.
3. Install the required libraries:
   ```
   pip install pandas matplotlib jupyter
   ```
4. Open the notebook:
   ```
   jupyter notebook Baslar_sales_analysis.ipynb
   ```
5. Run the cells in order from top to bottom.

## Project Files

```
.
├── Baslar_sales_analysis.ipynb   # Main analysis notebook
├── capstone2.pptx                # Final presentation
├── README.md                     # This file
└── data/
    ├── StoreSales.csv
    ├── StoreDetail.csv
    ├── Products.csv
    ├── ProductCategories.csv
    └── customer_list.csv
```

## Key Findings

**Revenue grew by 150% over four years.** Total revenue went from $598K in 2022 to $1.50M in 2025. Total revenue across the full period was $3.93M. The best single month was October 2025, with $188K.

**Growth was not steady.** There was a big jump between 2022 and 2023 (+53%), then a flat year in 2024, and a sharp rise starting in late 2024 that continued through 2025 (+63%).

**Two stores drive 30% of revenue.** Store 724 (Miami, Florida) and Store 728 (Tallahassee, Florida) outperform the other nine stores by a wide margin.

**The top 5 customers spend 5x more than the average.** Top 5 customers spend about $4,217 each, compared to $844 for the average rewards customer.

**Only 10.6% of transactions use the rewards program.** This means we have limited information about most of our customers, but it also shows there is room to grow the program.

**Two categories make 88% of revenue.** Technology & Accessories is 62.7%, and Textbooks is 25.2%. The other three categories together make only 12%.

## Recommendations

1. **Study and copy the Florida model.** Find what stores 724 and 728 do well, and apply it to the other nine stores.
2. **Grow the rewards program.** Add sign-up steps at checkout to bring the rate from 10.6% to a higher level.
3. **Add variety to the product mix.** Reduce the risk of being too dependent on Technology and Textbooks.
4. **Find the cause of the late-2024 growth.** If we know what started it, we can repeat it in 2026.

## Possible Next Steps

- Look at rewards program rates by store (do Florida stores enroll more customers?).
- Check if the top 5 customers are frequent shoppers or rare big buyers.
- Compare seasonal patterns (do some months always perform better?).
- Add a category-level study of the late-2024 growth — was it driven by Technology only, or by multiple categories?


