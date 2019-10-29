# [Earthquakes](https://likarajo.github.io/earthquakes/)
Fetch data from USGS and plot areas across the world that had a 4.5+ earthquake in the last 24 hours.

<div align="center">
  <img src="output_usgs_4.5quakes.png" width=700 />
</div>

## Data Source
[United State Geological Survey](https://earthquake.usgs.gov/)'s earthquake data.

## Process
* The size of the points corresponds to the power in Richter scale of the earthquake.

## Dependencies
```shell script
pip3 install datetime
pip3 install pandas
conda install matplotlib
conda install basemap
```

## Steps
* Run the python app
```shell script
python earthquake.py
```
