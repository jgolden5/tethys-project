import json
import os
import uuid
from pathlib import Path


def add_new_data(db_directory: Path | str, name: str, owner: str, river: str, date_built: str):
    """
    Persist new data.
    """
    # Serialize data to json
    new_data_id = uuid.uuid4()
    data_dict = {
        'id': str(new_data_id),
        'name': name,
        'owner': owner,
        'river': river,
        'date_built': date_built
    }

    data_json = json.dumps(data_dict)

    # Write to file in {{db_directory}}/datas/{{uuid}}.json
    # Make datas dir if it doesn't exist
    datas_dir = Path(db_directory) / 'data'
    if not datas_dir.exists():
        os.makedirs(datas_dir, exist_ok=True)

    # Name of the file is its id
    file_name = str(new_data_id) + '.json'
    file_path = datas_dir / file_name

    # Write json
    with file_path.open('w') as f:
        f.write(data_json)

def get_all_data(db_directory: Path | str):
    """
    Get all persisted data.
    """
    # Write to file in {{db_directory}}/data/{{uuid}}.json
    # Make data dir if it doesn't exist
    data_dir = Path(db_directory) / 'data'
    if not data_dir.exists():
        os.makedirs(data_dir, exist_ok=True)

    data = []

    # Open each json file and convert contents to python dictionaries
    for dam_json in data_dir.glob('*.json'):
        with dam_json.open('r') as f:
            dam_dict = json.loads(f.read())
            data.append(dam_dict)

    return data
