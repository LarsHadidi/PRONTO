# PRONTO
**Pro**gressive Di**N**ner **T**our **O**ptimizer 
___
[<img src="https://img.shields.io/static/v1?label=&message=Open%20µService%20in%20GitHub%20Codespaces&logo=github&labelColor=2f363d&color=24292e" alt="Open µService in GitHub Codespaces"/>](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=578729262&machine=standardLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=WestEurope)
[<img src="https://img.shields.io/static/v1?label=&message=Open%20MIP%20in%20Colab&logo=googlecolab&labelColor=555555&color=007ec6" alt="Open MIP In Colab"/>](https://colab.research.google.com/github/LarsHadidi/PRONTO/blob/mathprogram/mp/PDP-MIP.ipynb)
[<img src="https://img.shields.io/static/v1?label=&message=Open%20CSP%20in%20Colab&logo=googlecolab&labelColor=555555&color=007ec6" alt="Open CSP In Colab"/>](https://colab.research.google.com/github/LarsHadidi/PRONTO/blob/mathprogram/mp/PDP-CSP.ipynb)
[<img src="https://img.shields.io/static/v1?label=&message=Open%20AQC%20in%20Colab&logo=googlecolab&labelColor=555555&color=007ec6" alt="Open AQC In Colab"/>](https://colab.research.google.com/github/LarsHadidi/PRONTO/blob/mathprogram/mp/PDP-AQC.ipynb)

## What's a progressive dinner 

A progressive dinner or, more recently, safari supper, is a dinner party with successive courses prepared and eaten at the residences of different hosts. Usually this involves the consumption of one course at each location.

[[wikipedia.org/wiki/Progressive_dinner]](https://en.wikipedia.org/wiki/Progressive_dinner)

## Precise formulation of the progressive dinner problem

The event involves N couples having each course of a three-course meal at a different person’s house, three couples at each course, every couple hosting once and no two couples meeting more than once.

[[arXiv:2001.05394 [math.CO]]](
https://doi.org/10.48550/arXiv.2001.05394)


## The optimization task

Find a solution with routes as short as possible. Either enumerate all valid solutions using a CSP Solver and evaluate those solutions according the route lengths or find an optimized solution directly using an ILP Solver or search the space of combinations using simulated annealing.
