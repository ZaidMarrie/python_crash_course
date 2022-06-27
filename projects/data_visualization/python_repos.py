import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo in repo_dicts:
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")
