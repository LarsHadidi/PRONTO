# pdp-router
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=578729262&machine=standardLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=WestEurope)

## Description

**The PDP Problem reads as follows:**

*The event involves N couples having each course of a three-course meal at a different person’s house, three couples at each course, every couple hosting once and no two couples meeting more than once.*
[arXiv:2001.05394 [math.CO]](
https://doi.org/10.48550/arXiv.2001.05394)

It has been shown that the minimal amount of couples is nine and the total amount of couples must be divisible by three.

To find a valid solution, all contraints must be satisfied. The solution will contain a path for each couple consisting of three locations and two links between them.


** The Optimization**

A list of valid solutions may be generated using a CSP Solver. The routes may be of any length. To find a solution with routes as short as possible and guarantee accessibility on certain routes if enough locations provide accessibility options, a good or optimal solution is to be found.
