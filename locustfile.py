from locust import HttpUser, task

class Myuser(HttpUser):

    @task
    def load_test(self):
        self.client.get("/")