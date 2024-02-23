# Autonomous Driving 

- **Large Language Models for Autonomous Driving Real-World Experiments**
 **[`arXiv 2023`]** *Can Cui, Zichong Yang, Yupeng Zhou, Yunsheng Ma, Juanwu Lu, Lingxi Li, Yaobin Chen, Jitesh Panchal, Ziran Wang* [(arXiv)](http://arxiv.org/abs/2312.09397) [(pdf)](./LLM-based%20AD/Large%20Language%20Models%20for%20Autonomous%20Driving%20with%20Real-World%20Experiments.pdf) (Citation: 0)

<p align="center">
  <img src="./imgs/talk2drive.png" width="50%">
</p>

  - This paper presents a Talk-to-Drive LLM to process verbal commands from humans and make autonomous driving decisions with contextual information.  
  - **Problems on traditional autonomous driving**:
    - Traditional AD rely on manually configured human preferences. 
    - Conventional systems struggle to interpret and adapt to the abstract instructions from humans. 
    - Most current autonomous driving systems are trained on limited and model-specific driving data, which results in the deficiency of driving context information and a large database of common sense that would greatly help decision-making. Therefore, there are underlying risks for the system to make bad decisions in unseen or rare scenarios. 
  - Talk-to-Drive transforms verbal commands from humans into textual instructions, which are then processed by LLMs in the cloud. 
    - LLMs generate specific driving codes that are executed by the autonomous vehicle, adjusting driving behaviors and control parameters to align with the human's preferences. 
    - Talk2Drive allows for more natural and intuitive communications with the vehicle. 
    - **LLM Inputs** include human commands, weather (openweather API), traffic/road (TomTom API), and map information (OpenStreetMap API).
    - **LLM output** icnludes executable codes used for planning and control. The generated code adjust control parameters like the *look-ahead distance* and *look-ahead ratio* to optimize pure pursuit performance.
    - The LLMs are trained using **in-context learning**, coupled with **chain-of-thought prompting**. 
      - In-context learning (ICL): is a method of prompt engineering where demonstrations of the task are provided to teh model as part of the prompt in natural language. With ICL, you can use off-the-shelf LLMs to solve novel tasks without the need for **fine-tuning**.
  - **Problem of LLM-based Agent in AD**:
    - LLM's **latency** is too large.

<br />

- **LaMPilot An Open Benchmark Dataset for Autonomous Driving with Language
  Model Programs**
 **[`arXiv 2023`]** *Yunsheng Ma, Can Cui, Xu Cao, Wenqian Ye, Peiran Liu, Juanwu Lu, Amr Abdelraouf, Rohit Gupta, Kyungtae Han, Aniket Bera, James M. Rehg, Ziran Wang* [(arXiv)](http://arxiv.org/abs/2312.04372) [(pdf)](./LLM-based%20AD/LaMPilot%20An%20Open%20Benchmark%20Dataset%20for%20Autonomous%20Driving%20with%20Language%20Model%20Programs.pdf) (Citation: 0)

  - **Objective:** Introduce LaMPilot Benchmark specifically designed to quantitatively evaluate the efficacy of Large Language MOdels (LLMs) in translating human driectives into actionable driving policies. 
  - **Problems of Existing planners** rely on clear objectives and constraints to guide their deicisions. 
    - However, when faced with arbitrary commands like "overtake the car in front of me", existing planners struggle to handle them effectively. 
  - Research Gaps: 
    - There is a lack of datasets specifically for evalutaing and comparing the capacity of LLM-based models in teh context of autonomous driving. 
    - Controlling autonomous vehicles requires careful consideration due to its safety-critical nature. Existing frameworks often prioritize successful execution of actions predicted by LLMs without adequately addressing safety concerns.
  - Problem Statement:
    - Define a benchmark $B$ as the tuple $<S, A, T, I>$, where
      - $S$: the states of the vehicle and env.
      - $A$: set of actions for the vehicle
      - $T$: transition model, encapsulating the dynamics of the env.
      - $I$: high-level instructions that guide the planning for the vehicle
    - For each task in benchmark $B$, we begin form an initial state $b$. aiming to reach a goal state in $g$. The benchmark outlines a policy rollout for each task.
    - The rollout is steered by the conditional probability $p(a_{t+1}|s_t, I)$ and concludes upon arrival at a goal state $g$. Note that the agent does not have direct access to the goal state $g$, but only a high-level instruction $I$.
    - **An example**: consider the instruction $I$="Make a right lane change". If the initial state $s$ includes the ego vehicle in the curretn lane $l \in s$, the policy ``set_target_lane(get_right_lane(ego))`` will enact a series of state-action pairs. This process transitions the vehicle from its current state $l\in s$ to a new state $l'\in s'$, where $l'$ is the lane to the right of $l$. 
  - Simulator: [HighwayEnv](https://github.com/Farama-Foundation/HighwayEnv) 
  - Input Prompt to LLMs:
    - Environmental contexts (provided by the simulator) are encapusulated into a **structured language generator**, including information about other vehicles on the road, the ego vehicle, and the map. 
    <p align="center">
    <img src="./imgs/inputprompt.png" width="50%">
    </p>
    
  - **Outputs of LLM:** The LLM receives prompts and is responsible for generating a completion. The completion produced by the LLMs is anticipated to be valid functions, written using the provided APIs.
    - **API Docs**: bridge the gap between the LLM outputs and low-level controls. Examples are presented below: 
    <p align="center">
    <img src="./imgs/api_example1.png" width="60%">
    <img src="./imgs/api_example2.png" width="60%">
    </p>

  - **Evaluator**: 
    - Safety Metric: time to collision
    - Comfort Metric: speed variance
    - Efficiency Metric: time efficiency of the pollicy code
  - **Baselines**: rule-based models are favored for their deterministic and interpretable nature. 
    - Intelligent Driver Model (IDM)
    - Minimizing Overall Braking Induced by Lane Changes (MOBIL)
    - Human Feedback Baselines
    <p align="center">
    <img src="./imgs/human_feedback.png" width="50%">
    </p>
    
    - After an LLM generates a policy program $P$, it can intergate feedback $F$ to receive context-specific guidance, enabling the LLM to refine its output. This approach does not involve calculating gradients or modifying model weights. Instead, we introduce a code repository module, which functions as a vector database. This repository allows for the storage and retrieval of effective code snippets to be used in similar situations.  

  - **Conclusion**: the ongoing need for substantial improvements for LLMs to better support instruction following in driving tasks. 

<br />

- **Reason2Drive Towards Interpretable and Chain-based Reasoning for
  Autonomous Driving**
 **[`arXiv 2023`]** *Ming Nie, Renyuan Peng, Chunwei Wang, Xinyue Cai, Jianhua Han, Hang Xu, Li Zhang* [(arXiv)](http://arxiv.org/abs/2312.03661) [(pdf)](./LLM-based%20AD/Reason2Drive%20-%20Towards%20Interpretable%20and%20Chain-based%20Reasoning%20for%20Autonomous%20Driving.pdf) (Citation: 0)

  - Research in Autonomous System using LLMs is hindered by the lack of datasets with annotated reasoning chains that explain the decision-making processes in driving. To bridge this gap, this work proposes Reason2Drive, a benchmark dataset with over 600K video-text pairs. 
  - Characterize the autonomous driving process as a sequential combination of perception, prediction, and reasoning steps. 
  - Traditional end-to-end approaches have been developed to derive control signals directly from sensor inputs, treating the system as a black box that requires extensive data for training. However, thsi approach tends to obscure the underlying logic of decisions, complicating failure diagonosis in real-world applications. 
  - By contrast, VLMs have the potential to provide a more thorough understanding and explicit explanation for reliable decision-making. 
    <p align="center">
    <img src="./imgs/reason2drive.png" width="70%">
    </p>

  - Most existing datasets often oversimplify the complex processes of driving into straightforward question-answering tasks with only a few specific tasks covered. 
  - They found that 
    - Most LLMs struggle to effectively leverage perceptual pirors, resulting in subpar reasoning performance.
    - Constrained by the language model functioning solely as a decoder, these methods often fail to deliver accuarte perceptual results.  
    <p align="center">
    <img src="./imgs/reason2drive_detailed.png" width="100%">
    </p>

  - Model Architecture
    <p align="center">
    <img src="./imgs/reason2drive_model.png" width="100%">
    </p>
    
    - Vision Encoder: Pre-trained [Blip-2](https://arxiv.org/pdf/2301.12597.pdf) visual encoder. 
    - Prior Tokenizer: 2-layer MLP that extracts local image features and positional embeddings from visual priors. 
    - Q-Former: align the non-text features into textual domain
    - LLM: generate final text output.
    - Instructed Vision Decoder: A transformer decoder for features alignments


