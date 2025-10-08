import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="🎲 Monte Carlo Simulation Dashboard",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)

def monte_carlo_simulation(initial_price, drift, volatility, time_horizon, num_simulations):
    """
    Run Monte Carlo simulation for stock price prediction
    """
    dt = 1/252  # Daily time step (252 trading days per year)
    
    # Initialize results array
    simulations = np.zeros((num_simulations, time_horizon + 1))
    simulations[:, 0] = initial_price
    
    # Generate random shocks
    random_shocks = np.random.normal(0, 1, (num_simulations, time_horizon))
    
    # Run simulations
    for t in range(1, time_horizon + 1):
        # Geometric Brownian Motion formula
        simulations[:, t] = simulations[:, t-1] * np.exp(
            (drift - 0.5 * volatility**2) * dt + 
            volatility * np.sqrt(dt) * random_shocks[:, t-1]
        )
    
    return simulations

def calculate_portfolio_value(initial_investment, simulations, time_horizon):
    """
    Calculate portfolio value over time for different scenarios
    """
    portfolio_values = np.zeros((simulations.shape[0], time_horizon + 1))
    
    for i in range(simulations.shape[0]):
        # Calculate number of shares that can be bought initially
        shares = initial_investment / simulations[i, 0]
        
        # Portfolio value over time
        portfolio_values[i, :] = shares * simulations[i, :]
    
    return portfolio_values

def calculate_var_cvar(returns, confidence_level=0.05):
    """
    Calculate Value at Risk (VaR) and Conditional Value at Risk (CVaR)
    """
    var = np.percentile(returns, confidence_level * 100)
    cvar = returns[returns <= var].mean()
    
    return var, cvar

