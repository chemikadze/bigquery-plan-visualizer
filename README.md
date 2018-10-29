BigQuery plan visualizer
========================

Usage:
```
./bqplanviz.py examples/query.json
dot -O -Tpng examples/query.json.dot
open examples/query.json.dot.png
```

Requirements: GraphViz, Jinja2

Example output:

![alt text](https://github.com/chemikadze/bigquery-plan-visualizer/raw/master/examples/query.json.dot.png "Example plan picture")

