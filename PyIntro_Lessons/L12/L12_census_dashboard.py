"""
US Census Data Dashboard - Streamlit Application
===============================================

This Streamlit application analyzes and visualizes US Census data from 2010-2019.
It demonstrates various Streamlit features including:
- Data loading and caching
- Interactive widgets (selectbox, slider, checkbox)
- Multiple chart types (line, bar, scatter, map)
- Layout organization (columns, sidebar, tabs)
- Data filtering and aggregation

Author: Andreas Furth
Data Source: US Census Bureau (nst-est2019-alldata.csv)
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configure the page
st.set_page_config(
    page_title="US Census Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# We can add custom CSS to style the app
# WARNING: This is optional, and kinda wacky
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# The @-sign is a decorator
# It modifies the function that follows it
# There are many different kinds of decorators
@st.cache_data  # Cache the data loading for better performance
def load_census_data():
    """
    Load and preprocess the census data.
    
    Returns:
        pd.DataFrame: Processed census data
    """
    try:
        # Load the CSV file
        df = pd.read_csv('nst-est2019-alldata.csv')
        
        # NOTE: Here we're cleaning the data, this 
        # will be covered more in detail in later lessons

        # Clean the data
        # Remove rows where STATE is 0 (these are region summaries)
        df = df[df['STATE'] != 0]
        
        # Create a more readable state name column
        df['STATE_NAME'] = df['NAME']
        
        # Convert population columns to numeric, handling any non-numeric values
        pop_columns = [col for col in df.columns if 'POPESTIMATE' in col]
        for col in pop_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Calculate population change from 2010 to 2019
        df['POP_CHANGE_2010_2019'] = df['POPESTIMATE2019'] - df['POPESTIMATE2010']
        df['POP_CHANGE_PERCENT'] = (df['POP_CHANGE_2010_2019'] / df['POPESTIMATE2010']) * 100
        
        # Create year columns for easier plotting
        years = list(range(2010, 2020))
        pop_data = []
        for _, row in df.iterrows():
            for year in years:
                pop_data.append({
                    'STATE': row['STATE'],
                    'STATE_NAME': row['STATE_NAME'],
                    'REGION': row['REGION'],
                    'DIVISION': row['DIVISION'],
                    'YEAR': year,
                    'POPULATION': row[f'POPESTIMATE{year}']
                })
        
        df_long = pd.DataFrame(pop_data)
        
        return df, df_long
        
    except FileNotFoundError:
        st.error("❌ Census data file not found. Please ensure 'nst-est2019-alldata.csv' is in the same directory.")
        return None, None
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        return None, None

def create_population_map(df):
    """
    Create an interactive map showing population by state.
    
    Args:
        df (pd.DataFrame): Census data
        
    Returns:
        plotly.graph_objects.Figure: Map visualization
    """
    # Get the latest population data (2019)
    latest_data = df[df['YEAR'] == 2019].copy()
    
    # Create a mapping from census state names to standard state names
    state_mapping = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
        'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
        'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
        'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
        'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
        'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
        'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    
    # Add state codes to the data
    latest_data['STATE_CODE'] = latest_data['STATE_NAME'].map(state_mapping)
    
    # Remove any rows where we couldn't map the state name
    latest_data = latest_data.dropna(subset=['STATE_CODE'])
    
    # Create a choropleth map using plotly's built-in US states
    # This is very cool
    # You can explore this more, maybe try something for sweden/europe?
    fig = px.choropleth(
        latest_data,
        locations='STATE_CODE',
        locationmode='USA-states',
        color='POPULATION',
        scope='usa',
        title="US Population by State (2019)",
        color_continuous_scale='Blues',
        labels={'POPULATION': 'Population'},
        hover_name='STATE_NAME',
        hover_data={'STATE_CODE': False, 'POPULATION': ':,'}
    )
    
    fig.update_layout(
        height=600,
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'
        )
    )
    
    return fig

def create_population_bar_chart(df):
    """
    Create a bar chart showing top states by population.
    
    Args:
        df (pd.DataFrame): Census data
        
    Returns:
        plotly.graph_objects.Figure: Bar chart
    """
    # Get the latest population data (2019)
    latest_data = df[df['YEAR'] == 2019].copy()
    latest_data = latest_data.sort_values('POPULATION', ascending=False)
    
    fig = px.bar(
        latest_data.head(20),  # Show top 20 states
        x='POPULATION',
        y='STATE_NAME',
        orientation='h',
        title="Top 20 States by Population (2019)",
        labels={'POPULATION': 'Population', 'STATE_NAME': 'State'},
        color='POPULATION',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        height=600,
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False
    )
    
    return fig

def create_population_trends(df_long, selected_states):
    """
    Create a line chart showing population trends over time.
    
    Args:
        df_long (pd.DataFrame): Long format census data
        selected_states (list): List of selected states
        
    Returns:
        plotly.graph_objects.Figure: Line chart
    """
    # Filter data for selected states
    filtered_data = df_long[df_long['STATE_NAME'].isin(selected_states)]
    
    fig = px.line(
        filtered_data,
        x='YEAR',
        y='POPULATION',
        color='STATE_NAME',
        title="Population Trends Over Time",
        labels={'POPULATION': 'Population', 'YEAR': 'Year'}
    )
    
    fig.update_layout(
        height=500,
        xaxis_title="Year",
        yaxis_title="Population",
        hovermode='x unified'
    )
    
    return fig

def create_population_change_chart(df):
    """
    Create a chart showing population change from 2010 to 2019.
    
    Args:
        df (pd.DataFrame): Census data
        
    Returns:
        plotly.graph_objects.Figure: Bar chart
    """
    # Get states with the largest population changes
    change_data = df.nlargest(15, 'POP_CHANGE_2010_2019')
    
    fig = px.bar(
        change_data,
        x='POP_CHANGE_2010_2019',
        y='STATE_NAME',
        orientation='h',
        title="States with Largest Population Growth (2010-2019)",
        labels={'POP_CHANGE_2010_2019': 'Population Change', 'STATE_NAME': 'State'},
        color='POP_CHANGE_2010_2019',
        color_continuous_scale='RdYlGn'
    )
    
    fig.update_layout(
        height=500,
        yaxis={'categoryorder': 'total ascending'},
        showlegend=False
    )
    
    return fig

def create_regional_analysis(df_long):
    """
    Create regional analysis charts.
    
    Args:
        df_long (pd.DataFrame): Long format census data
        
    Returns:
        plotly.graph_objects.Figure: Regional analysis
    """
    # Aggregate by region and year
    regional_data = df_long.groupby(['REGION', 'YEAR'])['POPULATION'].sum().reset_index()
    
    # Map region numbers to names
    region_names = {1: 'Northeast', 2: 'Midwest', 3: 'South', 4: 'West'}
    regional_data['REGION_NAME'] = regional_data['REGION'].map(region_names)
    
    fig = px.line(
        regional_data,
        x='YEAR',
        y='POPULATION',
        color='REGION_NAME',
        title="Population by Region Over Time",
        labels={'POPULATION': 'Population', 'YEAR': 'Year'}
    )
    
    fig.update_layout(
        height=500,
        xaxis_title="Year",
        yaxis_title="Population"
    )
    
    return fig

def main():
    """
    Main function to run the Streamlit application.
    """
    # Title and description
    st.markdown('<h1 class="main-header">📊 US Census Data Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("""
    This dashboard analyzes US Census data from 2010-2019, showing population trends, 
    regional differences, and demographic changes across states and regions.
    """)
    
    # Load data
    df, df_long = load_census_data()
    
    if df is None:
        st.stop()
    
    # Sidebar for filters and controls
    st.sidebar.header("🔧 Dashboard Controls")
    
    # Year range selector
    st.sidebar.subheader("📅 Year Range")
    year_range = st.sidebar.slider(
        "Select year range:",
        min_value=2010,
        max_value=2019,
        value=(2010, 2019),
        step=1
    )
    
    # State selector
    st.sidebar.subheader("🗺️ State Selection")
    all_states = sorted(df['STATE_NAME'].unique())
    selected_states = st.sidebar.multiselect(
        "Choose states to analyze:",
        options=all_states,
        default=all_states  # Default to all states
    )
    
    # Region filter
    st.sidebar.subheader("🌎 Region Filter")
    region_names = {1: 'Northeast', 2: 'Midwest', 3: 'South', 4: 'West'}
    selected_regions = st.sidebar.multiselect(
        "Filter by region:",
        options=list(region_names.values()),
        default=list(region_names.values())
    )
    
    # Filter data based on selections
    if selected_states:
        df_filtered = df[df['STATE_NAME'].isin(selected_states)]
        df_long_filtered = df_long[df_long['STATE_NAME'].isin(selected_states)]
    else:
        # If no states selected, show all states (US total)
        df_filtered = df
        df_long_filtered = df_long
    
    # Filter by year range
    df_long_filtered = df_long_filtered[
        (df_long_filtered['YEAR'] >= year_range[0]) & 
        (df_long_filtered['YEAR'] <= year_range[1])
    ]
    
    # Main content area
    # Key metrics
    st.header("📈 Key Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_pop_2019 = df_filtered['POPESTIMATE2019'].sum()
        st.metric(
            label="Total Population (2019)",
            value=f"{total_pop_2019:,.0f}",
            delta=None
        )
    
    with col2:
        avg_growth = df_filtered['POP_CHANGE_PERCENT'].mean()
        st.metric(
            label="Average Growth Rate",
            value=f"{avg_growth:.1f}%",
            delta=None
        )
    
    with col3:
        fastest_growing = df_filtered.loc[df_filtered['POP_CHANGE_PERCENT'].idxmax(), 'STATE_NAME']
        fastest_rate = df_filtered['POP_CHANGE_PERCENT'].max()
        st.metric(
            label="Fastest Growing State",
            value=f"{fastest_growing}",
            delta=f"{fastest_rate:.1f}%"
        )
    
    with col4:
        total_change = df_filtered['POP_CHANGE_2010_2019'].sum()
        st.metric(
            label="Total Population Change",
            value=f"{total_change:,.0f}",
            delta=None
        )
    
    # Tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Population Trends", "🗺️ Geographic Analysis", "📈 Growth Analysis", "🌎 Regional Analysis"])
    
    with tab1:
        st.header("Population Trends Over Time")
        
        # Line chart for selected states
        if len(selected_states) <= 10:  # Show individual state lines if 10 or fewer states
            fig_trends = create_population_trends(df_long_filtered, selected_states)
            st.plotly_chart(fig_trends, width='stretch')
        else:
            # If many states selected, show aggregated view
            st.info("ℹ️ Showing aggregated view for many states. Select fewer states to see individual trends.")
            # Create aggregated data for all selected states
            aggregated_data = df_long_filtered.groupby('YEAR')['POPULATION'].sum().reset_index()
            aggregated_data['STATE_NAME'] = 'All Selected States'
            
            fig_trends = px.line(
                aggregated_data,
                x='YEAR',
                y='POPULATION',
                title="Total Population Trends Over Time",
                labels={'POPULATION': 'Total Population', 'YEAR': 'Year'}
            )
            st.plotly_chart(fig_trends, width='stretch')
        
        # Population change chart
        st.subheader("Population Change (2010-2019)")
        fig_change = create_population_change_chart(df_filtered)
        st.plotly_chart(fig_change, width='stretch')
    
    with tab2:
        st.header("Geographic Analysis")
        
        # Population map
        st.subheader("US Population Map (2019)")
        fig_map = create_population_map(df_long_filtered)
        st.plotly_chart(fig_map, width='stretch')
        
        # Debug information
        with st.expander("🔍 Map Data Debug Info"):
            st.write("**Data being used for the map:**")
            map_data = df_long_filtered[df_long_filtered['YEAR'] == 2019].copy()
            state_mapping = {
                'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
                'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
                'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
                'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
                'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
                'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
                'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
                'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
                'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
                'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
            }
            map_data['STATE_CODE'] = map_data['STATE_NAME'].map(state_mapping)
            st.write(f"Total states in data: {len(map_data)}")
            st.write(f"States with valid codes: {len(map_data.dropna(subset=['STATE_CODE']))}")
            st.dataframe(map_data[['STATE_NAME', 'STATE_CODE', 'POPULATION']].head(10))
        
        # Top states bar chart
        st.subheader("Top 20 States by Population")
        fig_bar = create_population_bar_chart(df_long_filtered)
        st.plotly_chart(fig_bar, width='stretch')
        
        # State comparison table
        st.subheader("State Comparison")
        comparison_data = df_filtered[['STATE_NAME', 'POPESTIMATE2010', 'POPESTIMATE2019', 'POP_CHANGE_2010_2019', 'POP_CHANGE_PERCENT']].copy()
        comparison_data.columns = ['State', 'Population 2010', 'Population 2019', 'Change (Number)', 'Change (%)']
        comparison_data = comparison_data.sort_values('Population 2019', ascending=False)
        
        st.dataframe(
            comparison_data,
            width='stretch',
            hide_index=True
        )
    
    with tab3:
        st.header("Growth Analysis")
        
        # Growth rate distribution
        st.subheader("Growth Rate Distribution")
        fig_hist = px.histogram(
            df_filtered,
            x='POP_CHANGE_PERCENT',
            nbins=20,
            title="Distribution of Population Growth Rates",
            labels={'POP_CHANGE_PERCENT': 'Growth Rate (%)', 'count': 'Number of States'}
        )
        st.plotly_chart(fig_hist, width='stretch')
        
        # Scatter plot: Population vs Growth Rate
        st.subheader("Population Size vs Growth Rate")
        # Create a copy of the data for the scatter plot
        scatter_data = df_filtered.copy()
        # Use absolute values for size to avoid negative values
        scatter_data['ABS_POP_CHANGE'] = abs(scatter_data['POP_CHANGE_2010_2019'])
        
        fig_scatter = px.scatter(
            scatter_data,
            x='POPESTIMATE2019',
            y='POP_CHANGE_PERCENT',
            size='ABS_POP_CHANGE',
            hover_name='STATE_NAME',
            title="Population Size vs Growth Rate (2010-2019)",
            labels={'POPESTIMATE2019': 'Population 2019', 'POP_CHANGE_PERCENT': 'Growth Rate (%)', 'ABS_POP_CHANGE': 'Absolute Population Change'}
        )
        st.plotly_chart(fig_scatter, width='stretch')
    
    with tab4:
        st.header("Regional Analysis")
        
        # Regional trends
        fig_regional = create_regional_analysis(df_long_filtered)
        st.plotly_chart(fig_regional, width='stretch')
        
        # Regional summary table
        st.subheader("Regional Summary")
        regional_summary = df_filtered.groupby('REGION').agg({
            'POPESTIMATE2019': 'sum',
            'POP_CHANGE_2010_2019': 'sum',
            'POP_CHANGE_PERCENT': 'mean'
        }).round(2)
        regional_summary.index = regional_summary.index.map(region_names)
        regional_summary.columns = ['Total Population 2019', 'Total Change', 'Avg Growth Rate (%)']
        regional_summary = regional_summary.sort_values('Total Population 2019', ascending=False)
        
        st.dataframe(regional_summary, width='stretch')
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>📊 US Census Data Dashboard | Built with Streamlit | Data Source: US Census Bureau</p>
        <p>This dashboard demonstrates various Streamlit features for data visualization and analysis.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
