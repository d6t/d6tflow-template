# Sharing Workflows and Outputs
# see https://d6tflow.readthedocs.io/en/latest/collaborate.html
import d6tflow
import tasks

flow = d6tflow.Workflow(task=tasks.TaskTrain, params=params)
e = d6tflow.FlowExport(flows=flow, save=True, path_export='tasks_export.py')
e.generate()

# auto save d6tflow data to d6tpipe repo
cfg_pipe = 'pipename'
cfg_profile = 'default'
d6tflow.pipes.init(cfg_pipe,profile=cfg_profile, local_pipe=True) # work in local mode first

# execute flow
flow = d6tflow.Workflow(task = tasks.TaskTrain)
flow.run()

# auto generate files for data consumer to run
d6tflow.pipes.FlowExport(flows=flow,pipename=cfg_pipe).generate()
params=dict()
