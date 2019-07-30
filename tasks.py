
import d6tflow
import luigi
from luigi.util import inherits
import sklearn, sklearn.datasets
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


import cfg

class TaskGetData(d6tflow.tasks.TaskPqPandas):
    dt_start = luigi.DateParameter(default=cfg.dt_start)
    dt_end = luigi.DateParameter(default=cfg.dt_end)

    def run(self):
        iris = sklearn.datasets.load_iris()
        df_train = pd.DataFrame(iris.data,columns=['feature{}'.format(i) for i in range(4)])
        df_train['y'] = iris.target
        # optional: df_train[df_train['date']>=self.dt_start]
        self.save(df_train) # quickly save dataframe

class TaskPreprocess(d6tflow.tasks.TaskPqPandas):
    do_preprocess = luigi.BoolParameter(default=cfg.do_preprocess)

    def requires(self):
        return TaskGetData()

    def run(self):
        df_train = self.input().load()
        if self.do_preprocess:
            df_train.iloc[:,:-1] = sklearn.preprocessing.scale(df_train.iloc[:,:-1])
        self.save(df_train)

@inherits(TaskPreprocess)
class TaskTrain(d6tflow.tasks.TaskPickle):

    def requires(self):
        return self.clone_parent()

    def run(self):
        df_train = self.input().load()
        model = RandomForestClassifier(n_jobs=2, random_state=0)
        model.fit(df_train.iloc[:,:-1], df_train['y'])
        self.save(model)
