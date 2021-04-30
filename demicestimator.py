#required modules
import pandas as pd
from scipy.integrate import odeint

#Implementing ODE of S.I.R Model
def sir_model(ecr,rr,total_pop,recovered,infected,n_days):

    #ecr = Effective ontact Rate
    #rr = Recovery Rate

    #R0 value of the virus
    R0 = ecr/rr
    # ODE of S.I.R Model
    def deriv(state, t, N, beta, gamma):
        S, I, R = state
        # Rate of Change of population S
        dSdt = -beta * S * I / N
        #  Rate of Change of population
        dIdt = beta * S * I / N - gamma * I
        #  Rate of Change of population
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    #total_pop = ''
    #recovered = ''
    #infected = ''
    susceptible = total_pop - infected - recovered

    # A list of days, 0-n
    days = range(0, n_days)

    # Solving ODE by using odeint
    ret = odeint(deriv,
                 [susceptible, infected, recovered],
                 days,
                 args=(total_pop, ecr, rr))
    S, I, R = ret.T

    #Dataframe for storing computed data.
    global sir_df
    sir_df = pd.DataFrame({
        'suseptible': S,
        'infected': I,
        'recovered': R,
        'day': days
        })
