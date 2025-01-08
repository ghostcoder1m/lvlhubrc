import requests

def enrich_lead(email: str):
    """Enrich lead data using Clearbit API."""
    response = requests.get(f"https://api.clearbit.com/v2/people/find?email={email}",
                            headers={"Authorization": "Bearer YOUR_API_KEY"})
    if response.status_code == 200:
        return response.json()
    else:
        return None
