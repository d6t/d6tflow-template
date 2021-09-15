import d6tflow
import cfg, tasks
import visualize


flow = d6tflow.Workflow(task = tasks.Process, params = {})
flow.preview()
flow.run()
