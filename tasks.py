import d6tflow
import sklearn, sklearn.datasets
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


import cfg

# define workflow
class TaskGetData(d6tflow.tasks.TaskPqPandas):  # save dataframe as parquet, see https://d6tflow.readthedocs.io/en/latest/targets.html
    dt_start = d6tflow.DateParameter(default=cfg.dt_start) # workflow parameters. See https://d6tflow.readthedocs.io/en/latest/advparam.html
    dt_end = d6tflow.DateParameter(default=cfg.dt_end)

    def run(self):
        iris = sklearn.datasets.load_iris()
        df_train = pd.DataFrame(iris.data,columns=['feature{}'.format(i) for i in range(4)])
        df_train['y'] = iris.target
        # optional: df_train[df_train['date']>=self.dt_start]
        self.save(df_train) # quickly save dataframe

@d6tflow.requires(TaskGetData) # define dependency. See https://d6tflow.readthedocs.io/en/latest/tasks.html
class TaskPreprocess(d6tflow.tasks.TaskPqPandas):
    do_preprocess = d6tflow.BoolParameter(default=cfg.do_preprocess) # parameter for preprocessing yes/no

    def run(self):
        df_train = self.input().load() # quickly load required data, see https://d6tflow.readthedocs.io/en/latest/tasks.html#load-input-data
        if self.do_preprocess:
            df_train.iloc[:,:-1] = sklearn.preprocessing.scale(df_train.iloc[:,:-1])
        self.save(df_train) # save task output, see https://d6tflow.readthedocs.io/en/latest/tasks.html#save-output-data

@d6tflow.requires(TaskPreprocess) # define dependency. See https://d6tflow.readthedocs.io/en/latest/tasks.html
class TaskTrain(d6tflow.tasks.TaskPickle): # save output as pickle
    model = d6tflow.BoolParameter(default='rf')

    def run(self):
        df_train = self.input().load()
        if self.model=='rf':
            model = RandomForestClassifier(n_jobs=2, random_state=0)
        else:
            model = RandomForestClassifier(n_jobs=2, random_state=0)
        
        model.fit(df_train.iloc[:,:-1], df_train['y'])
        self.save(model)
