
from locust import task, HttpUser, constant
import logging

class User(HttpUser):
    # Rate limiter have 10 token in 1 minute
    # A get request consumes 3 tokens
    # The application will respond 200 to 3 request and 429 to rest in 1 minute
    # At the 8th 16th 24th 32nd 40th 48th 56th 64th 72nd 80th 88th 96th 104th 112nd 120th seconds locust will send a get request
    # 9 of the 15 requests in 2 minutes will be banned
    # Hence, approximately 60% of the requests will fail
    wait_time = constant(8)


    @task
    def first_endpoint(self):

        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.1'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.2'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.3'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.4'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.5'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.6'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.7'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.8'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.9'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.1.0'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.1.1'})
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.1.2'})
 
        




