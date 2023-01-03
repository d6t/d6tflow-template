
import d6tflow
import luigi
import datetime

class TaskPreprocess(d6tflow.tasks.TaskPqPandas):
    external=True
    persist=['data']
    dt_start=luigi.parameter.DateParameter(default=datetime.date(2010, 1, 1))
    dt_end=luigi.parameter.DateParameter(default=datetime.date(2020, 1, 1))
    do_preprocess=luigi.parameter.BoolParameter(default=True)
    
class TaskGetData(d6tflow.tasks.TaskPqPandas):
    external=True
    persist=['data']
    dt_start=luigi.parameter.DateParameter(default=datetime.date(2010, 1, 1))
    dt_end=luigi.parameter.DateParameter(default=datetime.date(2020, 1, 1))
    
class TaskTrain(d6tflow.tasks.TaskPickle):
    external=True
    persist=['data']
    dt_start=luigi.parameter.DateParameter(default=datetime.date(2010, 1, 1))
    dt_end=luigi.parameter.DateParameter(default=datetime.date(2020, 1, 1))
    do_preprocess=luigi.parameter.BoolParameter(default=True)
    
