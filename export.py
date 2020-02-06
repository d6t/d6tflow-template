# Sharing Workflows and Outputs
# see https://d6tflow.readthedocs.io/en/latest/collaborate.html
import d6tflow
import d6tflow.pipes

import tasks

# auto save d6tflow data to d6tpipe repo
cfg_pipe = 'pipename'
cfg_profile = 'default'
d6tflow.pipes.init(cfg_pipe,profile=cfg_profile, local_pipe=True) # work in local mode first

# execute flow
task = tasks.TaskGetData()
d6tflow.run(task) # output automatically saved in pipe directory

# auto generate files for data consumer to run
d6tflow.pipes.FlowExport(task,cfg_pipe).generate()

# when you are ready to push output, connect to remote pipe
do_push = False
if do_push:
    d6tflow.pipes.init(cfg_pipe,profile=cfg_profile, reset=True)
    pipe = d6tflow.pipes.get_pipe()
    # pipe.pull_preview()
    # pipe.pull()
    pipe.push_preview()
    pipe.push()
