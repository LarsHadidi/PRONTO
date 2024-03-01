# PRONTO
**Pro**gressive Di**N**ner **T**our **O**ptimizer 
___

### Navigation
This repository hosts six major branches, three of which contain two sub-branches.
* [[main]](https://github.com/LarsHadidi/PRONTO)
* [[research]](https://github.com/LarsHadidi/PRONTO/tree/research/research)
* [[ui-components]](https://github.com/LarsHadidi/PRONTO/tree/ui-components/ui-components)
* [[servicelayer]](https://github.com/LarsHadidi/PRONTO/tree/servicelayer/development/servicelayer)
* [[backoffice]](https://github.com/LarsHadidi/PRONTO/tree/backoffice/development/backoffice)
* [[webclient]](https://github.com/LarsHadidi/PRONTO/tree/webclient/development/webclient)
___

<img align="right" width=33% src="https://github.com/LarsHadidi/PRONTO/assets/12017203/1aaba72c-372e-4810-83ac-b70c35dea0f4">

### What's a progressive dinner 
A progressive dinner is a dinner party with successive courses prepared and eaten at the residences of different hosts.
Usually this involves the consumption of one course at each location. More details on the [Wikipedia article](https://en.wikipedia.org/wiki/Progressive_dinner).

### Precise formulation of the progressive dinner problem
The event involves $N$ couples having each course of a three-course meal at a different person’s house, three couples at each course, every couple hosting once and no two couples meeting more than once. You can find the descripion by [Prof. D.S. Stinson](https://cs.uwaterloo.ca/~dstinson/) in his [publication](https://doi.org/10.48550/arXiv.2001.05394) on *Designing Progressive Dinner Parties* as a combinatorial problem.

<br clear="right"/>
<br/><br/>

<img align="left" width=50% src="https://github.com/LarsHadidi/PRONTO/assets/12017203/aa3c4e1a-d7b1-4c07-95ed-bb85e0a756b8">

### Optimization
Beyond finding a feasible solution, it is often desired to find a solution that minimizes the length of all travelled itineraries. This goes further than solving a multiple TSP problem.
Different methods have been investigated on these [**Jupyter Notebooks**](https://github.com/LarsHadidi/PRONTO/tree/research/research)

<br clear="left"/>

---

### CI Pipeline

On branches `servicelayer`, `backoffice` and `webclient`, three sub-brachnes are used to structure the process from development to production as shown on the diagram.

<br/>

![CI drawio (3)](https://github.com/LarsHadidi/PRONTO/assets/12017203/94606a3b-79fb-4982-aa22-0c04a6af1d4f)
