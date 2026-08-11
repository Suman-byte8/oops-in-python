import json
from pathlib import Path

database_file = Path(__file__).parent.parent / "bank_accounts.json"
data = {'savings_accounts': [], 'current_accounts': []}

if Path(database_file).exists():
    with open(database_file, 'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

# save data to file
def save():
    with open(database_file,'w') as f:
        json.dump(data, f, indent=4)