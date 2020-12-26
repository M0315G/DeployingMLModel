from django.db import models

# Create your models here.

class Endpoint(models.Model):

	''' This Endpoint class will represent ML API endpoint.

	Attributes:
		name: The name of the endpoint, it will be used in API URL,
		owner: The string with owner name,
		created_at: The date when endpoint was created.
	'''
	
	name = models.CharField(max_length=128)
	owner = models.CharField(max_length=128)
	created_at = mdoels.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):

	''' This MLAlgorithm represents the ML algorithm object.
	
	Attributes:
		name: The name of the algorithm.
		description: The short desciption of how the algorithm works.
		code: The code of the algorithm.
		version: The version of the algorithm similar to software versioning.
		owner: The name of the owner.
		created_at: The date when MLAlgorithm was added.
		parent_endpoint: The reference to the Endpoint.
	'''

	name = models.CharField(max_length=128)
	description = models.CharField(max_length=1000)
	code = models.CharField(max_length=50000)
	version = models.CharField(max_length=128)
	owner = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):

	''' This MLAlgorithmStatus class represents the status of the MLAlgotihm which can change during time.
		
	Attributes:
		status: The status of algorithm in the endpoint. Can be: testing, staging, production, ab_testing. 
		active: The boolean flag which point to currently active status.
		created_by: The name of creator.
		created_at: The date of status creation.
		parent_mlalgorithm: The reference to corresponding MLAlgorithm.
	'''

	status = models.CharField(max_length=128)
	active = models.BooleanField()
	created_by = models.CharField(max_length =128)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASADE)


