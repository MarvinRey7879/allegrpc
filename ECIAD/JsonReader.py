import json
from google.protobuf.json_format import Parse, ParseDict
import ECIAD_pb2
import os, os.path

def getMeasurementDescriptionRequest(file):
    with open("Jsons/" + file) as jsonFile:
        return ECIAD_pb2.EciadRequest(efficiency_task=ParseDict(json.load(jsonFile), ECIAD_pb2.MeasurementDescription()))

def getStatusRequest():
    return ECIAD_pb2.EciadRequest(status_task=ECIAD_pb2.StatusRequest())

def getSpectrumResultReqeust(file):
    with open("Jsons/" + file) as jsonFile:
        return ECIAD_pb2.EciadRequest(reconstruction_task=ParseDict(json.load(jsonFile), ECIAD_pb2.SpectrumResult()))

def getCancelationRequest(file):
    return ECIAD_pb2.EciadRequest(stop_task=ECIAD_pb2.CancelationRequest())

def getAllEciadTasks():
    fileNames = [e for e in os.listdir("./Jsons") if e.endswith(".JSON")]
    return fileNames

def filterMessageCode(code):
    with open("Messages.json") as messages:
        for message in json.load(messages)["ErrorMessages"]:
            if int(message["Code"]) == code:
                return message


def getMessagesJSON():
    message_list = []
    with open("Messages.json") as messages:
        for message in json.load(messages)["ErrorMessages"]:
            fullmessage = {"code": message["code"],"Task Type": message["Task Type"],"ErrorCategory": message["ErrorCategory"],"Message": message["Message"]}
            message_list.append(fullmessage)
    return message_list

"""
def read_route_guide_database():
    feature_list = []
    with open("1_ASGSValidation_GMI_Offset60_TL180_NORMunc_0p05_0.JSON") as jsonFile:
            data = json.load(jsonFile)
            eciadRequest = ECIAD_pb2.EciadRequest(

                efficiency_task=ECIAD_pb2.MeasurementDescription(

                    package=ECIAD_pb2.WastePackage(
                        inner_drum=ECIAD_pb2.Drum(
                            material=ECIAD_pb2.Material(
                                elemental_composition=data["package"]["innerDrum"]["material"]["elementalComposition"],
                                type=data["package"]["innerDrum"]["material"]["type"]
                            ),
                            density=data["package"]["innerDrum"]["density"],
                            height=data["package"]["innerDrum"]["heigth"],
                            radius =data["package"]["innerDrum"]["radius"],
                            lid_thickness =data["package"]["innerDrum"]["lidThickness"],
                            bottom_thickness =data["package"]["innerDrum"]["bottomThickness"],
                            wall_thickness =data["package"]["innerDrum"]["wallThickness"],
                            offset=data["package"]["innerDrum"]["offset"],
                            shielding=ECIAD_pb2.Shielding(
                                material=ECIAD_pb2.Material(
                                    material=data["package"]["material"]["elementalComposition"],
                                    type=data["package"]["material"]["type"]

                                )
                            )

                        ),
                        outer_drum=ECIAD_pb2.Drum(
                            material=ECIAD_pb2.Material(
                                elemental_composition=data["package"]["outerdrum"]["material"]["elementalComposition"],
                                type=data["package"]["outerdrum"]["material"]["type"]
                            ),
                            density=data["package"]["outerdrum"]["density"],
                            height=data["package"]["outerdrum"]["heigth"],
                            radius=data["package"]["outerdrum"]["radius"],
                            lid_thickness=data["package"]["outerdrum"]["lidThickness"],
                            bottom_thickness=data["package"]["outerdrum"]["bottomThickness"],
                            wall_thickness=data["package"]["outerdrum"]["wallThickness"],
                            offset=data["package"]["outerdrum"]["offset"],
                            shielding=ECIAD_pb2.Shielding(
                                material=ECIAD_pb2.Material(
                                    elemental_composition=data["package"]["material"]["elementalComposition"],
                                    type=data["package"]["material"]["type"]
                                )
                            )
                        ),
                        fill_factor=data["package"]["fillFactor"],
                        material= ECIAD_pb2.Material(
                            elemental_composition=data["package"]["material"]["elementalComposition"],
                            type=data["package"]["material"]["type"]
                        ),
                        density=data["package"]["density"],
                        distr=data["package"]["distr"],
                        unc_waste_density=data["package"]["uncWasteDensity"]
                    ),
                    setup=ECIAD_pb2.MeasurementSetup(
                        detector=ECIAD_pb2.DetectorDescription(
                            length=data["setup"]["detector"]["length"],
                            diameter=data["setup"]["detector"]["diameter"],
                            dead_layer_thickness=data["setup"]["detector"]["deadLayerThickness"],
                            distance=data["setup"]["detector"]["distance"],
                            borehole_length=data["setup"]["detector"]["boreholeLength"],
                            borehole_diameter=data["setup"]["detector"]["boreholeDiameter"],
                            holder_inner_diameter=data["setup"]["detector"]["holderInnerDiameter"],
                            holder_outer_diameter=data["setup"]["detector"]["holderOuterDiameter"],
                            endcap_diameter=data["setup"]["detector"]["endcapDiameter"],
                            endcap_thickness=data["setup"]["detector"]["endcapThickness"],
                            window_thickness=data["setup"]["detector"]["windowThickness"],
                            material=ECIAD_pb2.Material(
                                elemental_composition=data["setup"]["detector"]["material"]["elementalComposition"],
                                type=data["setup"]["detector"]["material"]["type"]
                            ),
                            window_density=data["setup"]["detector"]["windowDensity"],
                        ),

                        collimator=ECIAD_pb2.CollimatorDescription(
                            length=data["setup"]["collimator"]["length"],
                            outer_width=data["setup"]["collimator"]["outerWidth"],
                            outer_height=data["setup"]["collimator"]["outerHeight"],
                            inner_radius=data["setup"]["collimator"]["innerRadius"],
                            distance_detector=data["setup"]["collimator"]["distanceDetector"],
                            frustrum_length=data["setup"]["collimator"]["frustrumLength"],
                            inner_frustrum_width=data["setup"]["collimator"]["innerFrustrumWidth"],
                            inner_frustrum_height=data["setup"]["collimator"]["innerFrustrumHeight"],
                            outer_frustrum_width=data["setup"]["collimator"]["outerFrustrumWidth"],
                            outer_frustrum_height=data["setup"]["collimator"]["outerFrustrumHeight"],
                        ),

                        detector_distance=data["setup"]["detectorDistance"],
                        initial_detector_height=data["setup"]["initialDetectorHeight"],
                        segment_height=data["setup"]["segmentHeight"] ,
                        tomolight_mode=data["setup"]["tomolightMode"],
                        tomolight_offset=data["setup"]["tomolightOffset"],
                    ),
                    model=["model"]
                )
            )
return eciadRequest

"""""