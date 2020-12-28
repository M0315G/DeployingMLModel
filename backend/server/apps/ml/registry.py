
from apps.endpoints.models import Endpoint
from apps.endpoints.models import MLAlgorithm
from apps.endpoints .models import MLAlgorithmStatus

class MLRegistry:
    
    def __init__(Self):
        self.endpoints = {}
        
    def  add_algorithm(self, endpoint_name, algorithm_object, algorithm_name, algorithm_status, algorithm_version, owner, algorithm_description, algorithm_code):
        
        