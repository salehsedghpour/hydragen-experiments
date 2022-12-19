[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7458231.svg)](https://doi.org/10.5281/zenodo.7458231)

# Abstract

This repository presents the scripts and codes regarding HydraGen, a tool that can systematically generate a wide range of microservice benchmarks that facilitate research on (i) efficient microservice development and operation, and (ii) resource management tools focused on microservices by offering capabilities beyond those of current simple static benchmarks. Our tool can serve as a common baseline for researchers to systematically evaluate, reproduce, and compare resource management strategies for microservices because it allows control over characteristics such as application complexity, application architecture, and resource allocation.

This repository contains different steps toward performing all the experiments and get the results discussed in the paper. These steps are installation, performing the experiemnts, and getting the results (drawing charts). We tried to automate most of the procedure. 

## Requirements
- Eight Machines (either Virtual or Baremetal) with at least 8 CPUs and 16GB of RAM
- [Kubernetes](https://kubernetes.io/) cluster with [Cilium CNI](https://cilium.io/)
- [Istio](https://istio.io/) as service mesh
- +100 hours for experiments execution.
- If perfroming all the experiments on [Google Cloud Platform](https://cloud.google.com/), you may need to spend $300 credit (8 VMs with  `e2-standard-8` type).