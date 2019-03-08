
Export the environment: `conda env export > env.yml`

Build the docker: `docker build -t some_tag -f .`

Test the code: `python -m pytest`