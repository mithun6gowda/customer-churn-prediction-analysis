Customer Churn Prediction Application

Case Study of Customer Churn Prediction Model
Creating churn prediction models involves using historical customer data to predict the likelihood of the current customer leaving or continuing with a particular service/product. The data used for the predictive models include product usage data and direct customer feedback. Besides, the predictive models identify the different trends and patterns in the data to forecast customer churn.

Consider an e-commerce company with historical data on how their clients have interacted with their services. The company wants to know the likelihood of customers churning so they can launch targeted marketing campaigns.

[DataSource](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data)

The data is in .xlsx format with the following features:

| Feature Name                | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| CustomerID                 | Unique customer ID                                                         |
| Churn                      | Flag indicating whether the customer churned (1) or not (0)               |
| Tenure                     | Tenure of the customer in the organization                                 |
| PreferredLoginDevice       | Preferred login device (e.g., mobile, web)                                 |
| CityTier                   | City tier classification (Tier 1, Tier 2, Tier 3)                          |
| WarehouseToHome            | Distance between warehouse and customer's home                             |
| PreferredPaymentMode       | Preferred payment method (credit card, debit card, cash on delivery)       |
| Gender                     | Gender of the customer                                                     |
| HourSpendOnApp             | Hours spent on mobile app or website                                       |
| NumberOfDeviceRegistered   | Number of devices registered to the account                                |
| PreferedOrderCat           | Preferred order category in the last month                                 |
| SatisfactionScore          | Customer satisfaction score                                                |
| MaritalStatus              | Marital status of the customer                                             |
| NumberOfAddress            | Number of addresses linked to the account                                  |
| OrderAmountHikeFromlastYear| % increase in order value vs last year                                     |
| CouponUsed                 | Coupons used in the last month                                             |
| OrderCount                 | Orders placed in the last month                                            |
| DaySinceLastOrder          | Days since last order                                                      |
| CashbackAmount             | Average cashback received in the last month                                |

Application Input User Interface

![alt text](data/ui.png.png)

Application Result User Interface

![alt text](data/result.png.png)