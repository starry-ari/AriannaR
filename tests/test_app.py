import unittest
import os
from peewee import *

os.environ['TESTING'] = 'true'

import app
MODELS = [app.TimelinePost]
# test_order = ["test_home", "test_timeline", "test_malformed_timeline_post"] 
# unittest.TestLoader.sortTestMethodsUsing = lambda x: test_order.index(x)

class AppTestCase(unittest.TestCase):
    def setUp(self):
    
        app.mydb.create_tables(MODELS)
        self.client = app.app.test_client()

    def tearDown(self) -> None:
        app.mydb.drop_tables(MODELS)
     

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
       
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    def test_malformed_timeline_post(self):
        response = self.client.post("api/timeline_post", data={ "email": "john@example.com", "content":
        "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        print(f"{html} is the html")
        assert "Invalid name" in html

        # response = self.client.post("api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content":
        # "Hello world, I'm John!" })
        # assert response.status_code == 400
        # html = response.get_data(as_text=True)
        # assert "Invalid content" in html

        # response = self.client.post("api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content":
        # "Hello world, I'm John!"})
        # assert response.status_code == 400
        # html = response.get_data(as_text=True)
        # assert "Invalid email" in html

