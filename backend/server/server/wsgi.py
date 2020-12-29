"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

# ML Registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier

try:
    registry = MLRegistry()   # create a ML registry
    
    # RF classifier
    rf = RandomForestClassifier()
    
    # add it to the regsitry
    registry.add_algorithm(endpoint_name="income_classifier",
                           algorithm_object=rf,
                           algorithm_name="random forest",
                           algorithm_status="production",
                           algorithm_version="0.0.1",
                           owner="Manish",
                           algorithm_description="Random Forest with basic pre and post processing",
                           algorithm_code=inspect.getsource(RandomForestClassifier))
    
except Exception as e:
    print("Exception while loading the algorithms to the registry", str(e))
                           
