
- **GNM: A General Navigation Model to Drive Any Robot**
 **[`ICRA 2023`]** *Dhruv Shah, Ajay Sridhar, Arjun Bhorkar, Noriaki Hirose, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2210.03370) [(pdf)](./../GNM%20-%20A%20General%20Navigation%20Model%20to%20Drive%20Any%20Robot.pdf) [(Notes)](./ARI_Notes/gnm.md) (Citation: 35)
  - **Overall:** this is a follow-up work of the ViNG, which proposes a universal model for vision-based navigation on multiple robotic platforms.
  - **Objective:**
    - Study how a *general* goal-conditioned model for vision-based navigation can be trained on data obtained from many distinct but structurally similar robots to enable broad generalization across environments and embodiments. 
    - Using a pre-trained navigation model with broad generalization capabilities can bootstrap applications on novel robots going forward. 
  - **Dataset**:
    - 8 datasets collected on robotic platforms with varying dynamics, sensors, adn behaviors.
    - 60 hours of real-world navigation trajectories.
    - Contains forward-facing RGB images, paired with robot's commanded actions and local odometry measurements. 
  - **General Navigation Model**: 
    - A robot is tasked with navigting to a goal location $G$ specified as an image observation $o_G$ taken at $G$.
    <p align="center">
    <img src="./../../images/gnm.png" width="80%">
    </p>
   
    - Architecture:
      - **Embodiment Context**: a stack of past 5 consecutive observations
      - **Output**: future waypoints + temporal distance 
  - **Training Details**:
    - Use a combination of image-goal pairs sampled from the same trajectory in the dataset as "positives" and "negatives" sampled from different trajectories, to obtain training data pairs. 
