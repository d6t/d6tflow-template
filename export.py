import d6tflow
import tasks

params=dict()
flow = d6tflow.Workflow(task=tasks.Process, params=params)

e = d6tflow.FlowExport(flows=flow, save=True, path_export='tasks_export.py')
e.generate()
