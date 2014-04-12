analysis
========
author: Ge Yang

## Overview and Motivation
This new setup is motivated by the increasing complexity of the electron on Helium experiment. Recently, we noticed that the experiment start to require a mix of different measurements to run in conjuction with each other. Writing experiment and analytical scripts in the old way becomes very verbose. 

More importantly, our new experiment often require rapid iteration of volatile scripts that generate a different data schema each time. Have to manually look at the data file for old experiments, or try to run experiments that combine old and new measurements together becomes mentally taxing. To solve this problem, we decided on this new scripting style.

Each experiment involves the data taking and analytics. This analysis repository works in conjuction with the experiment repo to allow separation of data modle and plotting. 

## Data Organization
The data in each experiment is organized into data stacks. Each stack has a stackType, which indicates the type of measurement, and also specifies the dataschema. 

On the analytical side, a stackType specific datagetter works together with a type specific data plotter. The plotter is called via a callback function with explicity signature that's specific to the type of measurement.

In this way, things become more declaritive. Old data now can simply be plotted by calling old getter and plotter. 

Plotting of new measurements are done by simply creating newer stackTypes. 

If an experiment has multiple different measurements mingled together, you can just call the specific getting/plotter for each stack. As simple as that.
