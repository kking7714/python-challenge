

```python
## Three Observed Trends from Pymoli Data Analysis
#
# Observation 1: Males dominate the gender use of the games purchased
# Observation 2: Of the age groups recorded in this data the '20-24' group is the highest user base
# Observation 3: Despite female spenders being a smaller demographic they spend more on average
#
```


```python
import pandas as pd
import numpy as np

```


```python
#read json file
data = 'purchase_data.json'
path = 'Resources/purchase_data.json'
heroes_df = pd.read_json(path)
```


```python
#Determine number of players
player_count = heroes_df["Age"].count()

```


```python
#Determine unique items from 'Item Name'
unique_items = heroes_df["Item Name"].value_counts()
#Count numberof unique items
nmbr_unique_items = unique_items.count()
```


```python
#Determine number of purchases by counting 'Price' column
number_of_purchases = heroes_df["Price"].count()

#Determine total revenue with sum of 'Price' column
total_revenue = heroes_df["Price"].sum()

#Average purchase price 
avg_purchase_price = total_revenue/number_of_purchases
```


```python
#create purchase_analysis dataframe and assign values to columns
purchase_analysis = pd.DataFrame({"Number of Unique Items":[nmbr_unique_items],
                                  "Average Price":[avg_purchase_price],
                                  "Number of Purchases":[number_of_purchases],
                                  "Total Revenue":[total_revenue]})
#set column order
purchase_analysis = purchase_analysis[["Number of Unique Items",
                                      "Average Price",
                                      "Number of Purchases",
                                      "Total Revenue"]]
```


```python
#Format Average Price and Total Revenue with '$'
purchase_analysis["Average Price"] = purchase_analysis["Average Price"].map("${0:,.2f}".format)
purchase_analysis["Total Revenue"] = purchase_analysis["Total Revenue"].map("${0:,.2f}".format)
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>63</td>
      <td>$2.92</td>
      <td>78</td>
      <td>$228.10</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Count of "Gender" values: 'Male', 'Female', 'Other / Non-Disclosed'
males = heroes_df["Gender"].value_counts()["Male"]
males_prcnt = (males/player_count) * 100


females = heroes_df["Gender"].value_counts()["Female"]
females_prcnt = (females/player_count) * 100

non_disc = heroes_df["Gender"].value_counts()["Other / Non-Disclosed"]
non_disc_prcnt = (non_disc/player_count) * 100


```


```python
#dataframe for gender demographics
gender_data = [{"Percentage of Players": males_prcnt,"Total Count": males},
               {"Percentage of Players": females_prcnt,"Total Count": females},
              {"Percentage of Players": non_disc_prcnt,"Total Count": non_disc}]

gender_df = pd.DataFrame(gender_data, index=["Male","Female","Other / Non-Disclosed"])
gender_df['Percentage of Players'] = gender_df['Percentage of Players'].map("{0:,.2f}%".format)
gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>82.05%</td>
      <td>64</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>16.67%</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.28%</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# male purchase data
m_purch = heroes_df.loc[heroes_df["Gender"]=="Male"]
m_purch_total = m_purch["Price"].sum()
m_purch_avg_n = m_purch_total / males 
m_purch_avg = m_purch["Price"].mean()


# female purchase data
f_purch = heroes_df.loc[heroes_df["Gender"]=="Female"]
f_purch_total = f_purch["Price"].sum()
f_purch_avg_n = f_purch_total / females 
f_purch_avg = f_purch["Price"].mean()

#non-disclosed purchase data
o_purch = heroes_df.loc[heroes_df["Gender"]=="Other / Non-Disclosed"]
o_purch_total = o_purch["Price"].sum()
o_purch_avg_n = o_purch_total / non_disc 
o_purch_avg = o_purch["Price"].mean()



```


```python
gender_purch_analysis = [{"Purchase Count": males,"Average Purchase Price": m_purch_avg_n,
                                       "Total Purchase Value": m_purch_total, "Normalized Totals": m_purch_avg},
                                       {"Purchase Count": females,"Average Purchase Price": f_purch_avg_n,
                                       "Total Purchase Value": f_purch_total, "Normalized Totals": f_purch_avg},
                                       {"Purchase Count": non_disc,"Average Purchase Price": o_purch_avg_n,
                                       "Total Purchase Value": o_purch_total, "Normalized Totals": o_purch_avg}]

# set indexes
gender_purch_analysis = pd.DataFrame(gender_purch_analysis, index=["Male","Female","Other / Non-Disclosed"])  

#format monetary columns
gender_purch_analysis['Average Purchase Price'] = gender_purch_analysis['Average Purchase Price'].map("${0:,.2f}".format)
gender_purch_analysis['Total Purchase Value'] = gender_purch_analysis['Total Purchase Value'].map("${0:,.2f}".format)
gender_purch_analysis['Normalized Totals'] = gender_purch_analysis['Normalized Totals'].map("${0:,.2f}".format)

#reorder columns
gender_purch_analysis = gender_purch_analysis[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]

gender_purch_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>64</td>
      <td>$2.88</td>
      <td>$184.60</td>
      <td>$2.88</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>13</td>
      <td>$3.18</td>
      <td>$41.38</td>
      <td>$3.18</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1</td>
      <td>$2.12</td>
      <td>$2.12</td>
      <td>$2.12</td>
    </tr>
  </tbody>
</table>
</div>




```python
# assign age group bins
bins = [0,9,14,19,24,29,34,39,150]
# bin names
group_ages = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

