from __future__ import print_function
import os
import json
import logging
import time

import grpc
import user_pb2
import user_pb2_grpc

count = 0
start_time = 0

def filterAllJsons():
    names = [e for e in os.listdir() if e.startswith("request")]
    return names

def get_one_status(stub, user):
    global count
    status = stub.GetStatus(user)
    if not status.data:
        print("Server returned incomplete Status")
        return
    if status.status:
        elapsed_time = round(time.time() - start_time, 3)
        print("Status is %s from %s in %s soconds" % (status.status, status.data, elapsed_time))
        createJson(count, status)
    else:
        print("Found no Status from %s" % status.data)

def createJson(index, data):
    name = "Response" + str(index)
    object = {"status":data.status, "data": {"firstname": data.data.firstname, "lastname": data.data.lastname}}
    with open(name, 'w') as f:
        json.dump(object, f, indent=2)

def getDataFromJsons(filenum):
    user = ""
    jsonfile = filterAllJsons()
    with open(str(jsonfile[filenum])) as json_file:
        data2 = json.load(json_file)
        user = user_pb2.User(firstname=data2["firstname"],lastname=data2["lastname"])
    return user


def get_status(stub):
    global start_time
    start_time = time.time()
    global count
    get_one_status(stub, getDataFromJsons(count))
    count += 1
    get_one_status(stub, getDataFromJsons(count))




def run():
    with grpc.insecure_channel('localhost:40') as channel:
        stub = user_pb2_grpc.RouteGuideStub(channel)
        print("-------------- GetStatus --------------")
        get_status(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()