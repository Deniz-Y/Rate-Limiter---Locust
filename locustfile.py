
from urllib import response
from locust import task, HttpUser, constant
import logging
import time
import random

class User(HttpUser):
    # Rate limiter have 10 token in 1 minute
    # A get request consumes 3 tokens, a post request consumes 5 tokens
    # 1 get and 1 post will be requested by the user with a random ip, HTTP 200 will return, 8 tokens will be consumed
    # The next get and post request with the same ip will be responded with HTTP 429, it is marked as success
    # The process will be repeated after 60 seconds
    # The code will be runned with a number of concurrent users
    wait_time = constant(60)
    
    num = random.randint(100,900)
    # ip = determine(num)


    @task
    def first(self):
        # self.ip
        ip = random.randint(100,900)
        self.client.get('/get', headers={'x-fowarded-for': 'ip: %s' % str(ip)})
        self.client.post('/post', headers={'x-fowarded-for': 'ip: %s' % str(ip)})
        with self.client.get('/get', catch_response = True, headers={'x-fowarded-for': 'ip: %s' % str(ip)}) as resp:
            if resp.status_code == 429:
                resp.success()
                logging.info("Rate limiter is successful")
        with self.client.post('/post', catch_response = True, headers={'x-fowarded-for': 'ip: %s' % str(ip)}) as resp:
            if resp.status_code == 429:
                resp.success()
                logging.info("Rate limiter is successful")
    
 
    
