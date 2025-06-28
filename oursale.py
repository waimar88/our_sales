import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('all_df.csv')
st.set_page_config(page_title='My Sale Dashboard',page_icon=':bar_chart:')
st.sidebar.header('Please filter here')
user_product = st.sidebar.multiselect(
    'Select Product',
    options = df['Product'].unique(),
    default = df['Product'].unique() [:5]
)
user_city = st.sidebar.multiselect(
    'Select City',
    options = df['City'].unique(),
    default = df['City'].unique() [:5]
)
user_month = st.sidebar.multiselect(
    'Select Month',
    options = df['Month'].unique(),
    default = df['Month'].unique() [:5]
)
st.title(':bar_chart: Sales Dashboard for 2019')
our_total = df['Total'].sum()
no_of_product = df['Product'].nunique()
left_col, right_col = st.columns(2)
with left_col:
    st.subheader('Total Sales')
    st.subheader(f'US ${our_total}')
with right_col:
    st.subheader('No. of Product')
    st.subheader(f'{no_of_product}')
user_select = df.query('Product == @user_product and City == @user_city and Month == @user_month')
sale_by_product = user_select.groupby('Product') ['Total'].sum().sort_values()
fig_sale_by_product = px.bar(
    sale_by_product, 
    x= sale_by_product.values,
    y= sale_by_product.index,
)
sale_by_month = user_select.groupby('Month') ['Total'].sum().sort_values()
fig_sale_by_month = px.bar(
    sale_by_month, 
    x= sale_by_month.values,
    y= sale_by_month.index,
)
sale_by_city = user_select.groupby('City')['Total'].sum().sort_values()
fig_sale_by_city = px.pie(
    sale_by_city, 
    values= sale_by_city.values,
    names= sale_by_city.index, 
    title='Sales by City'
)
a,b,c = st.columns(3)
a.plotly_chart(fig_sale_by_product,use_container_width = True)
b.plotly_chart(fig_sale_by_city,use_container_width = True)
c.plotly_chart(fig_sale_by_month,use_container_width = True)
fig_sale_by_month_line = px.line(
    fig_sale_by_month, 
    x= sale_by_month.values,
    y= sale_by_month.index, 
    title='Sales by Month Line Chart'
)
fig_scatter = px.scatter(
    df, 
    x= 'Total',
    y= 'QuantityOrdered', 
    title='Sales by Amount Quantity'
)
d,e = st.columns(2)
d.plotly_chart(fig_sale_by_month_line,use_container_width = True)
e.plotly_chart(fig_scatter,use_container_width = True)