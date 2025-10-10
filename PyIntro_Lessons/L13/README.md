# Matplotlib Tutorial - L13

This directory contains comprehensive matplotlib tutorials with both Jupyter notebook and Python script examples.

## Files

### 1. `matplotlib_tutorial.ipynb`
A comprehensive Jupyter notebook that covers:
- Basic matplotlib concepts
- Line plots, scatter plots, bar charts, histograms
- Subplots and multiple plots
- Titanic dataset analysis
- Styling and customization

**How to use:**
```bash
jupyter notebook matplotlib_tutorial.ipynb
```

### 2. `matplotlib_examples.py`
A Python script that demonstrates:
- How matplotlib displays figures when running from .py files
- Key differences between notebook and script execution
- Figure saving capabilities
- Non-blocking plot display
- Titanic dataset visualizations

**How to use:**
```bash
python matplotlib_examples.py
```

### 3. `titanic.csv`
The Titanic dataset used for real-world visualization examples.

## Key Differences: Notebook vs Script

### Jupyter Notebook (`matplotlib_tutorial.ipynb`)
- Uses `%matplotlib inline` for inline display
- Plots appear directly in the notebook cells
- Interactive and exploratory
- Great for data analysis and learning

### Python Script (`matplotlib_examples.py`)
- Uses `plt.show()` to display figures
- Figures open in separate windows
- Script pauses until figures are closed
- Can save figures to files
- Better for production and automation

## Requirements

Make sure you have the following packages installed:

```bash
pip install matplotlib numpy pandas jupyter
```

## Usage Examples

### Running the Notebook
```bash
cd L13
jupyter notebook matplotlib_tutorial.ipynb
```

### Running the Script
```bash
cd L13
python matplotlib_examples.py
```

## Learning Objectives

After completing this tutorial, you will understand:

1. **Basic matplotlib concepts** - figures, axes, and plot types
2. **Different plot types** - when and how to use each
3. **Data visualization best practices** - making clear, informative plots
4. **Real-world analysis** - using matplotlib with actual datasets
5. **Script vs notebook differences** - when to use each approach

## Tips for Success

1. **Start with the notebook** - it's more interactive and easier to learn
2. **Experiment with the code** - modify parameters and see what happens
3. **Try the script version** - understand how matplotlib works in production
4. **Practice with your own data** - apply what you learn to real projects

## Troubleshooting

### Common Issues

1. **Figures not displaying in script**: Make sure you're using `plt.show()`
2. **Import errors**: Install required packages with `pip install`
3. **Backend issues**: Try different matplotlib backends if needed
4. **File not found**: Ensure `titanic.csv` is in the same directory

### Getting Help

- Check matplotlib documentation: https://matplotlib.org/
- Use `plt.help()` for function documentation
- Search for specific plot types in matplotlib gallery

Happy plotting! 📊
