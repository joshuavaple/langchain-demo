import os
import requests


def scrape_linkedin_profile(
    linkedin_profile_url: str, scrapin_api_key: str, demo_mode: bool = False
):
    """Scrape information from a LinkedIn profile,
    Manually scrape the information from a LinkedIn profile."""
    if demo_mode:
        gist_response = requests.get(
            "https://gist.githubusercontent.com/joshuavaple/dccf26db38df1374bca33458e8fbc437/raw/e5cc7b59e79f2a0acca07c27a2fb6426bc942e09/joshuale.json"
        )
        return gist_response.json()
    else:
        url = "https://api.scrapin.io/enrichment/profile"
        querystring = {"apikey": scrapin_api_key, "linkedinUrl": linkedin_profile_url}
        response = requests.request("GET", url, params=querystring)
        return response.json()
