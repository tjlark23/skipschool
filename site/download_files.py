import os
import sys
import json
import base64
import urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN = "REMOVED_SECRET"
TEAM_ID = "team_dVaxPtI3A2JQFxAQnwHDNa40"
DEPLOY_ID = "dpl_4SaJGKbm9vCNd791svBrPdHgTtGs"

with open('file_list.txt', 'r') as f:
    lines = f.readlines()

downloaded = 0
errors = 0

for line in lines:
    line = line.strip()
    if not line:
        continue
    uid, filepath = line.split('\t', 1)

    # Create directory structure
    local_path = os.path.join('files', filepath)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    # Download file
    url = f"https://api.vercel.com/v7/deployments/{DEPLOY_ID}/files/{uid}?teamId={TEAM_ID}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
            content = base64.b64decode(data.get('data', ''))
            with open(local_path, 'wb') as out:
                out.write(content)
            downloaded += 1
            if downloaded % 10 == 0:
                print(f"Downloaded {downloaded}/{len(lines)} files...")
    except Exception as e:
        print(f"Error downloading {filepath}: {e}")
        errors += 1

print(f"\nDone: {downloaded} downloaded, {errors} errors")
