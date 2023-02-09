# CI Components Catalog

## Introduction

This repository contains metadata and code for the ICICLE CI Components Catalog. The CI Components Catalog tracks all major
products developed by the ICICLE AI Institute. Using the Catalog, members within ICICLE as well as their collaborators and
the general public can learn about the products being produced. 

## Schema

We are using LinkedML and JSONSchema to describe the data model associated with components in the catalog. 
The JSONSchema document can be generated from the LinkedML yaml document by doing the following:

```
$ docker run -v $(pwd):/work  -w /work/ --rm -it jstubbs/linkedml gen-json-schema ci-component.yaml

```

## Deploying the Catalog Locally


## 


