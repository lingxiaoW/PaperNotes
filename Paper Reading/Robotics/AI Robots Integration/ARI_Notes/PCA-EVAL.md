- **Towards End-to-End Embodied Decision Making via Multi-modal Large
  Language Model Explorations with GPT4-Vision and Beyond**
 **[`arXiv 2023`]** *Liang Chen, Yichi Zhang, Shuhuai Ren, Haozhe Zhao, Zefan Cai, Yuchi Wang, Peiyi Wang, Tianyu Liu, Baobao Chang* [(arXiv)](http://arxiv.org/abs/2310.02071) [(pdf)](./../Towards%20End-to-End%20Embodied%20Decision%20Making%20via%20Multi-modal%20Large%20Language%20Model%20-%20Explorations%20with%20GPT4-Vision%20and%20Beyond.pdf) [(Notes)](./ARI_Notes/PCA-EVAL.md) (Citation: 0)


    - **Objective:**
      - Explore the potential of Multimodal LLM (MLLM) in improving embodied decision-making process for agents. 
      - Introduce a new **benchmark** **PCA-EVAL**: Perception, Cognition, and Action. 
      - Proposed **HOLMES**, a multi-agent cooperation framework that allows LLMs to leverage MLLMs and APIs to gather multimodal information for informed decision-making.
    - PCA-EVAL includes **three control problem domains**:
      - **Autonomous driving**: Real-world transportation scenes ([traffic sign detection](https://ieeexplore.ieee.org/document/7780601))
      - **Domestic Assistance**: [ALFRED](https://askforalfred.com/)
      - **Game-playing**: [Minedojo](https://github.com/MineDojo/MineDojo)
      - Each instance in the benchmark consists of 6-element tuple:
        ``<image, question, action, answer, reason, key concept>``