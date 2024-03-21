- **BADGR An Autonomous Self-Supervised Learning-Based Navigation System**
 **[`arXiv 2020`]** *Gregory Kahn, Pieter Abbeel, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2002.05700) [(pdf)](./../BADGR%20-%20An%20Autonomous%20Self-Supervised%20Learning-Based%20Navigation%20System.pdf) (Citation: 230)

    - **Background**: Mobile robot navigation is typically regarded as a geometric problem, in which the robot’s objective is to perceive the geometry of the environment in order to plan collision-free paths towards a desired goal.
    - **Objective**:  In this work, we investigate how to move beyond these purely geometric-based approaches using a method that learns about physical navigational affordances from experience.
    - **BADGR**: an end-to-end learning-based mobile robot navigation system that can be trained with selfsupervised off-policy data gathered in real-world environments, without any simulation or human supervision.
    - **Mobile Robot Platform**:
      - Clearpath Jackal
      - Controlled with the desired linear and angular velocity
      - Sensor module: IMU, GPS, Encoder, 2 forward-facing cameras, 2D lidar, and a compass. 
      - Embedded Computer: NVIDIA Jetson TX2
      - Data is saved to an external SSD. 
    - **Data Collection**:
      - Off-policy data collection: ramdon exploration
    - **Predictive Model**:
      - Input: Sensor observations and a sequence of future intended actions
      - Output: future navigational events.
        <p align="center">
        <img src="/Paper Reading/Robotics/images/BADGR_framework.png" width="100%">
        </p>

        - CNN: process RGB images to get features for LSTM Inputs
        - LSTM: takes $H$ actions in a sequential fashion and produces $H$ outputs. 
          - These $H$ outputs are then passed through additional fully connected layers to predict all $K$ **events** for all $H$ future time steps.  
          - These predicted future **events**, such as position, if the robot collided, and if the robot drove over bumpy terrain, enable a planner to select actions that achieve desirable events, such reaching a goal, and avoid undesirable events, such as collisions and bumpy terrain. 
    - **Planning**
      - **Objective**: Given the trained neural network predictive model, this model can then be used at test time to plan and execute desirable actions.
      - **Reward function**: We first define a reward function that encodes what we want the robot to do in terms of the model’s predicted future events.
        - For example, the reward function could encourage driving towards a goal while discouraging collisions or driving over bumpy terrain.
        - Find the optimal action using zeroth order stochastic optimizer. 
