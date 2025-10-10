#!/usr/bin/env python3
"""
Matplotlib Examples - Python Script Version

This script demonstrates how matplotlib displays figures when running from a .py file.
It covers basic plotting concepts and includes Titanic dataset visualizations.

Key differences when running matplotlib from .py files:
1. Need to use plt.show() to display figures
2. Figures may open in separate windows
3. Script execution pauses until figures are closed (unless using non-blocking mode)
4. Can save figures to files using plt.savefig()

Author: Python Tutorial
Date: 2024
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def setup_matplotlib():
    """Configure matplotlib for script execution"""
    # Set the backend (optional, matplotlib will choose automatically)
    # plt.switch_backend('TkAgg')  # For GUI display
    # plt.switch_backend('Agg')    # For saving to files only
    
    # Set figure size and style
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12
    
    print("Matplotlib configured for script execution")
    print(f"Current backend: {plt.get_backend()}")

def basic_line_plot():
    """Demonstrate basic line plotting"""
    print("\n=== Basic Line Plot ===")
    
    # Create sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=2, color='blue')
    plt.title('Basic Sine Wave - Python Script')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    # Show the plot (this will open a window)
    plt.show()
    print("Figure displayed. Close the window to continue...")

def multiple_plots():
    """Demonstrate multiple plots in one figure"""
    print("\n=== Multiple Plots ===")
    
    # Create data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Sine wave
    axes[0, 0].plot(x, y1, 'b-', linewidth=2)
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True)
    
    # Plot 2: Cosine wave
    axes[0, 1].plot(x, y2, 'r-', linewidth=2)
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True)
    
    # Plot 3: Combined
    axes[1, 0].plot(x, y1, 'b-', label='sin(x)', linewidth=2)
    axes[1, 0].plot(x, y2, 'r-', label='cos(x)', linewidth=2)
    axes[1, 0].set_title('Both Functions')
    axes[1, 0].legend()
    axes[1, 0].grid(True)
    
    # Plot 4: Product
    axes[1, 1].plot(x, y3, 'g-', linewidth=2)
    axes[1, 1].set_title('sin(x) * cos(x)')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.show()
    print("Multiple plots displayed. Close the window to continue...")

def scatter_plot_example():
    """Demonstrate scatter plotting"""
    print("\n=== Scatter Plot ===")
    
    # Generate random data
    np.random.seed(42)
    n = 100
    x = np.random.randn(n)
    y = 2 * x + np.random.randn(n) * 0.5
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.6, color='blue', s=50)
    plt.title('Scatter Plot Example')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    plt.show()
    print("Scatter plot displayed. Close the window to continue...")

def bar_chart_example():
    """Demonstrate bar chart"""
    print("\n=== Bar Chart ===")
    
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(categories, values, color=colors)
    plt.title('Bar Chart Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}', ha='center', va='bottom')
    
    plt.show()
    print("Bar chart displayed. Close the window to continue...")

def histogram_example():
    """Demonstrate histogram"""
    print("\n=== Histogram ===")
    
    # Generate sample data
    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)
    
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Histogram Example - Normal Distribution')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    plt.show()
    print("Histogram displayed. Close the window to continue...")

def titanic_analysis():
    """Analyze Titanic dataset"""
    print("\n=== Titanic Dataset Analysis ===")
    
    # Check if titanic.csv exists
    if not os.path.exists('titanic.csv'):
        print("Error: titanic.csv not found in current directory")
        print("Please make sure the file is in the same directory as this script")
        return
    
    # Load the dataset
    try:
        df = pd.read_csv('titanic.csv')
        print(f"Dataset loaded successfully. Shape: {df.shape}")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return
    
    # 1. Survival rate by gender
    print("\nCreating survival rate by gender plot...")
    survival_by_gender = df.groupby('Sex')['Survived'].agg(['count', 'sum'])
    survival_by_gender['survival_rate'] = survival_by_gender['sum'] / survival_by_gender['count']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(survival_by_gender.index, survival_by_gender['survival_rate'], 
                   color=['lightblue', 'pink'])
    plt.title('Titanic: Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Survival Rate')
    plt.ylim(0, 1)
    
    # Add percentage labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                 f'{height:.1%}', ha='center', va='bottom')
    
    plt.show()
    print("Gender survival plot displayed. Close the window to continue...")
    
    # 2. Age distribution
    print("\nCreating age distribution plot...")
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'].dropna(), bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Titanic: Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()
    print("Age distribution plot displayed. Close the window to continue...")
    
    # 3. Survival rate by passenger class
    print("\nCreating survival rate by class plot...")
    survival_by_class = df.groupby('Pclass')['Survived'].agg(['count', 'sum'])
    survival_by_class['survival_rate'] = survival_by_class['sum'] / survival_by_class['count']
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(survival_by_class.index, survival_by_class['survival_rate'], 
                   color=['gold', 'silver', 'brown'])
    plt.title('Titanic: Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Survival Rate')
    plt.ylim(0, 1)
    
    # Add percentage labels
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                 f'{height:.1%}', ha='center', va='bottom')
    
    plt.show()
    print("Class survival plot displayed. Close the window to continue...")

def save_figures_example():
    """Demonstrate saving figures to files"""
    print("\n=== Saving Figures to Files ===")
    
    # Create a sample plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=2, color='blue')
    plt.title('Figure Saved to File')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    
    # Save the figure
    filename = 'saved_plot.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Figure saved as: {filename}")
    
    # Also save as PDF
    pdf_filename = 'saved_plot.pdf'
    plt.savefig(pdf_filename, bbox_inches='tight')
    print(f"Figure also saved as: {pdf_filename}")
    
    plt.show()
    print("Figure displayed and saved. Close the window to continue...")

def non_blocking_example():
    """Demonstrate non-blocking plot display"""
    print("\n=== Non-blocking Plot Display ===")
    
    # Create multiple plots without blocking
    for i in range(3):
        x = np.linspace(0, 10, 100)
        y = np.sin(x + i)
        
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, linewidth=2)
        plt.title(f'Non-blocking Plot {i+1}')
        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.grid(True, alpha=0.3)
        
        # Use non-blocking show
        plt.show(block=False)
        print(f"Plot {i+1} displayed (non-blocking)")
    
    print("All plots displayed. They will remain open until manually closed.")
    input("Press Enter to continue...")

def main():
    """Main function to run all examples"""
    print("=" * 60)
    print("MATPLOTLIB EXAMPLES - PYTHON SCRIPT VERSION")
    print("=" * 60)
    print("\nThis script demonstrates matplotlib functionality when running from .py files.")
    print("Each plot will open in a separate window.")
    print("Close each window to proceed to the next example.")
    print("\nKey differences from Jupyter notebooks:")
    print("- Use plt.show() to display figures")
    print("- Figures open in separate windows")
    print("- Script pauses until figures are closed")
    print("- Can save figures to files")
    
    # Setup matplotlib
    setup_matplotlib()
    
    # Run examples
    try:
        basic_line_plot()
        multiple_plots()
        scatter_plot_example()
        bar_chart_example()
        histogram_example()
        titanic_analysis()
        save_figures_example()
        
        # Ask user if they want to see non-blocking example
        response = input("\nWould you like to see the non-blocking example? (y/n): ")
        if response.lower() == 'y':
            non_blocking_example()
        
        print("\n" + "=" * 60)
        print("ALL EXAMPLES COMPLETED!")
        print("=" * 60)
        print("\nSummary of what we covered:")
        print("1. Basic line plots")
        print("2. Multiple plots in one figure")
        print("3. Scatter plots")
        print("4. Bar charts")
        print("5. Histograms")
        print("6. Titanic dataset analysis")
        print("7. Saving figures to files")
        print("8. Non-blocking plot display")
        
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")
        print("Please check your matplotlib installation and dependencies.")

if __name__ == "__main__":
    main()
