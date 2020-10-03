# d6tflow - Project Templates
## Clean and scalable project structure for data science projects

Templates with common design patterns for https://github.com/d6t/d6tflow

## Structure

`task.py`: workflow tasks  
`cfg.py`: parameter and other config  
`run.py`: execute workflow tasks  
`visualize.py`: use outputs for further analysis  
`visualize.ipynb`: use outputs in jupyter notebook  
`.creds.yaml`: optional file with protected credentials in [yaml format](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html), not commited to git to protect credentials  

## Clean branch

For repeat usage you don't need all those comments and can use the clean branch. Clone into an existing folder using `git clone -b clean --single-branch https://github.com/d6t/d6tflow-template.git .`

## Minimal branch

For frequent users with a variety of projects, this is the best starting point. Available as zip https://github.com/d6t/d6tflow-template/raw/master/d6tflow-template-minimal.zip

