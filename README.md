[![Build Status](http://lkire.com:8082/buildStatus/icon?job=pipeline-test0%2Fmaster)](http://lkire.com:8082/job/pipeline-test0/job/master/)

Export the environment: `conda env export > env.yml`

Build the docker: `docker build -t some_tag -f .`

Test the code: `python -m pytest`

Install sphinx: `easy_install -U sphinx`
```bash
sphinx-quickstart doc
cd doc
make html
```
