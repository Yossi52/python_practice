import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        self.response = requests.get(blog_url)
        self.blog_data = self.response.json()
