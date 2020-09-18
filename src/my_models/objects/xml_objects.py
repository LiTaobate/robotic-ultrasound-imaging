from robosuite.models.objects import MujocoXMLObject

class ProbeObject(MujocoXMLObject):
    """
    Probe object
    """

    def __init__(self):
        super().__init__("my_models/assets/objects/probe.xml")

class TorsoObject(MujocoXMLObject):
    """
    Torso object
    """

    def __init__(self):
        super().__init__("my_models/assets/objects/human_torso.xml")