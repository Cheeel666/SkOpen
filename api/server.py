import time
import threading
import requests
import argparse
from flask import Flask, request
from database.interaction.interaction import DbInteraction
import sys
sys.path.append("../")
from api.utils import *

class Server:
    def __init__(self, host, port, db_host, db_port, user, db_name, password, rebuild_db=False):
        self.host = host
        self.port = port

        self.db_interaction = DbInteraction(
            host=db_host,
            port=db_port,
            user=user,
            password=password,
            db_name=db_name,
            rebuild_db=True
        )

        self.app = Flask(__name__)
        self.app.add_url_rule("/shutdown", view_func=self.shutdown)
        self.app.add_url_rule("/", view_func=self.get_home)
        self.app.add_url_rule("/home", view_func=self.get_home)

    def shutdown_server(self):
        request.get(f"http//{self.host}:{self.port}/shutdown")

    def shutdown(self):
        terminate_func = request.environ.get("werkzeug.server.shutdown")
        if terminate_func:
            terminate_func()

    def run_server(self):
        self.server = threading.Thread(
            target=self.app.run, kwargs={"host": self.host, "port": self.port}
        )
        self.server.start()
        return self.server

    def get_home(self):
        return "Api"

    def add_user_info(self):
        request_body = dict(request.json)
        username = request_body['username']
        password = request_body['password']
        email = request_body['email']
        self.db_interaction.add_user_info(
            username=username,
            password=password,
            email=email,
            role=3
        )
        return f'Successfuly added {username}', 201


    def get_user_info(self):



class WebApplication:
    def __init__(self):
        pass

    def start_app(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", type=str, dest="config")

        args = parser.parse_args()

        config = config_parser(args.config)

        server_host = config['SERVER_HOST']
        server_port = int(config['SERVER_PORT'])
        
        server = Server(
            host=server_host,
            port=server_port
        )
        server.run_server()
        
        while(0):
            get_data()

            time.sleep(300)



    def get_data(self):
        pass


if __name__ == "__main__":
    run = WebApplication()
    run.start_app()
    


#python3 server.py --config=/Users/ilchel/Desktop/projects/agregator/api/config.txt