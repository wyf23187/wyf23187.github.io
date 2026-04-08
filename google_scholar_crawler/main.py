from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys

def setup_proxy():
    """Set up a free proxy to avoid Google Scholar IP bans."""
    pg = ProxyGenerator()
    try:
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        print("Proxy configured successfully")
    except Exception as e:
        print(f"Warning: Failed to set up proxy ({e}), trying without proxy", file=sys.stderr)

def fetch_scholar_data(max_retries=3):
    """Fetch Google Scholar data with retry logic."""
    last_error = None
    for attempt in range(max_retries):
        try:
            if attempt > 0:
                print(f"Retry attempt {attempt + 1}/{max_retries}")
                # Re-setup proxy on retry
                setup_proxy()

            author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
            scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
            return author
        except Exception as e:
            last_error = e
            print(f"Attempt {attempt + 1} failed: {e}", file=sys.stderr)
            import time
            if attempt < max_retries - 1:
                time.sleep(5 * (attempt + 1))

    raise last_error

try:
    setup_proxy()
    author = fetch_scholar_data()
    name = author['name']
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']:v for v in author['publications']}
    print(json.dumps(author, indent=2))
    os.makedirs('results', exist_ok=True)
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
      "schemaVersion": 1,
      "label": "citations",
      "message": f"{author['citedby']}",
    }
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
except Exception as e:
    print(f"Error fetching Google Scholar data: {e}", file=sys.stderr)
    sys.exit(1)
