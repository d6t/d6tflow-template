import d6tflow
import cfg, tasks, visualize

# Check task dependencies and their execution status
d6tflow.preview(tasks.TaskTrain())

# Execute the model training task including dependencies. See https://d6tflow.readthedocs.io/en/latest/run.html
d6tflow.run(tasks.TaskTrain())

# use output
visualize.accuracy()
visualize.plot_importances()

# change parameter and rerun, see https://d6tflow.readthedocs.io/en/latest/advparam.html
d6tflow.run(tasks.TaskTrain(do_preprocess=False))
visualize.accuracy(do_preprocess=False) # task output is parameter specific

# rerun flow after code changes
import importlib
importlib.reload(cfg)
importlib.reload(tasks)

# say you changed TaskGetData, reset all tasks depending on TaskGetData
d6tflow.invalidate_downstream(tasks.TaskGetData(), tasks.TaskTrain())

d6tflow.preview(tasks.TaskTrain())
d6tflow.run(tasks.TaskTrain())
