import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)


    @task(1)
    def encrypt(self):
        self.client.post("/encrypt", json={"message":"Hello MY world", "salt":20})
  

    
        