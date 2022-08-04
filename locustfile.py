
from locust import task, HttpUser, constant
import logging
import time

class User(HttpUser):
    # Rate limiter have 10 token in 1 minute
    # A get request consumes 3 tokens, a post request consumes 5 tokens
    # 1 get and 1 post will be requested, HTTP 200 will return, 8 tokens will be consumed
    # The next get and post request will be responded with HTTP 429, it is marked as success
    # The process will be repeated after 60 seconds
    wait_time = constant(60)

    @task
    def first(self):
        self.client.get('/get', headers={'x-fowarded-for': 'ip: 0.0.1'})
        self.client.post('/post', headers={'x-fowarded-for': 'ip: 0.0.1'})
        with self.client.get('/get', catch_response = True, headers={'x-fowarded-for': 'ip: 0.0.1'}) as resp:
            if resp.status_code == 429:
                resp.success()
                logging.info("Rate limiter is successful")
        with self.client.post('/post', catch_response = True, headers={'x-fowarded-for': 'ip: 0.0.1'}) as resp:
            if resp.status_code == 429:
                resp.success()
                logging.info("Rate limiter is successful")
    
