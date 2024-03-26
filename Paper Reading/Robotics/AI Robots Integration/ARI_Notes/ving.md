- **ViNG Learning Open-World Navigation with Visual Goals**
 **[`ICRA 2021`]** *Dhruv Shah, Benjamin Eysenbach, Gregory Kahn, Nicholas Rhinehart, Sergey Levine* [(arXiv)](http://arxiv.org/abs/2012.09812) [(pdf)](./../ViNG%20-%20Learning%20Open-World%20Navigation%20with%20Visual%20Goals.pdf) (Citation: 66)
  - **Objective**:
    - Propose a **learning-based navigation** system for reaching visually indicated goals and demonstrate this system on a real mobile robot platform. 
    -  **Learning** provides an appealing alternative to conventional methods for robotic navigation: instead of reasoning about environments in terms of geometry and maps, learning can enable a robot to learn about navigational affordances, understand what types of obstacles are traversable (e.g., tall grass) or not (e.g., walls), and generalize over patterns in the environment.
  - **Problem Statement**:
    - A robot is tasked with navigating to **a goal location** $G$ given an **image observation** $o_G$ taken at $G$. 
    - Outputs of the navigation model contain continuous linear and angular velocities.
    - Conventional planning algorithms are hard to change the goal for a learned policy during deployment. Instead of navigating to a goal position, the robot is tasked to navigate to **a goal image**.
    <p align="center">
    <img src="./../../images/ViNG_overview.png" width="70%">
    </p> 

    - In addition to navigating to the goal, the robot also needs to recognize when it has reached the goal, signaling that the task has been completed.
  - **Three insights**:
    - Waypoint proposal
    - Graph pruning
    - Negative mining
  - **Procedures**:
    -  First learn a function that predicts the dynamical distance between pairs of observations, estimating how many time steps are needed to transition between them.
    -  Then use this learned dynamical distance to embed past observations into a topological graph, and plan over this graph. 
  - **Training Steps**:
    - Aim to learn a traversability function $\mathcal{T}(o_i, o_j)$, indicating whether any controller can successfully navigate between observations $o_i$ and $o_j$. More specifically, learn to predict the estimated number of time steps $d_{ij}=j-i$ required by a controller to navigate from one observation to another. 
    <p align="center">
    <img src="./../../images/ViNG_training.png" width="60%">
    </p>

    - $\mathcal{T}(o_i, o_j)$ can be learned via **(1)** supervised learning and **(2)** temporal difference learning. 
      - In **(1)** supervised learning, a **positive** dataset $\mathbb{D}_+$ contains observation pairs $(o_i, o_j)$ taken from the same trajectory and regress to the number of timestpes $d_{ij}=j-i$ elapsed between observations. 
      - In **(2)** temporal difference learning, the same experience was used. 
    - **Negative mining**: In our experiments, we found that training the distance function using only observation pairs from the same trajectory performed poorly.
      - A **Negative** Dataset $\mathbb{D}_-$ is added. Reason: training the distance function using only observation pairs from the same trajectory performed poorly. 
      - Augment the dataset by adding $\mathbb{D}_-$, which contains sampling observations from different trajectories, labeled as $d_{max}$

  - **Deploying**
    - We build a topological graph $\mathcal{M}$ using the learned distance function together with a collection of previously-observed observations ${o_t}$. Each *node* in the graph corresponds to one of these observations. 
    - Add weighted *edges* between every *node*, using weights predicted by the distance function $\mathcal{T}$.
      - **Graph Pruning**: 
        - **Problem**: As the robot gathers more experience, maintaining a dense graph of traversability across all observation nodes becomes redundant and infeasible, as the graph size grows quadratically.
        - **Solution**: we sparsify trajectories by thresholding the edges that get added to the graph: edges that are easily traversable $\left(\mathcal{T}\left(o_i, o_j\right)<\delta_{\text {sparsify }}\right)$ are not added to the graph, since the controller can traversethose edges with high probability.
    - **Planning**: Use the weighted DJ algorithm to compute the shortest path to goal, and the immediate next node in the planned path is then handed over to the controller. 
    - **Controller**: After the planner predicts a waypoint observation, the controller must output an action that takes the agent towards that waypoint.
      - **Main Challenge**: both the current state and waypoint are represented as high-dimensional observations (e.g., images).
      - $\mathcal{P}$: learn a relative position predictor that takes as input two observations $\left(o_i, o_j\right)$ and predicts the relative pose $\Delta p_{i j}$ (i.e., heading difference) between these observations.
      - PD controller to take the robot to the target waypoints via minimizing $\Delta p_{i j}$. 
    <p align="center">
    <img src="./../../images/ViNG_deploying.png" width="60%">
    </p>
  
  - **Implementation Details**:
    - $\mathcal{T}$ is a MobileNet Encoder followed by three densely connected layers to project 1024-dimensional latents to 50 class labels. 
    - $\mathcal{P}$ has similar structure, comprising of a MobileNet encoder followed by three densely connected layers projecting the 1024-dimensional latents to 3 outputs for waypoints: $\{\Delta_x, \Delta_y \}$