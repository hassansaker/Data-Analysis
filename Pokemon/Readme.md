# Pokémon Data Analysis

This repository contains a Python script for analyzing Pokémon data using the `Pokemon.csv` dataset. The script performs various data cleaning, filtering, and visualization tasks to derive insights from the Pokémon dataset.

## Files in This Repository

- **Pokemon.csv**: Contains detailed data on various Pokémon, including stats, types, and generations.
- **Pokemon.py**: A Python script that processes and analyzes the Pokémon dataset.

## Features and Analysis

The `Pokemon.py` script performs the following operations:

1. **Data Cleaning**:
   - Removes missing values in `Type 1` and `Type 2` columns.
   - Drops duplicate entries.

2. **Basic Statistics**:
   - Computes mean, min, and max values for `Attack` and `Speed`.

3. **Filtering Pokémon Data**:
   - Finds all Fire-type Pokémon with `Attack > 100`.
   - Identifies Legendary Pokémon with `Speed > 120`.

4. **Grouping and Aggregation**:
   - Calculates the average HP per Pokémon type.
   - Counts the number of Legendary Pokémon per generation.

5. **Sorting and Ranking**:
   - Ranks Pokémon by their total stats in descending order.
   - Finds Water-type Pokémon with `Sp. Atk > 80`, sorted by Defense.

6. **Visualizations**:
   - Bar chart of average `Attack` by Pokémon type.
   - Pie chart showing the distribution of Pokémon across generations.
   - Line chart showing the evolution of combat stats (Attack, Defense, Speed) by generation.

## Requirements

To run the script, ensure you have the following dependencies installed:
```bash
pip install pandas matplotlib
```

## Usage
Run the script using Python:
```bash
python Pokemon.py
```
---
Feel free to contribute by improving the analysis or adding new features!
