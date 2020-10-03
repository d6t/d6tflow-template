do_preprocess = True

import datetime
dt_start = datetime.date(2010,1,1)
dt_end = datetime.date(2020,1,1)

# load protected credentials
try:
    import yaml
    with open('.creds.yaml') as fh:
        cfg_yaml = yaml.safe_load(fh)
except:
    pass
