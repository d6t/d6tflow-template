import d6tflow
import cfg, tasks
import visualize

import importlib # optional
importlib.reload(cfg)
importlib.reload(tasks)
importlib.reload(visualize)

d6tflow.preview(tasks.TaskTrain())

d6tflow.run(tasks.TaskTrain())

visualize.accuracy()
visualize.plot_importances()

d6tflow.run(tasks.TaskTrain(do_preprocess=False))
visualize.accuracy(do_preprocess=False)

d6tflow.invalidate_downstream(tasks.TaskGetData(), tasks.TaskTrain())

d6tflow.preview(tasks.TaskTrain())
d6tflow.run(tasks.TaskTrain())
