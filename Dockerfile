FROM continuumio/miniconda
# set up work directory.
WORKDIR /home/me/dev/
# copy necessary files.
COPY ./*.* ./
# install packages.
RUN conda env create -f env.yaml
# run script.
CMD python my_script.py