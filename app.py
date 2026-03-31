import requests

def fetch_github_events():
    """Fetches the latest events from the GitHub public timeline."""
    url = "https://github.com"
    try:
        response = requests.get(url)
        # Raise an exception for bad status codes (4XX or 5XX)
        response.raise_for_status() 
        events = response.json()
        print(f"Successfully fetched {len(events)} events from GitHub API.")
        # Print the first event details as an example
        if events:
            first_event = events[0]
            print(f"\nFirst event details:")
            print(f"  Type: {first_event.get('type')}")
            print(f"  Repo: {first_event.get('repo', {}).get('name')}")
            print(f"  Actor: {first_event.get('actor', {}).get('display_login')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_github_events()
