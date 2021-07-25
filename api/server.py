import time
import threading
import requests
import argparse
from flask import Flask, request, jsonify, abort
from database.interaction.interaction import DbInteraction
from database.exceptions import *
from parser.parser import *
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
        self.app.add_url_rule("/add_user_info", view_func=self.add_user_info, methods=['POST'])
        self.app.register_error_handler(404, self.page_not_found)

    def page_not_found(self, error_description):
        return jsonify(error=error_description), 404

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
        self.parse_data = threading.Thread(target=self.run_cycle)

        self.server.start()
        self.parse_data.start()
        return self.server

    def get_home(self):
        return "Api"

    def run_cycle(self):
        while(1):
            self.update_data()
            print("running")
            time.sleep(300)

    def update_data(self):
        self.db_interaction.update_roads()
        return "Updated"

    def add_user_info(self):
        request_body = dict(request.json)
        username = request_body['username']
        password = request_body['password']
        email = request_body['email']
        role = request_body['role']
        self.db_interaction.add_user_info(
            username=username,
            password=password,
            email=email,
            role=role
        )
        return f'Successfuly added {username}', 201

    def get_user_info(self, username):
        try:
            user_info = self.db_interaction.get_user_info(username)
            return user_info, 200
        except UserNotFoundException:
            abort(404, description='User not found')



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
        db_host = config['DB_HOST']
        db_port = config['DB_PORT']
        db_user = config['DB_USER']
        db_name = config['DB_NAME']
        db_password = config['DB_PASSWORD']
        server = Server(
            host=server_host,
            port=server_port,
            db_host=db_host,
            db_port=db_port,
            user=db_user,
            db_name=db_name,
            password=db_password,
            rebuild_db=1
        )
        server.run_server()


if __name__ == "__main__":
    run = WebApplication()
    run.start_app()
    


#python3 server.py --config=/Users/ilchel/projects/SkOpen/api/config.txt

