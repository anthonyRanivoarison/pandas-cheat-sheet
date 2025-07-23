# Matplotlib Overview

**Matplotlib** is the most popular python library for data visualization.
It allows us making awesome graph with just a few code lines.

### Installation

- Installation with pip:

```bash
pip install matplotlib
```

- Checking version:

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

### Getting started

```jupyterpython
import matplotlib.pyplot as plt  # Import module

# Data examples to view
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)  # display graph
plt.title("Mon premier graphique")  # Graph's title
plt.xlabel("X")  # Label on x axis
plt.ylabel("Y")  # Label on y axis
plt.show()  # Showing the graph
```

### Most Common Graph Types

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
z = [7, 8, 5, 6, 9, 6, 8, 7]

plt.plot(x, y)  # Line plot
plt.bar(x, y)  # Bar plot
plt.scatter(x, y)  # Nuage de points
plt.hist(z, bins=5)  # Histogram plot
```

### Personalize your graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.figure(figsize=(7, 7))  # Precise width and height in a tuple
plt.plot(x, y, color="red", linestyle="---") # custom color and linestyle (only on line plot)
```

### Resources

- It's just an overview of matplotlib's power. If you want more, I invite you to see official doc. After that, you can optimize your graph with Seaborn (for later) 

- Official documentation: `https://matplotlib.org/stable/contents.html`