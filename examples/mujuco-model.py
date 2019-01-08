from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import os

MODEL_XML = 'humanoid.xml'

model = load_model_from_path(MODEL_XML)
sim=MjSim(model)
viewer=MjViewer(sim)
t=0

while True:
    t+=1
    sim.step()
    viewer.render()