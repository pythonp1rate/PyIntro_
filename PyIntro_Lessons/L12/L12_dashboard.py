import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Set page config for better layout
st.set_page_config(
    page_title="📊 Advanced Streamlit Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def create_sample_data():
    """Create sample datasets for the dashboard"""
    # Sales data
    # With pandas date_range we create a range of dates
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    sales_data = pd.DataFrame({
        'date': dates,
        'sales': np.random.normal(1000, 200, len(dates)).cumsum(),
        'customers': np.random.poisson(50, len(dates)),
        'region': np.random.choice(['North', 'South', 'East', 'West'], len(dates)),
        'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], len(dates))
    })
    
    # Employee data
    employee_data = pd.DataFrame({
        'employee_id': range(1, 101),
        'name': [f'Employee {i}' for i in range(1, 101)],
        'department': np.random.choice(['Sales', 'Marketing', 'Engineering', 'HR', 'Finance'], 100),
        'salary': np.random.normal(75000, 15000, 100),
        'performance_score': np.random.uniform(1, 10, 100),
        'years_experience': np.random.uniform(0, 20, 100)
    })
    
    # Stock prices simulation
    stock_prices = []
    price = 100
    for i in range(252):  # Trading days in a year
        change = np.random.normal(0, 2)
        price += change
        stock_prices.append({
            'date': datetime(2024, 1, 1) + timedelta(days=i),
            'price': max(price, 10),  # Don't let price go below 10
            'volume': np.random.randint(1000, 10000)
        })
    
    stock_data = pd.DataFrame(stock_prices)
    
    return sales_data, employee_data, stock_data

def create_dashboard():
    """Main dashboard function"""
    
    # Title and description
    st.title("📊 Advanced Streamlit Dashboard")
    st.markdown("A comprehensive dashboard showcasing various Streamlit visualization capabilities")
    
    # Load sample data
    sales_data, employee_data, stock_data = create_sample_data()
    
    # Sidebar controls
    st.sidebar.title("🎛️ Dashboard Controls")
    
    # Date range selector
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(sales_data['date'].min().date(), sales_data['date'].max().date()),
        min_value=sales_data['date'].min().date(),
        max_value=sales_data['date'].max().date()
    )
    
    # Filter data based on date range
    filtered_sales = sales_data[
        (sales_data['date'].dt.date >= date_range[0]) & 
        (sales_data['date'].dt.date <= date_range[1])
    ]
    
    # Region filter
    selected_regions = st.sidebar.multiselect(
        "Select Regions",
        options=sales_data['region'].unique(),
        default=sales_data['region'].unique()
    )
    
    # Filter by regions
    filtered_sales = filtered_sales[filtered_sales['region'].isin(selected_regions)]
    
    # Department filter for employee data
    selected_departments = st.sidebar.multiselect(
        "Select Departments",
        options=employee_data['department'].unique(),
        default=employee_data['department'].unique()
    )
    
    filtered_employees = employee_data[employee_data['department'].isin(selected_departments)]
    
    # Main dashboard layout
    st.header("📈 Key Metrics")
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = filtered_sales['sales'].iloc[-1] if len(filtered_sales) > 0 else 0
        st.metric(
            "Total Sales",
            f"${total_sales:,.0f}",
            delta=f"{np.random.randint(-10, 20)}%"
        )
    
    with col2:
        avg_customers = filtered_sales['customers'].mean() if len(filtered_sales) > 0 else 0
        st.metric(
            "Avg Daily Customers",
            f"{avg_customers:.0f}",
            delta=f"{np.random.randint(-5, 15)}%"
        )
    
    with col3:
        total_employees = len(filtered_employees)
        st.metric(
            "Total Employees",
            f"{total_employees}",
            delta=f"{np.random.randint(-2, 5)}"
        )
    
    with col4:
        avg_salary = filtered_employees['salary'].mean() if len(filtered_employees) > 0 else 0
        st.metric(
            "Avg Salary",
            f"${avg_salary:,.0f}",
            delta=f"{np.random.randint(-3, 8)}%"
        )
    
    st.divider()
    
    # Charts section
    st.header("📊 Visualizations")
    
    # Create tabs for different chart types
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Sales Analytics", "👥 Employee Insights", "📊 Stock Analysis", "🎯 Interactive Charts"])
    
    with tab1:
        st.subheader("Sales Trends")
        
        # Line chart for sales over time
        fig_sales = px.line(
            filtered_sales, 
            x='date', 
            y='sales',
            title='Sales Over Time',
            color='region'
        )
        fig_sales.update_layout(height=400)
        st.plotly_chart(fig_sales, use_container_width=True)
        
        # Sales by region pie chart
        col1, col2 = st.columns(2)
        
        with col1:
            region_sales = filtered_sales.groupby('region')['sales'].sum()
            fig_pie = px.pie(
                values=region_sales.values,
                names=region_sales.index,
                title='Sales by Region'
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Sales by product category
            category_sales = filtered_sales.groupby('product_category')['sales'].sum()
            fig_bar = px.bar(
                x=category_sales.index,
                y=category_sales.values,
                title='Sales by Product Category'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    
    with tab2:
        st.subheader("Employee Analytics")
        
        # Salary distribution
        fig_hist = px.histogram(
            filtered_employees,
            x='salary',
            nbins=20,
            title='Salary Distribution',
            color='department'
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Performance vs Salary scatter plot
        col1, col2 = st.columns(2)
        
        with col1:
            fig_scatter = px.scatter(
                filtered_employees,
                x='years_experience',
                y='salary',
                color='department',
                size='performance_score',
                title='Experience vs Salary',
                hover_data=['name']
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Department performance
            dept_performance = filtered_employees.groupby('department')['performance_score'].mean()
            fig_dept = px.bar(
                x=dept_performance.index,
                y=dept_performance.values,
                title='Average Performance by Department'
            )
            st.plotly_chart(fig_dept, use_container_width=True)
    
    with tab3:
        st.subheader("Stock Price Analysis")
        
        # Stock price line chart
        fig_stock = px.line(
            stock_data,
            x='date',
            y='price',
            title='Stock Price Over Time'
        )
        fig_stock.update_layout(height=400)
        st.plotly_chart(fig_stock, use_container_width=True)
        
        # Volume and price correlation
        col1, col2 = st.columns(2)
        
        with col1:
            fig_volume = px.bar(
                stock_data.tail(30),  # Last 30 days
                x='date',
                y='volume',
                title='Trading Volume (Last 30 Days)'
            )
            st.plotly_chart(fig_volume, use_container_width=True)
        
        with col2:
            # Price distribution
            fig_dist = px.histogram(
                stock_data,
                x='price',
                nbins=20,
                title='Price Distribution'
            )
            st.plotly_chart(fig_dist, use_container_width=True)
    
    with tab4:
        st.subheader("Interactive Visualizations")
        
        # Interactive scatter plot with selection
        st.write("**Interactive Scatter Plot - Click and drag to zoom, double-click to reset**")
        
        fig_interactive = px.scatter(
            filtered_employees,
            x='salary',
            y='performance_score',
            color='department',
            size='years_experience',
            hover_data=['name'],
            title='Interactive Employee Analysis'
        )
        st.plotly_chart(fig_interactive, use_container_width=True)
        
        # 3D scatter plot
        st.write("**3D Visualization**")
        fig_3d = px.scatter_3d(
            filtered_employees,
            x='salary',
            y='performance_score',
            z='years_experience',
            color='department',
            title='3D Employee Analysis'
        )
        st.plotly_chart(fig_3d, use_container_width=True)
    
    st.divider()
    
    # Data tables section
    st.header("📋 Data Tables")
    
    # Tabs for different data views
    data_tab1, data_tab2, data_tab3 = st.tabs(["Sales Data", "Employee Data", "Stock Data"])
    
    with data_tab1:
        st.subheader("Sales Data")
        st.dataframe(
            filtered_sales.head(20),
            use_container_width=True,
            hide_index=True
        )
        
        # Download button for sales data
        csv_sales = filtered_sales.to_csv(index=False)
        st.download_button(
            label="Download Sales Data as CSV",
            data=csv_sales,
            file_name='sales_data.csv',
            mime='text/csv'
        )
    
    with data_tab2:
        st.subheader("Employee Data")
        st.dataframe(
            filtered_employees.head(20),
            use_container_width=True,
            hide_index=True
        )
        
        # Download button for employee data
        csv_employees = filtered_employees.to_csv(index=False)
        st.download_button(
            label="Download Employee Data as CSV",
            data=csv_employees,
            file_name='employee_data.csv',
            mime='text/csv'
        )
    
    with data_tab3:
        st.subheader("Stock Data")
        st.dataframe(
            stock_data.head(20),
            use_container_width=True,
            hide_index=True
        )
        
        # Download button for stock data
        csv_stock = stock_data.to_csv(index=False)
        st.download_button(
            label="Download Stock Data as CSV",
            data=csv_stock,
            file_name='stock_data.csv',
            mime='text/csv'
        )
    
    # Footer
    st.divider()
    st.markdown("---")
    st.markdown("**Dashboard created with Streamlit** | 📊 Advanced Visualizations | 🎯 Interactive Features")

# Run the dashboard
if __name__ == "__main__":
    create_dashboard()
