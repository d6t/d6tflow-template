
import d6tflow
import luigi
import datetime

class GetData(d6tflow.tasks.TaskPqPandas):
    external=True
    persist=['data']
    
class Process(d6tflow.tasks.TaskPqPandas):
    external=True
    persist=['data']
    optional=luigi.parameter.BoolParameter(default=False)
    