# set groups by age
heroes_df["Age Group"] = pd.cut(heroes_df["Age"],bins,labels=group_ages)
group_age = heroes_df.groupby(["Age Group"])

# count per age group
age_group_count = heroes_df["Age Group"].value_counts()
# percentage of groups
age_group_prcnt = round((age_group_count / player_count) * 100)

# calc avg price by group and format for $
age_group_avg_price = round(group_age["Price"].mean(),2).map("${:.2f}".format)

# total purchase values by group
age_group_total = group_age["Price"].sum()
# normalized?
age_group_n = round(age_group_total/age_group_count, 2)

# format $ columns
age_group_total = age_group_total.map("${:.2f}".format)
age_group_n = age_group_n.map("${:.2f}".format)

age_demo_df = pd.DataFrame({"Purchase Count": age_group_count, "Average Purchase Price": age_group_avg_price,
                           "Total Purchase Value": age_group_total, "Normalized Totals": age_group_n})

# reorder columns
age_demo_df = age_demo_df[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
age_demo_df


```


```python

screen_ns = heroes_df.groupby(["SN"])['Price'].sum()
screen_count = heroes_df.groupby(["SN"])['Price'].count()
sn_group = heroes_df.groupby(["SN"])
avg_sn = screen_ns / screen_count
avg_sn = avg_sn.map("${:.2f}".format)
screen_ns = screen_ns.map("${:.2f}".format)

top_spenders = pd.DataFrame({"Purchase Count": screen_count,"Average Purchase Price":avg_sn, "Total Purchase Value": screen_ns})

top_spenders = top_spenders.sort_values("Total Purchase Value", ascending=False)
top_spenders = top_spenders[["Purchase Count","Average Purchase Price", "Total Purchase Value"]]

top_spenders.reset_index(inplace=True)




```


```python

top_ids_sort = heroes_df.groupby("Item ID")

top_id_tot_purch = top_ids_sort["Price"].sum()


id_count = heroes_df["Item ID"].value_counts()
item_ids = heroes_df["Item ID"]
item_names = heroes_df["Item Name"]
item_price = (top_id_tot_purch/id_count)
top_id_tot_purch = top_id_tot_purch.map("${:.2f}".format)
item_price = item_price.map("${:.2f}".format)
```


```python
# Most Popular Items
top_items_df = pd.DataFrame({"Purchase Count": id_count, "Item Price": item_price, "Total Purchase Value": top_id_tot_purch})
top_items_df = top_items_df[["Purchase Count", "Item Price","Total Purchase Value"]]
top_items_df = top_items_df.sort_values("Purchase Count", ascending=False)
top_items_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>94</th>
      <td>3</td>
      <td>$3.64</td>
      <td>$10.92</td>
    </tr>
    <tr>
      <th>90</th>
      <td>2</td>
      <td>$4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>111</th>
      <td>2</td>
      <td>$1.79</td>
      <td>$3.58</td>
    </tr>
    <tr>
      <th>64</th>
      <td>2</td>
      <td>$2.42</td>
      <td>$4.84</td>
    </tr>
    <tr>
      <th>154</th>
      <td>2</td>
      <td>$4.11</td>
      <td>$8.22</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most Profitable Items

top_items_df = pd.DataFrame({"Purchase Count": id_count, "Item Price": item_price, "Total Purchase Value": top_id_tot_purch})
top_items_df = top_items_df[["Purchase Count", "Item Price","Total Purchase Value"]]
top_items_df = top_items_df.sort_values("Total Purchase Value", ascending=False)
top_items_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>117</th>
      <td>2</td>
      <td>$4.71</td>
      <td>$9.42</td>
    </tr>
    <tr>
      <th>93</th>
      <td>2</td>
      <td>$4.49</td>
      <td>$8.98</td>
    </tr>
    <tr>
      <th>90</th>
      <td>2</td>
      <td>$4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>154</th>
      <td>2</td>
      <td>$4.11</td>
      <td>$8.22</td>
    </tr>
    <tr>
      <th>180</th>
      <td>2</td>
      <td>$2.77</td>
      <td>$5.54</td>
    </tr>
  </tbody>
</table>
</div>


