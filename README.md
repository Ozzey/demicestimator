# Project Description

## Introduction
<p>This package contains standalone code for computing data of any epidemic through various Epidemic Models (SIR, SEIR etc) . The data can be further used for studying, graphing, stimulating and predicting the spread of any epidemic.</p>

<p> **SIR Model**
A simple mathematical description of the spread of a disease in a population is the so-called SIR model, which divides the (fixed) population of N individuals into three "compartments" which may vary as a function of time.</p>

<p> **SEIR Model**
For many important infections, there is a significant incubation period during which individuals have been infected but are not yet infectious themselves. During this period the individual is in compartment E (for exposed). This is where SEIR model is used.</p>

## For The Users
The package can be installed via:
```bash
pip install epidemic_estimator
```
<p>The package can be used to call the functions of available Epidemic Models</p>

## Example for SIR Model
```python
import epidemic_estimator as ee
ee.sir_model(0.5,1/4,1000,0,1,160)
print(ee.sir_df)
```
>Here you can call the function for SIR model using
**ee.sir_model()**

Parameters:
- Effective contact Rate
- Recovery Rate
- Total population
- Recovered
- Infected
- No. Of Days

>Probable Epidemic Data is computed from the code above which can be used to plot graph, create stimulation and so on.

## Updates
Further updates with support for other models like SEIR and SIS is coming soon.

## License
[MIT](https://choosealicense.com/licenses/mit/)
