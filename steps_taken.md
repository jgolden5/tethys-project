# Steps Taken
### Step-by-step guide for how I implemented my Tethys app project

---

# Table of Contents:
* A) Tutorial Project (Points I-IV)
* B) My adaptation with traffic data (V-X)

---

# A) [Tutorial](https://docs.tethysplatform.org/en/latest/tutorials/map_layout.html) Project

## I. Create and Activate Tethys Environment
1. Installed miniconda with brew:  
   `brew install miniconda`
2. Created new venv:  
   `conda create -n tethys`
3. Source entire path for activate (must be overwritten?):  
   `source /usr/local/Caskroom/miniconda/base/bin/activate`
4. Initialized conda with bash:  
   `conda init bash`
5. Activated tethys venv:  
   `conda activate tethys`

---

## II. Data Prep
1. Download sample NextGen data.  
   - This time, put `map_layout_tutorial` inside `workspaces/`, `app_workspace` inside `map_layout_tutorial/`, and contents of `sample_nextgen_data.zip` inside `app_workspace/`.  
   - Unzipped as:  
     `unzip sample_nextgen_data.zip -d sample_nextgen_data`  
   - Note to future Jonathan: **`workspaces/map_layout_tutorial/app_workspace` does NOT work. What DOES work is `map_layout_tutorial/workspaces/app_workspace` — swap the order.**
2. Explore the data again; try to understand the nexus file and differences from catchments.
3. Reproject spatial data.  
   This involves:  
   - Copy/pasting `reproject_environment.yml` and `reproject.py`  
   - Creating another conda env based on the yml  
   - Entering that env  
   - Running `reproject.py` on nexus and catchments GeoJSON files

---

## III. Add Spatial Data to Map Layout
1. Override `compose_layers` function of `MapLayout` in:  
   `~/tethys/tethysdev/tethysapp-map_layout_tutorial/tethysapp/workspaces/map_layout_tutorial/controllers.py`
2. Adjust map default zoom and extent.  
   Useful tip for understanding `default_map_extent`: in Chrome debugger console:  
   `ol.proj.transformExtent(TETHYS_MAP_VIEW.getMap().getView().calculateExtent(TETHYS_MAP_VIEW.getMap().getSize()), 'EPSG:3857', 'EPSG:4326')`
3. Fix 404 at `http://localhost:8000/apps/map-layout-tutorial/`.  
   Issue was wrong workspace directory structure — swapping directories fixed it. Nexus data appeared.
4. Replace `controllers.py` with additional code from **"3. Adjust the layer styles"** section.
5. Change outer nexus colors from red → green, and catchment outline from blue → yellow.

---

## IV. Configure Map Layout Data Plotting
1. Configure NextGen plotting by replacing `controllers.py` with new code:  
   - Add import (`pandas`)  
   - Add constant (`app_workspace`)  
   - Set two properties true in `MapLayoutTutorialMap` (`show_properties_popup`, `plot_slide_sheet`)  
   - Add `get_plot_for_layer_feature`
2. For deeper explanation, see:  
   https://docs.tethysplatform.org/en/latest/tutorials/map_layout/configure_data_plotting.html

---

# B) My adaptation with traffic data

## V. (AZ Branch) Set Up Scaffolding and Basic Map
Ref: https://docs.tethysplatform.org/en/latest/tutorials/key_concepts/new_app_project.html

1. Navigate to `~/tethys/tethysdev` and run:  
   `mkdir tethysapp-az_map`  
   `cd tethysapp-az_map`
2. Scaffold and install app via CLI:  
   https://docs.tethysplatform.org/en/latest/recipes/scaffold_an_app_via_command_line.html#scaffold-an-app-via-command-line
3. Change icon (cactus.jpeg) and colors (`#FEDCBA`).
4. Build your own basic version of controllers.py based on:  
   https://docs.tethysplatform.org/en/latest/tutorials/key_concepts/beginner.html
5. Add a template extending `base.html`:  
   `~/tethys/tethysdev/tethysapp-az_map/tethysapp/az_map/templates/az_map/add_data.html`
6. Modify template with Add/Cancel buttons; add controller.
7. Add link to new page in `.../templates/az_map/base.html` (swap icon).
8. Add customized navigation tab for `base.html`.
9. Highlight.

---

## VI. Add Data to the Web App  
Ref: intermediate tutorial:  
https://docs.tethysplatform.org/en/latest/tutorials/key_concepts/intermediate.html#spatial-input-with-forms

1. Add a form for `add_data` in template and controller.
2. Add form submission handling in controller.
3. Add `az_map/model.py` with `add_data` and update controller to persist data.  
   Check `workspaces/app_workspace/data` for JSON output.
4. Complete **Develop Table View Page**:  
   - Add `get_all_data` in `model.py`  
   - Add new template `list_data.html`  
   - Add controller `list_data`  
   - Add header button to `base.html`
5. Complete **Spatial Input with Forms**:  
   - Add `location_input` gizmo  
   - Add validation  
   - Modify model to store spatial data  
   - Delete existing JSON files for consistency  
   - Create new entries  
   - Verify in Tethys portal and filesystem  
   - Replace every `dam` with `data`
6. Fix date bug where `date_built` defaults to today.  
   Change initial value (line 111 in controllers.py) to empty string. Works.
7. Render spatial data on map — major updates in `controllers.py`. (Beware date bug.)

---

## VII. Scaffold Your Own Layout (az_irrigation → map_layout_tutorial + GeoJSON)
Data hub: https://azgeo-open-data-agic.hub.arcgis.com/

1. Initial data download and prep using GeoJSON from:  
   https://azgeo-open-data-agic.hub.arcgis.com/datasets/dd15ab8c811a49e8ac1b8a7ddcb64101_0/explore
2. Reproject for validation at https://geojsonlint.com/
3. Rename `az_map` → `az_irrigation` by rescaffolding.  
   - Requires new scaffold + file copying  
   - Also redo Step I by reinstalling miniconda  
   - Note: Tethys wasn’t working until running:  
     `pip install tethysplatform` inside `conda activate tethys`
4. Remove `az_irrigation/az_map` and build directly on `map_layout_tutorial`.  
   To uninstall:  
   `tethys manage tethys_app_uninstall az_map`

---

## VIII. Add Irrigation Layer to map_layout_tutorial
1. Add clickable irrigation layer via layer menu (currently shows nothing).
2. Copy nexus layer logic to irrigation layer to display data similarly.
3. Add AZ 1960s irrigation CSV to `app_workspace/outputs/` and integrate in `get_plot_for_layer_feature`.
4. Tried to finish irrigation integration, but switching to ADOT traffic data instead.

---

## IX. Use ADOT Traffic Data Instead
1. Migrate irrigation GeoJSON/CSV → ADOT equivalents.
2. Surgical git cleanup to remove large files from history.
3. Side quest: pull Tethys project to DigitalOcean server. Success.
4. Rename and reproject traffic files.
5. Replace every `"irrigation"` with `"traffic"` in `controllers.py`.
6. Explore logic needed to extract data from ADOT CSV & GeoJSON.

---

## X. Set Up Tethys GitHub Project with README
1. Create README and move steps_taken into it.
2. Update README with basic working version of project (also got the logic for traffic layer closer, but not working yet)
