# CI Components Catalog

## Introduction

This repository contains metadata and code for the ICICLE CI Components Catalog. The CI Components Catalog tracks all major
products developed by the ICICLE AI Institute. Using the Catalog, members within ICICLE as well as their collaborators and
the general public can learn about the products being produced. 

## Schema

We are using LinkML and JSONSchema to describe the data model associated with components in the catalog. 
The JSONSchema document can be generated from the LinkML yaml document by doing the following:

```
$ docker run -v $(pwd):/work  -w /work/ --rm -it jstubbs/linkml gen-json-schema ci-component.yaml

```

You can test the schema by validating the local example dataset ``components-data.yaml``, 
included in the repository, by doing the following:

```
docker run -v $(pwd):/work  -w /work/ --rm -it jstubbs/linkml linkml-validate -sci-component.yaml components-data.yaml
```

If no errors are returned, the message ``None`` will be output. 


## Deploying the Catalog Locally

A simple prototype application is being developed with Flask and Docker. You can deploy the
prototype locally using one of the following methods:

### Using Make

If you have GNU make on your computer, issuing the following command should build the
application image and start the container in one go:

```
make run
```


### Building with Docker

One can build the container image using a command such as:

```
docker build -t tapis/ci-catalog .
```

With the image build, start the application using:

```
docker run --name catalog --rm -p 5000:5000 tapis/ci-catalog
```

## Application URLs

With the application deployed locally, navigate to ``localhost:5000/data`` to see the 
catalog.

![Catalog](catalog.png)






