import streamlit as st
from sandbox import SessionState
import time
from src.bandit import Agent, BernoulliBandit
import numpy as np
import pandas as pd
from scipy.stats import beta
import matplotlib.pyplot as plt
import seaborn as sns

# Sidebar
go1 = st.sidebar.button("Play 1")
go2 = st.sidebar.button("Play 2")
go3 = st.sidebar.button("Play 3")
go4 = st.sidebar.button("Play 4")
go5 = st.sidebar.button("Play 5")

BANDITS = [BernoulliBandit(mean=0.1),
           BernoulliBandit(mean=0.3),
           BernoulliBandit(mean=0.5),
           BernoulliBandit(mean=0.7),
           BernoulliBandit(mean=0.9)]

ss = SessionState.get(Agent01=Agent(list_of_bandits=BANDITS, T=1000))

if go1:
    ss.Agent01.play_bernoulli_bandit(0)
if go2:
    ss.Agent01.play_bernoulli_bandit(1)
if go3:
    ss.Agent01.play_bernoulli_bandit(2)
if go4:
    ss.Agent01.play_bernoulli_bandit(3)
if go5:
    ss.Agent01.play_bernoulli_bandit(4)


## Output

st.header("Expected Distributions of Bandits")
st.text("Played so far:")
for no in range(5):
    a = ss.Agent01.bandit_beta_expectations[no].Alpha
    b = ss.Agent01.bandit_beta_expectations[no].Beta
    st.text(f"Bandit {no+1}: {a+b-2} times with {a-1} successes.")

# Configure Plot
fig, ax = plt.subplots()
x = np.linspace(0, 1, 200)

# Get expectations
expectations = {}
for no in range(5):
    a = ss.Agent01.bandit_beta_expectations[no].Alpha
    b = ss.Agent01.bandit_beta_expectations[no].Beta
    sns.lineplot(x=x, y=beta.pdf(x,a,b))
st.pyplot(fig)