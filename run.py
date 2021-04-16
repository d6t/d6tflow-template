import d6tflow
import cfg, tasks, visualize

# Check task dependencies and their execution status
flow = d6tflow.Workflow()
flow.preview(tasks.TaskTrain)

# Execute the model training task including dependencies. See https://d6tflow.readthedocs.io/en/latest/run.html
flow.run(tasks.TaskTrain)

# use output
visualize.accuracy()
visualize.plot_importances()

# change parameter and rerun, see https://d6tflow.readthedocs.io/en/latest/advparam.html
flow1 = d6tflow.Workflow(params = {'do_preprocess': False})
flow1.run(tasks.TaskTrain)
visualize.accuracy(do_preprocess=False) # task output is parameter specific

# rerun flow after code changes
import importlib
importlib.reload(cfg)
importlib.reload(tasks)

# say you changed TaskGetData, reset all tasks depending on TaskGetData
flow.reset_downstream(tasks.TaskGetData, tasks.TaskTrain)
flow1.reset_downstream(tasks.TaskGetData, tasks.TaskTrain)

flow.preview(tasks.TaskTrain)
flow.run(tasks.TaskTrain)
