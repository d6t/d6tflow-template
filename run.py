import d6tflow
import cfg, tasks, visualize

# Check task dependencies and their execution status
flow = d6tflow.Workflow(task=tasks.TaskTrain)
flow.preview()

# Execute the model training task including dependencies. See https://d6tflow.readthedocs.io/en/latest/run.html
flow.run()

# use output
visualize.accuracy()
visualize.plot_importances()

# change parameter and rerun, see https://d6tflow.readthedocs.io/en/latest/advparam.html
params = dict(do_preprocess=False)
flow1 = d6tflow.Workflow(params=params, task=tasks.TaskTrain)
flow1.run()
visualize.accuracy(do_preprocess=False)  # task output is parameter specific

# rerun flow after code changes
import importlib

importlib.reload(cfg)
importlib.reload(tasks)

# say you changed TaskGetData, reset all tasks depending on TaskGetData
flow.reset_downstream(tasks.TaskGetData, tasks.TaskTrain)
flow1.reset_downstream(tasks.TaskGetData, tasks.TaskTrain)

flow.preview()
flow.run()
