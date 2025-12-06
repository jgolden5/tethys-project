# Tethys Application Project
## Based on [Map Layout Tutorial](https://docs.tethysplatform.org/en/latest/tutorials/map_layout.html)

## Steps to Recreate:
1. Download and install the miniconda (a lightweight version of the conda package and virtual environment manager, alternative to pip)
  `brew install miniconda` (replace brew with a package manager of your choice)
2. Follow virtual environment setup instructions [here](https://docs.tethysplatform.org/en/latest/supplementary/virtual_environment.html) (make sure to activate tethys environment with `conda activate tethys`)
3. Clone the project
  `git clone https://github.com/jgolden5/tethys-project`
4. Start the tethys app
  `tethys manage start`
5. Go to `localhost:8080/`, and log in with username `admin` and password `pass`
6. Click on the app icon with waves (This is the map_layout_tutorial app)
7. The map will now show an area of north Alabama, with data for nexus and catchments.
8. Toggle Nexus and Catchments to view their data, and click plot to view streamflow data over time period
9. You can zoom in and out of different aspects of the map
10. As a side note, there is also a traffic layer which, though I didn't identify exactly how to implement the data integration logic as of right now, has a reprojected geojson file tailored to CRS84 in config (config/traffic_4326.geojson) and a csv output file (outputs/traffic.csv), downloaded from an official government

### View detailed steps of my development of this project [here](https://github.com/jgolden5/tethys-project/blob/main/steps_taken.md)
