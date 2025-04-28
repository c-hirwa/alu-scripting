#!/usr/bin/python3
"""Script that fetches top 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints the titles or None if the subreddit is invalid
    """
    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    
    # Reddit API URL for hot posts in the specified subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Make the request
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit exists (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Print the titles of the first 10 posts
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # If not a valid subreddit, print None
        print(None)
