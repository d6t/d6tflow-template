do_preprocess = True

# load protected credentials
try:
    import d6tpipe
    uri = d6tpipe.utils.loadyaml('.creds.yaml').get('uri')
except:
    pass
