import d6tflow
import cfg, tasks

params=dict()
task=tasks.Process

flow = d6tflow.Workflow(task=task, params=params)
flow.preview()
flow.run()
