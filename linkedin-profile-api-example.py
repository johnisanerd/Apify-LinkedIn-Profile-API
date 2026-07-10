"""
LinkedIn Profile API: A Quick Start Example
See more at: https://apify.com/johnvc/linkedin-profile-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/linkedin-profile-api/input-schema?fpr=9n7kx3

This script shows how to call the LinkedIn Profile API on Apify from Python and
read its structured JSON output. Send one or many public LinkedIn profile URLs
and get one clean row per profile (name, headline, company, title, experience,
education, follower counts, and more).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Kept to a single profile URL so your first run stays cheap (you pay per
# profile returned). Add more URLs to the list to collect many profiles in one
# batch; they are collected in parallel and returned one row each.
run_input = {
    "profileUrls": [
        "https://www.linkedin.com/in/satyanadella",
        # "https://www.linkedin.com/in/williamhgates",
    ],
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/linkedin-profile-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} profile(s).\n")

# Show a few key fields from each profile.
for item in items:
    print(f"Name:      {item.get('name')}")
    print(f"Headline:  {item.get('headline')}")
    print(f"Company:   {item.get('currentCompany')} ({item.get('currentTitle')})")
    print(f"Location:  {item.get('location')}")
    print(f"Followers: {item.get('followers')}")
    print(f"URL:       {item.get('publicUrl')}")
    print(f"Summary:   {item.get('summary')}")
    print("-" * 60)
