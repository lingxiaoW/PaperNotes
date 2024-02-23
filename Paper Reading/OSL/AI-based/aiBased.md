# AI-Based OSL


- **Emergent behavior and neural dynamics in artificial agents tracking
  turbulent plumes**
 **[`Nature 2021`]** *Satpreet Harcharan Singh, Floris van Breugel, Rajesh P. N. Rao, Bingni Wen Brunton* [(arXiv)](http://arxiv.org/abs/2109.12434) [(pdf)](./Emergent%20behavior%20and%20neural%20dynamics%20in%20artificial%20agents%20tracking%20turbulent%20plumes.pdf) (Citation: 4)


- **A deep reinforcement learning based searching method for source localization**
 **[`Information Sciences 2022`]** *Yong Zhao, Bin Chen, et al.* [(ELSEVIER)](https://www.sciencedirect.com/science/article/abs/pii/S0020025521012615) [(pdf)](./A%20deep%20reinforcement%20learning%20based%20searching%20method%20for%20source%20localization.pdf) (Citation: 14)
  - Frame the plume tracing process as a POMDP, where
    - **State** $s$: source term parameters (i.e., source location);
    - **Observation** $o$: the encounter time between sesnor and gas particles (i.e., how many times the sensor detects gas particles per unit time). Observation probability is calculated via a Poisson random process. The turbulence is in the Poisson random process;
    - **Station transition probability** $T$: since odor source location is fixed, station transition probability = 1;
    - **Belief** $b$: the probability of the environment is in state $s$ 
      - This is the probability of a source located a position inside the search area;
      - This probability is calculated via a Particle Filter.
  - Solve the Belif-MDP via deep Q network
    - A neural network is employed to calculate Q function;
    - **Inputs** to the network includes 6 features, specifies the distance between the robot and the estimated odor source;
    - **The output** is the robot next action.
  - Problems:
    - Why use DQN to plan the path? Since you already find the odor source, why not use a simple path planner to direct the robot to the source directly?
    - Action is too simplicity
    - Training and testing environment is identical.