# Seaborn Statistical Visualization

<!--
Author: Molla Samser
Website: https://rskworld.in/
Email: help@rskworld.in
Phone: +91 93305 39277
Address: Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India, 713147
-->

## Project Overview

This project demonstrates **Seaborn**, a statistical visualization library built on Matplotlib. It covers distribution plots, correlation heatmaps, categorical plots, regression plots, and advanced statistical visualizations. Perfect for exploratory data analysis and statistical insights.

## Features

- ✅ Statistical distribution plots
- ✅ Correlation matrices and heatmaps
- ✅ Categorical and relational plots
- ✅ Regression visualization
- ✅ Advanced statistical charts
- ✅ Q-Q plots and ECDF (Empirical Cumulative Distribution Function)
- ✅ Statistical tests and annotations (t-tests, ANOVA)
- ✅ Multiple styling options and themes
- ✅ Matrix plots and multi-variable visualizations
- ✅ Statistical summary tables and visualizations

## Technologies Used

- Python
- Seaborn
- Matplotlib
- Pandas
- NumPy
- Jupyter Notebook

## Installation

1. Clone or download this repository
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Project Structure

```
seaborn-statistical/
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_distribution_plots.ipynb
│   ├── 02_correlation_heatmaps.ipynb
│   ├── 03_categorical_plots.ipynb
│   ├── 04_regression_plots.ipynb
│   ├── 05_advanced_visualizations.ipynb
│   └── complete_guide.ipynb
├── data/
│   └── sample_data.csv
└── images/
    └── (generated visualization outputs)
```

## Usage

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open any notebook from the `notebooks/` directory
3. Run cells sequentially to see visualizations
4. For a complete guide, open `notebooks/complete_guide.ipynb`

## Notebooks Description

- **01_distribution_plots.ipynb**: Histograms, KDE plots, rug plots, and distribution comparisons
- **02_correlation_heatmaps.ipynb**: Correlation matrices, heatmaps, and cluster maps
- **03_categorical_plots.ipynb**: Bar plots, count plots, box plots, violin plots, and swarm plots
- **04_regression_plots.ipynb**: Linear regression, polynomial regression, and residual plots
- **05_advanced_visualizations.ipynb**: Pair plots, joint plots, and faceted grids
- **06_advanced_statistical_analysis.ipynb**: Q-Q plots, ECDF, statistical tests, and annotations
- **07_styling_and_themes.ipynb**: Different styles, color palettes, contexts, and custom styling
- **08_matrix_plots.ipynb**: Matrix plots and multi-variable visualizations
- **complete_guide.ipynb**: Comprehensive guide covering all visualization types

## Examples

### Distribution Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(data=df, x='value', kde=True)
plt.show()
```

### Correlation Heatmap
```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

## Contact

**Author:** Molla Samser  
**Website:** [https://rskworld.in/](https://rskworld.in/)  
**Email:** help@rskworld.in  
**Phone:** +91 93305 39277  
**Address:** Nutanhat, Mongolkote, Purba Burdwan, West Bengal, India, 713147

## License

This project is for educational purposes.

---

*Created by Molla Samser - [RSK World](https://rskworld.in/)*

