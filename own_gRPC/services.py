import json
import os
import user_pb2


def read_JSONs():
    status_list = []
    with open("db.json") as json_file:
        for item in json.load(json_file):
            status = user_pb2.Status(
                status=item["status"],
                data=user_pb2.User(
                    firstname=item["data"]["firstname"],
                    lastname=item["data"]["lastname"]))
            status_list.append(status)
    return status_list