def create_simulation_dashboard():
    """
    Main dashboard function for Monte Carlo simulation
    """
    
    st.title("🎲 Monte Carlo Simulation Dashboard")
    st.markdown("**Interactive Financial Risk Analysis with Real-time Updates**")
    
    # Sidebar controls
    st.sidebar.header("🎛️ Simulation Parameters")
    
    # Simulation parameters
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        initial_price = st.sidebar.slider(
            "Initial Stock Price ($)",
            min_value=10.0,
            max_value=500.0,
            value=100.0,
            step=5.0,
            help="Starting price of the stock"
        )
        
        drift = st.sidebar.slider(
            "Expected Annual Return (%)",
            min_value=-20.0,
            max_value=30.0,
            value=8.0,
            step=0.5,
            help="Expected annual return (drift)"
        ) / 100
        
        volatility = st.sidebar.slider(
            "Annual Volatility (%)",
            min_value=5.0,
            max_value=80.0,
            value=25.0,
            step=1.0,
            help="Annual volatility (risk measure)"
        ) / 100
    
    with col2:
        time_horizon = st.sidebar.slider(
            "Time Horizon (Days)",
            min_value=30,
            max_value=1000,
            value=252,
            step=30,
            help="Number of trading days to simulate"
        )
        
        num_simulations = st.sidebar.slider(
            "Number of Simulations",
            min_value=100,
            max_value=10000,
            value=1000,
            step=100,
            help="More simulations = more accurate results"
        )
        
        initial_investment = st.sidebar.number_input(
            "Initial Investment ($)",
            min_value=1000,
            max_value=1000000,
            value=10000,
            step=1000,
            help="Amount to invest initially"
        )
    
    # Advanced parameters
    st.sidebar.subheader("📊 Analysis Parameters")
    
    confidence_level = st.sidebar.selectbox(
        "Confidence Level for Risk Metrics",
        options=[0.01, 0.05, 0.10],
        index=1,
        format_func=lambda x: f"{x*100:.0f}%",
        help="Confidence level for VaR and CVaR calculations"
    )
    
    show_individual_paths = st.sidebar.checkbox(
        "Show Individual Simulation Paths",
        value=True,
        help="Display individual simulation trajectories"
    )
    
    # Run simulation
    if st.sidebar.button("🔄 Run New Simulation", type="primary"):
        st.rerun()
    
    # Generate time axis
    time_axis = np.arange(0, time_horizon + 1)
    
    # Run Monte Carlo simulation
    with st.spinner("Running Monte Carlo simulation..."):
        simulations = monte_carlo_simulation(
            initial_price, drift, volatility, time_horizon, num_simulations
        )
        
        # Calculate portfolio values
        portfolio_values = calculate_portfolio_value(
            initial_investment, simulations, time_horizon
        )
        
        # Calculate final returns
        final_returns = (simulations[:, -1] - initial_price) / initial_price
        portfolio_returns = (portfolio_values[:, -1] - initial_investment) / initial_investment
    
    # Main dashboard layout
    st.header("📈 Simulation Results")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_final_price = np.mean(simulations[:, -1])
        st.metric(
            "Mean Final Price",
            f"${mean_final_price:.2f}",
            delta=f"{((mean_final_price - initial_price) / initial_price * 100):.1f}%"
        )
    
    with col2:
        mean_portfolio_value = np.mean(portfolio_values[:, -1])
        st.metric(
            "Mean Portfolio Value",
            f"${mean_portfolio_value:,.0f}",
            delta=f"{((mean_portfolio_value - initial_investment) / initial_investment * 100):.1f}%"
        )
    
    with col3:
        var, cvar = calculate_var_cvar(portfolio_returns, confidence_level)
        st.metric(
            f"VaR ({confidence_level*100:.0f}%)",
            f"{var*100:.1f}%",
            help="Value at Risk - worst case scenario"
        )
    
    with col4:
        st.metric(
            f"CVaR ({confidence_level*100:.0f}%)",
            f"{cvar*100:.1f}%",
            help="Conditional Value at Risk - expected loss in worst case"
        )
    
    st.divider()
    
    # Charts section
    st.header("📊 Interactive Visualizations")
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Price Paths", 
        "💰 Portfolio Analysis", 
        "📊 Risk Metrics", 
        "🎯 Distribution Analysis"
    ])
    
    with tab1:
        st.subheader("Stock Price Simulation Paths")
        
        # Create price paths chart
        fig_paths = go.Figure()
        
        # Add individual paths if requested
        if show_individual_paths:
            for i in range(min(50, num_simulations)):  # Show max 50 paths for performance
                fig_paths.add_trace(go.Scatter(
                    x=time_axis,
                    y=simulations[i, :],
                    mode='lines',
                    line=dict(width=0.5, color='rgba(0,100,80,0.1)'),
                    showlegend=False,
                    hoverinfo='skip'
                ))
        
        # Add mean path
        mean_path = np.mean(simulations, axis=0)
        fig_paths.add_trace(go.Scatter(
            x=time_axis,
            y=mean_path,
            mode='lines',
            line=dict(width=3, color='red'),
            name='Mean Path',
            hovertemplate='Day: %{x}<br>Price: $%{y:.2f}<extra></extra>'
        ))
        
        # Add confidence intervals
        percentile_5 = np.percentile(simulations, 5, axis=0)
        percentile_95 = np.percentile(simulations, 95, axis=0)
        
        fig_paths.add_trace(go.Scatter(
            x=time_axis,
            y=percentile_95,
            mode='lines',
            line=dict(width=0),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        fig_paths.add_trace(go.Scatter(
            x=time_axis,
            y=percentile_5,
            mode='lines',
            line=dict(width=0),
            fill='tonexty',
            fillcolor='rgba(0,100,80,0.2)',
            name='90% Confidence Interval',
            hoverinfo='skip'
        ))
        
        fig_paths.update_layout(
            title="Monte Carlo Stock Price Simulation",
            xaxis_title="Trading Days",
            yaxis_title="Stock Price ($)",
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig_paths, width='stretch')
        
        # Statistics table
        st.subheader("📊 Price Statistics")
        
        stats_data = {
            'Metric': [
                'Mean Final Price',
                'Median Final Price',
                'Min Final Price',
                'Max Final Price',
                'Standard Deviation',
                '5th Percentile',
                '95th Percentile'
            ],
            'Value': [
                f"${np.mean(simulations[:, -1]):.2f}",
                f"${np.median(simulations[:, -1]):.2f}",
                f"${np.min(simulations[:, -1]):.2f}",
                f"${np.max(simulations[:, -1]):.2f}",
                f"${np.std(simulations[:, -1]):.2f}",
                f"${np.percentile(simulations[:, -1], 5):.2f}",
                f"${np.percentile(simulations[:, -1], 95):.2f}"
            ]
        }
        
        st.dataframe(pd.DataFrame(stats_data), width='stretch', hide_index=True)
    
    with tab2:
        st.subheader("Portfolio Value Analysis")
        
        # Portfolio value paths
        fig_portfolio = go.Figure()
        
        # Add individual portfolio paths
        if show_individual_paths:
            for i in range(min(50, num_simulations)):
                fig_portfolio.add_trace(go.Scatter(
                    x=time_axis,
                    y=portfolio_values[i, :],
                    mode='lines',
                    line=dict(width=0.5, color='rgba(255,0,0,0.1)'),
                    showlegend=False,
                    hoverinfo='skip'
                ))
        
        # Add mean portfolio path
        mean_portfolio = np.mean(portfolio_values, axis=0)
        fig_portfolio.add_trace(go.Scatter(
            x=time_axis,
            y=mean_portfolio,
            mode='lines',
            line=dict(width=3, color='blue'),
            name='Mean Portfolio Value',
            hovertemplate='Day: %{x}<br>Value: $%{y:,.0f}<extra></extra>'
        ))
        
        # Add initial investment line
        fig_portfolio.add_hline(
            y=initial_investment,
            line_dash="dash",
            line_color="green",
            annotation_text="Initial Investment",
            annotation_position="top right"
        )
        
        fig_portfolio.update_layout(
            title="Portfolio Value Over Time",
            xaxis_title="Trading Days",
            yaxis_title="Portfolio Value ($)",
            height=500
        )
        
        st.plotly_chart(fig_portfolio, width='stretch')
        
        # Portfolio statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Portfolio Returns")
            
            returns_data = {
                'Metric': [
                    'Mean Return',
                    'Median Return',
                    'Best Case Return',
                    'Worst Case Return',
                    'Standard Deviation',
                    'Sharpe Ratio (approx)'
                ],
                'Value': [
                    f"{np.mean(portfolio_returns)*100:.2f}%",
                    f"{np.median(portfolio_returns)*100:.2f}%",
                    f"{np.max(portfolio_returns)*100:.2f}%",
                    f"{np.min(portfolio_returns)*100:.2f}%",
                    f"{np.std(portfolio_returns)*100:.2f}%",
                    f"{np.mean(portfolio_returns)/np.std(portfolio_returns):.2f}"
                ]
            }
            
            st.dataframe(pd.DataFrame(returns_data), width='stretch', hide_index=True)
        
        with col2:
            st.subheader("💰 Final Portfolio Values")
            
            # Histogram of final portfolio values
            fig_hist = px.histogram(
                x=portfolio_values[:, -1],
                nbins=50,
                title="Distribution of Final Portfolio Values",
                labels={'x': 'Final Portfolio Value ($)', 'y': 'Frequency'}
            )
            fig_hist.add_vline(
                x=initial_investment,
                line_dash="dash",
                line_color="green",
                annotation_text="Initial Investment"
            )
            st.plotly_chart(fig_hist, width='stretch')
    
    with tab3:
        st.subheader("Risk Analysis")
        
        # VaR and CVaR analysis
        col1, col2 = st.columns(2)
        
        with col1:
            # VaR over time
            var_over_time = []
            cvar_over_time = []
            time_points = list(range(0, time_horizon + 1, 30))  # Every 30 days
            
            for t in time_points:
                if t == 0:
                    var_over_time.append(0)
                    cvar_over_time.append(0)
                else:
                    returns_at_t = (portfolio_values[:, t] - initial_investment) / initial_investment
                    var, cvar = calculate_var_cvar(returns_at_t, confidence_level)
                    var_over_time.append(var)
                    cvar_over_time.append(cvar)
            
            fig_risk = go.Figure()
            fig_risk.add_trace(go.Scatter(
                x=time_points,
                y=[v*100 for v in var_over_time],
                mode='lines+markers',
                name=f'VaR ({confidence_level*100:.0f}%)',
                line=dict(color='red', width=2)
            ))
            fig_risk.add_trace(go.Scatter(
                x=time_points,
                y=[v*100 for v in cvar_over_time],
                mode='lines+markers',
                name=f'CVaR ({confidence_level*100:.0f}%)',
                line=dict(color='darkred', width=2)
            ))
            
            fig_risk.update_layout(
                title="Risk Metrics Over Time",
                xaxis_title="Trading Days",
                yaxis_title="Risk (%)",
                height=400
            )
            
            st.plotly_chart(fig_risk, width='stretch')
        
        with col2:
            # Risk metrics table
            st.subheader("📊 Risk Metrics")
            
            # Calculate various risk metrics
            max_drawdown = np.min((portfolio_values - initial_investment) / initial_investment)
            volatility_annual = np.std(portfolio_returns) * np.sqrt(252)
            sharpe_ratio = np.mean(portfolio_returns) / np.std(portfolio_returns) * np.sqrt(252)
            
            risk_data = {
                'Risk Metric': [
                    f'VaR ({confidence_level*100:.0f}%)',
                    f'CVaR ({confidence_level*100:.0f}%)',
                    'Maximum Drawdown',
                    'Annual Volatility',
                    'Sharpe Ratio',
                    'Probability of Loss'
                ],
                'Value': [
                    f"{var*100:.2f}%",
                    f"{cvar*100:.2f}%",
                    f"{max_drawdown*100:.2f}%",
                    f"{volatility_annual*100:.2f}%",
                    f"{sharpe_ratio:.2f}",
                    f"{np.mean(portfolio_returns < 0)*100:.2f}%"
                ]
            }
            
            st.dataframe(pd.DataFrame(risk_data), width='stretch', hide_index=True)
    
    with tab4:
        st.subheader("Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Returns distribution
            fig_returns = px.histogram(
                x=portfolio_returns*100,
                nbins=50,
                title="Portfolio Returns Distribution",
                labels={'x': 'Portfolio Return (%)', 'y': 'Frequency'}
            )
            fig_returns.add_vline(
                x=0,
                line_dash="dash",
                line_color="red",
                annotation_text="Break-even"
            )
            st.plotly_chart(fig_returns, width='stretch')
        
        with col2:
            # Q-Q plot for normality
            from scipy import stats
            
            # Generate theoretical quantiles
            theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(portfolio_returns)))
            sample_quantiles = np.sort(portfolio_returns)
            
            fig_qq = go.Figure()
            fig_qq.add_trace(go.Scatter(
                x=theoretical_quantiles,
                y=sample_quantiles,
                mode='markers',
                name='Sample vs Theoretical',
                marker=dict(size=4)
            ))
            
            # Add diagonal line
            min_val = min(theoretical_quantiles.min(), sample_quantiles.min())
            max_val = max(theoretical_quantiles.max(), sample_quantiles.max())
            fig_qq.add_trace(go.Scatter(
                x=[min_val, max_val],
                y=[min_val, max_val],
                mode='lines',
                name='Perfect Normal',
                line=dict(dash='dash', color='red')
            ))
            
            fig_qq.update_layout(
                title="Q-Q Plot: Portfolio Returns vs Normal Distribution",
                xaxis_title="Theoretical Quantiles",
                yaxis_title="Sample Quantiles",
                height=400
            )
            
            st.plotly_chart(fig_qq, width='stretch')
        
        # Statistical tests
        st.subheader("📊 Statistical Analysis")
        
        # Jarque-Bera test for normality
        from scipy.stats import jarque_bera
        
        jb_stat, jb_pvalue = jarque_bera(portfolio_returns)
        
        stats_analysis = {
            'Test': [
                'Jarque-Bera Test (Normality)',
                'Skewness',
                'Kurtosis',
                'Mean',
                'Standard Deviation'
            ],
            'Statistic': [
                f"{jb_stat:.4f}",
                f"{stats.skew(portfolio_returns):.4f}",
                f"{stats.kurtosis(portfolio_returns):.4f}",
                f"{np.mean(portfolio_returns):.4f}",
                f"{np.std(portfolio_returns):.4f}"
            ],
            'P-value': [
                f"{jb_pvalue:.4f}",
                "-",
                "-",
                "-",
                "-"
            ]
        }
        
        st.dataframe(pd.DataFrame(stats_analysis), width='stretch', hide_index=True)
    
    # Footer
    st.divider()
    st.markdown("---")
    st.markdown("**Monte Carlo Simulation Dashboard** | 🎲 Real-time Risk Analysis | 📊 Interactive Financial Modeling")

# Run the dashboard
if __name__ == "__main__":
    create_simulation_dashboard()
