import d6tflow
import cfg, tasks, visualize

d6tflow.show(tasks.TaskTrain())

d6tflow.run(tasks.TaskTrain())

visualize.accuracy()
visualize.plot_importances()

d6tflow.run(tasks.TaskTrain(do_preprocess=False))
visualize.accuracy(do_preprocess=False)

import importlib
importlib.reload(cfg)
importlib.reload(tasks)

d6tflow.invalidate_downstream(tasks.TaskGetData(), tasks.TaskTrain())

d6tflow.show(tasks.TaskTrain())
d6tflow.run(tasks.TaskTrain())
