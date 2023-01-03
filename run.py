import d6tflow
import cfg, tasks
import visualize

params=dict()
flow = d6tflow.Workflow(task=tasks.Process, params=params)
flow.preview()
flow.run()
