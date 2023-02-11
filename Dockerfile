# Image: tapis/ci-catalog

FROM python:3.10
RUN pip install Flask==2.2
RUN pip install pyyaml

# application directory
RUN mkdir /catalog

# data
ADD components-data.yaml /catalog/components-data.yaml

# code 
ADD catalog /catalog

WORKDIR /catalog
# CMD ["flask", "--app", "app", "--debug", "run"]
CMD ["python", "app.py"]