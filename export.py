import d6tflow
import d6tflow.pipes

import tasks

cfg_pipe = 'pipename'
cfg_profile = 'default'
d6tflow.pipes.init(cfg_pipe,profile=cfg_profile, local_pipe=True)

task = tasks.TaskGetData()
d6tflow.run(task)

d6tflow.pipes.FlowExport(task,cfg_pipe).generate()

do_push = False
if do_push:
    d6tflow.pipes.init(cfg_pipe,profile=cfg_profile, reset=True)
    pipe = d6tflow.pipes.get_pipe()
    # pipe.pull_preview()
    # pipe.pull()
    pipe.push_preview()
    pipe.push()
