from __future__ import print_function
import asyncio
import json
import logging
import time

import ECIAD_pb2
import JsonReader
import grpc
import Eciad_pb2_grpc

start_time = time.time()

jsonTaskFiles = JsonReader.getAllEciadTasks()
tasks = []
messages=[]

def DefineTaskType():
    for name in jsonTaskFiles:
        words = name.split('.' and '_')
        for word in words:
            if word == "MeasurementDescription.JSON" or word == "SpectrumResult.JSON":
                description = word.split('.')
                tasks.append({"filename": name, "description": description[0] })
                break



def createJson(index, data, code):
    name = "Response" + str(index)
    object = {"status": data.status, "data": {"firstname": data.data.firstname, "lastname": data.data.lastname}}
    with open(name, 'w') as f:
        json.dump(object, f, indent=2)


def sendTask(index):
    """
    global messages
    print("sf")
    for index, json in enumerate(jsonTaskFiles):
        if tasks[index]["description"] == "MeasurementDescription":
            messages.append(JsonReader.getMeasurementDescriptionRequest(json))
        elif tasks[index]["description"] == "SpectrumResult":
            messages.append(JsonReader.getSpectrumResultReqeust(json))
    print("sf")
    """
    messages = [
        JsonReader.getMeasurementDescriptionRequest(jsonTaskFiles[0]),
    ]
    for index, msg in enumerate(messages):
        print("Sending %s Message with: %s" % (index + 1 , msg))
        yield msg

def sendStatusRequests():
    messages = [
        JsonReader.getStatusRequest(),
    ]
    for index, msg in enumerate(messages):
        print("Sending %s Message with: %s" % (index + 1, msg))
        yield msg

async def get_EciadTask(stub):
    for idx in enumerate(jsonTaskFiles):
        responses = stub.EciadTask(sendTask(idx))
        Eciadisrunning = True
        for response in responses:
            while Eciadisrunning:
                if response.notification.code:
                    errorCategory = JsonReader.filterMessageCode(response.notification.code)["ErrorCategory"]
                    if errorCategory == "ErrorMeasurementDescription" or errorCategory == "ECIADDLLError" or errorCategory == "ErrorSpectrumResult":
                        print("die: " + str(idx) + "wurde abgebrochen1")
                        Eciadisrunning = False
                    else:
                        responses = stub.EciadTask(sendStatusRequests())
                else:
                    print("die: " + str(idx) + "wurde abgebrochen")
                    Eciadisrunning = False

                print("received %s" % (response))
                await asyncio.sleep(20)


async def run():
    with grpc.insecure_channel('192.168.200.131:50051') as channel:
        stub = Eciad_pb2_grpc.ECIADStub(channel)
        print("-------------- GetStatus --------------")
        await get_EciadTask(stub)

if __name__ == '__main__':
    logging.basicConfig()
    DefineTaskType()
    asyncio.run(run())