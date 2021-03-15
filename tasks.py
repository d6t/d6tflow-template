import d6tflow
import pandas as pd


import cfg

class GetData(d6tflow.tasks.TaskPqPandas):

    def run(self):
        df = pd.DataFrame({'a':range(10)})
        self.save(df)

@d6tflow.requires(GetData)
class Process(d6tflow.tasks.TaskPqPandas):
    optional = d6tflow.BoolParameter(default=False)

    def run(self):
        df = self.input().load()
        if self.optional:
            df = df*2
        self.save(df)
