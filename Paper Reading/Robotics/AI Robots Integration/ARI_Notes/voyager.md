- **Voyager An Open-Ended Embodied Agent with Large Language Models**
 **[`arXiv 2023`]** *Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar* [(arXiv)](http://arxiv.org/abs/2305.16291) [(pdf)](./../Voyager%20An%20Open-Ended%20Embodied%20Agent%20with%20Large%20Language%20Models.pdf) (Citation: 254)

  - **What is Voyager?**
    - **Voyager** is the **first LLM-powered embodied lifelong learning agent** that operates within the virtual realm of **Minecraft**.
    - It continuously **explores the Minecraft world**, acquires a diverse range of skills, and makes novel discoveries—all without any human intervention.

  - **Key Components of Voyager:**
    - **Automatic Curriculum**: Voyager employs an **automatic curriculum** that maximizes exploration. This ensures that it constantly seeks out new experiences and challenges.
    - **Skill Library**: The agent maintains an **ever-growing skill library** containing executable code for storing and retrieving complex behaviors. These skills empower Voyager to perform various tasks.
    - **Iterative Prompting Mechanism**: Voyager's **new iterative prompting mechanism** incorporates environment feedback, execution errors, and self-verification. This mechanism continually improves the agent's programs and abilities.

  - **Interaction with GPT-4**:
    - Voyager communicates with **GPT-4** via **blackbox queries**, bypassing the need for fine-tuning model parameters. This efficient interaction allows Voyager to leverage GPT-4's language capabilities without extensive training.

  - **Impressive Abilities**:
    - **In-Context Lifelong Learning**: Empirically, Voyager demonstrates **strong in-context lifelong learning capability**.
    - **Minecraft Proficiency**: Voyager excels at playing Minecraft, achieving remarkable feats:
      - Obtaining **3.3 times more unique items**.
      - Traveling **2.3 times longer distances**.
      - Unlocking key tech tree milestones up to **15.3 times faster** than prior state-of-the-art methods.

  - **Generalization Across Worlds**:
    - Voyager's skills are **temporally extended, interpretable, and compositional**. This allows it to **utilize the learned skill library** even in a **new Minecraft world**, solving novel tasks from scratch—a feat that other techniques struggle to achieve.