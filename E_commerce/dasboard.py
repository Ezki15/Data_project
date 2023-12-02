import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data 
df = pd.read_csv("product_order.csv")
df_state = pd.read_csv("customer_order.csv")


# Sidebar
st.sidebar.title('Top N Filter')
top_n = st.sidebar.slider('Select Top N', 1, 10, 5)

# Filter data
filtered_data = df.nlargest(top_n, 'number_of_order')
filtered_data_state = df_state.nlargest(top_n, 'number_of_order')

# Visualisasi
st.title("Dasboard")
colors = ["#82b084", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
st.subheader('Top N Product with Highest Orders')
fig, ax = plt.subplots()
sns.barplot(x='number_of_order', y='product', data=filtered_data, palette=colors, ax=ax)
ax.set(xlabel=None, ylabel=None)
st.pyplot(fig)

st.subheader("States with the most orders")
fig, ax1 = plt.subplots()
sns.barplot(x='customer_state', y='number_of_order', data=filtered_data_state, palette=colors, ax=ax1)
for i, value in enumerate(filtered_data_state['number_of_order']):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom', size=8)
ax1.set_yticks([])
ax1.set(xlabel="State", ylabel="Orders")
st.pyplot(fig)



