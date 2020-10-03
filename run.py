import d6tflow
import cfg, tasks
import visualize

params = {}
task_ = tasks.Process(**params)
d6tflow.preview(task_)
d6tflow.run(task_)

